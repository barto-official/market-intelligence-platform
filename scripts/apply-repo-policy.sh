#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  apply-repo-policy.sh -o OWNER -r REPO [-b BRANCH] [-t TOKEN]

Options:
  -o  GitHub org/user (owner)
  -r  Repository name
  -b  Branch to protect (default: repo default branch)
  -t  Token (optional if GITHUB_TOKEN is set)
  -h  Show help

Env:
  GITHUB_TOKEN  Personal access token or GitHub App user token

Examples:
  GITHUB_TOKEN=... ./scripts/apply-repo-policy.sh -o myorg -r myrepo
  ./scripts/apply-repo-policy.sh -o myorg -r myrepo -b main -t ghp_...
EOF
}

log() { printf '%s\n' "$*"; }
err() { printf 'ERROR: %s\n' "$*" >&2; }

OWNER=""
REPO=""
BRANCH=""
TOKEN="${GITHUB_TOKEN:-}"

while getopts ":o:r:b:t:h" opt; do
  case "$opt" in
    o) OWNER="$OPTARG" ;;
    r) REPO="$OPTARG" ;;
    b) BRANCH="$OPTARG" ;;
    t) TOKEN="$OPTARG" ;;
    h) usage; exit 0 ;;
    \?) err "Unknown option: -$OPTARG"; usage; exit 2 ;;
    :)  err "Missing argument for -$OPTARG"; usage; exit 2 ;;
  esac
done

if [[ -z "$OWNER" || -z "$REPO" ]]; then
  err "OWNER and REPO are required."
  usage
  exit 2
fi

if [[ -z "$TOKEN" ]]; then
  err "Provide a token via -t or GITHUB_TOKEN."
  exit 2
fi

API="https://api.github.com"
HDR_ACCEPT="Accept: application/vnd.github+json"
HDR_AUTH="Authorization: Bearer ${TOKEN}"
HDR_VER="X-GitHub-Api-Version: 2022-11-28"
HDR_CT="Content-Type: application/json"

policy_dir=".github/repo-policy"
repo_security_json="${policy_dir}/repo-security.json"
codeql_json="${policy_dir}/codeql-default-setup.json"
branch_protection_json="${policy_dir}/branch-protection.json"

require_file() {
  local f="$1"
  if [[ ! -f "$f" ]]; then
    err "Missing required file: $f"
    exit 2
  fi
}

validate_json() {
  local f="$1"
  python3 -m json.tool "$f" >/dev/null \
    || { err "Invalid JSON: $f"; exit 2; }
}

require_file "$repo_security_json"
require_file "$codeql_json"
require_file "$branch_protection_json"

log "Validating policy JSON files"
validate_json "$repo_security_json"
validate_json "$codeql_json"
validate_json "$branch_protection_json"

api_call() {
  local method="$1"
  local url="$2"
  local data_file="${3:-}"
  local resp_file=""
  local http_code

  resp_file="$(mktemp)"
  trap '[[ -n "${resp_file:-}" ]] && rm -f "$resp_file"' RETURN

  # Build curl args safely (no word-splitting surprises)
  local -a curl_args=(
    -sS -L
    -X "$method"
    -H "$HDR_ACCEPT"
    -H "$HDR_AUTH"
    -H "$HDR_VER"
  )

  if [[ -n "$data_file" ]]; then
    curl_args+=(-H "$HDR_CT" --data-binary @"$data_file")
  fi

  # Note: curl itself can fail (network/TLS). Capture exit code.
  if ! http_code="$(curl "${curl_args[@]}" -w "%{http_code}" -o "$resp_file" "$url")"; then
    err "$method $url failed at transport level (curl error)."
    err "curl output:"
    cat "$resp_file" >&2 || true
    exit 1
  fi

  # Success is any 2xx
  if [[ "$http_code" -lt 200 || "$http_code" -ge 300 ]]; then
    err "$method $url failed with HTTP $http_code"
    cat "$resp_file" >&2
    exit 1
  fi

  cat "$resp_file"
}
get_default_branch() {
  local repo_json
  repo_json="$(api_call GET "${API}/repos/${OWNER}/${REPO}")"

  printf '%s' "$repo_json" | python3 -c '
import json, sys

data = sys.stdin.read().strip()
if not data:
    sys.exit("ERROR: Empty JSON response while reading repository metadata.")

obj = json.loads(data)
branch = obj.get("default_branch")
if not branch:
    sys.exit("ERROR: '\''default_branch'\'' missing in repository response.")

print(branch)
'
}

ensure_branch_exists() {
  local branch="$1"
  # If the branch doesn't exist, GitHub returns 404 and api_call will exit with the response body.
  api_call GET "${API}/repos/${OWNER}/${REPO}/branches/${branch}" >/dev/null
}

# Determine default branch if BRANCH not provided
if [[ -z "$BRANCH" ]]; then
  log "Determining default branch"
  BRANCH="$(get_default_branch)"
fi

log "Applying policy to ${OWNER}/${REPO} (branch: ${BRANCH})"

log "Preflight: ensure branch exists (${BRANCH})"
ensure_branch_exists "$BRANCH"

log "1) Configure repo security_and_analysis"
api_call PATCH "${API}/repos/${OWNER}/${REPO}" "$repo_security_json" >/dev/null

log "2) Enable vulnerability alerts (Dependabot alerts + dependency graph)"
api_call PUT "${API}/repos/${OWNER}/${REPO}/vulnerability-alerts" >/dev/null

log "3) Enable automated security fixes (Dependabot security updates)"
api_call PUT "${API}/repos/${OWNER}/${REPO}/automated-security-fixes" >/dev/null

log "4) Configure CodeQL default setup (code scanning)"
api_call PATCH "${API}/repos/${OWNER}/${REPO}/code-scanning/default-setup" "$codeql_json" >/dev/null

log "5) Apply branch protection"
api_call PUT "${API}/repos/${OWNER}/${REPO}/branches/${BRANCH}/protection" "$branch_protection_json" >/dev/null

log "Done."

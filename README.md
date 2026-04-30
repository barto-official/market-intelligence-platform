# What this repository contains

1. READMEs templates to choose
1. Package setup via pyproject (uv recommended)
1. Repository prepared for collaboration: [CODE_OF_CONDUCT](./CODE_OF_CONDUCT.md), [CONTRIBUTING](./CONTRIBUTING.md), [CODEOWNERS](/.github/CODEOWNERS)
1. Documentation set-up via **mkdocs**
1. Pre-commit and CI gates in `./github/workflows`
1. [VsCode settings](./.vscode)

# How To Use This Template

1. Click green button "Use This Template" on the right upper corner of this repo.

1. Fill next form with Your data.

1. Choose the README style — either for public presence or internal.

   - Public is more suited for packages.
   - Remove the unused README
   - Change the name of the readme that you have chosen to README.MD so that it's the main file.

1. Run `repo_polcy.sh` from the root folder. This Bash script enforces a standardized security and branch-protection policy using JSON specs that ara applied using Github Rest API. Concretely it:

   - Repository settings: Advanced Security, Code scanning, Secret scanning, secret scanning push protection from `repo-security.json`
   - Enables Dependabot vulnerability alerts
   - Enables the dependency graph
   - Enables Dependabot automated security fixes
   - Configures CodeQL default code scanning from `codeql-default-setup.json`
   - Applies branch protection rules to the target branch from `branch-protection.json`

   Usage:
   `apply-repo-policy.sh -o OWNER -r REPO [-b BRANCH] [-t TOKEN]`

   Options:

   - -o  GitHub org/user (owner)
   - -r  Repository name
   - -b  Branch to protect (default: repo default branch)
   - -t  Token (optional if GITHUB_TOKEN is set)
   - -h  Show help

   Note: you can set env variable **GITHUB_TOKEN** and skip it as an argument.

1. Update the link — `[docs/rfc](https://github.com/ORG/REPO/tree/main/docs/rfc)` — in `.github/ISSUE_TEMPLATE/design_rfc.yml`

1. Update the name of the package in `src/my_package/` and `docs/reference/my_package.md` and in `docs/reference/index.md`

1. Update `pyproject.toml` with the information of your package.

1. Adjust Ruff Settings in `pyproject.toml`

1. Remove this README.md

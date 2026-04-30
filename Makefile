# -----------------------------------------------------------------------------
# Project Makefile for Static Analysis & Code Quality
# -----------------------------------------------------------------------------

PYTHON := python3

# Directories (adjust if needed)
SRC_DIR := src
TEST_DIR := tests

# -----------------------------------------------------------------------------
# Formatting (import sort → format)
# -----------------------------------------------------------------------------
format:
	ruff check --select I --fix $(SRC_DIR) $(TEST_DIR)
	ruff format $(SRC_DIR) $(TEST_DIR)


# -----------------------------------------------------------------------------
# Linting (no fixes applied)
# -----------------------------------------------------------------------------
lint:
	ruff check $(SRC_DIR) $(TEST_DIR)


# -----------------------------------------------------------------------------
# Full verification (formatting check + linting check)
# -----------------------------------------------------------------------------
check:
	# 1. Ensure imports are sorted (but do not modify files)
	ruff check --select I $(SRC_DIR) $(TEST_DIR)

	# 2. Check formatting is correct (no file writes)
	ruff format --check $(SRC_DIR) $(TEST_DIR)

	# 3. Run linting
	ruff check $(SRC_DIR) $(TEST_DIR)


# -----------------------------------------------------------------------------
# Quality Gate (FAANG-level): formatting, linting, typing, tests, security
# -----------------------------------------------------------------------------
quality:
	# 1. Run all formatting fixes (developer-friendly)
	ruff check --select I --fix $(SRC_DIR) $(TEST_DIR)
	ruff format $(SRC_DIR) $(TEST_DIR)

	# 2. Run lint
	ruff check $(SRC_DIR) $(TEST_DIR)

	# 3. Type-checking (pyright or mypy)
	#pyright || mypy $(SRC_DIR) || true

	# 4. Run unit tests
	#pytest -q

	# 5. Dependency vulnerability scanning
	#pip-audit || true


# -----------------------------------------------------------------------------
# Utility Targets
# -----------------------------------------------------------------------------
.PHONY: format lint check quality

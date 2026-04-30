Thank you for considering contributing to this project. All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Tweet about it
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues


## Table of Contents

- [Project Scope](#project-scope)
- [Before You Start](#before-you-start)
- [Questions](#i-have-a-question)
- [Contribution](#i-want-to-contribute)
- [Bugs](#reporting-bugs)
- [Enhancements](#suggesting-enhancement)
- [Development Setup](#development-setup)
- [Branching and Workflow](#branching-and-workflow)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Testing and Quality](#testing-and-quality)
- [Documentation](#documentation)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Review Process](#review-process)
- [Security Issues](#security-issues)
- [Licensing](#licensing)
- [Getting Help](#getting-help)
- [Code of Conduct](#code-of-conduct)

---

## Project Scope

This repository focuses on:

- [INSERT 1–3 BULLETS DESCRIBING THE PROJECT’S PURPOSE]
- [INSERT WHAT IS IN SCOPE]
- [INSERT WHAT IS OUT OF SCOPE]

Contributions that align with the scope are more likely to be accepted.

---

## Before You Start

### Check existing work

Before opening a new issue or pull request:

1. Search existing issues and pull requests.
2. Read the project README and docs.
3. If proposing a large change, open a design discussion first (see below).

### Discuss larger changes first

For significant changes (architecture, major dependencies, breaking changes):

- Open an issue labeled `type:design` (or `RFC`) and include:
  - Problem statement
  - Goals and non-goals
  - Proposed approach and alternatives
  - Compatibility and migration plan
  - Test and rollout plan

Maintainers may request an approved design before implementation.
--->

---

## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation]().

Before you ask a question, it is best to search for existing [Issues](/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (nodejs, npm, etc), depending on what seems relevant.

We will then take care of the issue as soon as possible.

----

## I Want To Contribute

You can contribute by:

- Reporting bugs and regressions
- Proposing features or architectural improvements
- Improving documentation and examples
- Adding tests and increasing coverage
- Fixing issues labeled `good first issue` or `help wanted`
- Improving performance, observability, accessibility, or developer experience

> ### Legal Notice
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.

---

## Bugs

### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](issues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
- Stack trace (Traceback)
- OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
- Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
- Possibly your input and the output
- Can you reliably reproduce the issue? And can you also reproduce it with older versions?

### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to <>.
>
We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](/issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).


### Bug Triage

This sections explains how bug triaging is done for your project. Help beginners by including examples to good bug reports and providing them questions they should look to answer.

You can help report bugs by filing them here:

You can look through the existing bugs here:

You can help us diagnose and fix existing bugs by asking and providing answers for the following:

Is the bug reproducible as explained?
Is it reproducible in other environments (for instance, on different browsers or devices)?
Are the steps to reproduce the bug clear? If not, can you describe how you might reproduce it?
What tags should the bug have?
Is this bug something you have run into? Would you appreciate it being looked into faster?
You can close fixed bugs by testing old tickets to see if they are still happening.

You can update our changelog here:

You can remove duplicate bug reports by:
--->

---

## Enhancements

This section guides you through submitting an enhancement suggestion for CONTRIBUTING.md, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation]() carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- You may want to **include screenshots and animated GIFs** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
- **Explain why this enhancement would be useful** to most CONTRIBUTING.md users. You may also want to point out the other projects that solved it better and which could serve as inspiration.

---

## Development Setup

---
> Replace the commands below with your project’s actual tooling. If you support multiple options (e.g., `uv`, `poetry`, `pip`), document the preferred one first and list alternatives.

### Prerequisites

- [INSERT LANGUAGE VERSION, e.g., Python 3.12+ / Node 20+]
- [INSERT TOOLING, e.g., `uv` or `poetry`, `make`, `docker`, etc.]
- [OPTIONAL: DB / services required for local dev]

### Clone

```bash
git clone [YOUR_REPO_URL]
cd [REPO_DIR]
````

### Install dependencies

Option A (preferred):

```bash
# Example (Python/uv)
uv sync
```

Option B (alternative):

```bash
# Example (Python/poetry)
poetry install
```

### Configure environment

1. Copy example environment file:

   ```bash
   cp .env.example .env
   ```
2. Update values in `.env` as needed.

If your project uses secrets, do not commit them. Prefer `.env` files ignored by Git, a secret manager, or local environment variables.

### Run the project locally

```bash
# Example
make dev
# or
uv run python -m your_app
```

### Run tests locally

```bash
make test
# or
uv run pytest
```
--->
---

## Branching and Workflow

### Default workflow

1. Create a branch from the default branch (`main` or `master`).
2. Make small, focused commits.
3. Add tests for behavior changes.
4. Ensure formatting and linting pass.
5. Open a pull request and request review.

### Branch naming

Use descriptive branch names, for example:

* `feature/<short-description>`
* `fix/<short-description>`
* `docs/<short-description>`
* `chore/<short-description>`
* `refactor/<short-description>`

If you use an issue tracker, include the ticket key:

* `feature/PROJ-123-short-description`

---

## Commit Message Guidelines
---
Write clear, informative commit messages. Recommended formats:

### Conventional Commits (recommended)

* `feat: add X`
* `fix: correct Y`
* `docs: update Z`
* `refactor: reorganize A`
* `test: add coverage for B`
* `chore: update tooling`

For breaking changes:

* `feat!: change API for ...`
* Include a `BREAKING CHANGE:` footer describing impact and migration.

### General guidance

* Use imperative mood: “Add”, “Fix”, “Improve”
* Keep the subject line concise (ideally under ~72 characters)
* Explain “why” in the body when needed
--->

---

## Testing and Quality

### Testing expectations

* Add or update tests for any behavior change.
* Prefer unit tests for logic and integration tests for critical paths.
* Tests should be deterministic and not depend on external services unless explicitly designated as integration/e2e.

### Code quality checks

Before opening a PR, run:

```bash
make fmt
make lint
make test
```

If your repo uses specific tools, list them here, for example:

* Formatting: [BLACK/RUFF/PRETTIER/GOFMT/...]
* Linting: [RUFF/ESLINT/GOLANGCI-LINT/...]
* Type checking: [MYPY/PYRIGHT/TS/...]
* Security scanning: [BANDIT/SEMGREP/...]
* Tests: [PYTEST/JEST/GO TEST/...]
* Coverage: [COVERAGE.PY/NYC/...], minimum: [INSERT THRESHOLD]

### Performance considerations

If your change may impact performance:

* Provide a benchmark or before/after numbers
* Note changes in time/memory complexity where relevant
--->

---

## Documentation & ADR

Documentation is managed by [Material MkDocs](https://squidfunk.github.io/mkdocs-material/). All settings can
be found in `mkdocs.yml`. The documentation source files are located in the `docs/` folder. The documentation consists
of three main pillars:
* `README.md` as a entry gate.
* `docs/` for markdown in-depth guides (architecture, how-tos, general guides)
* Docstrings following [**Google Style Convention**](https://google.github.io/styleguide/pyguide.html).

**Expectations**
* Docstrings are mandatory for all public APIs (classes, methods, functions, modules).
* Provide examples (minimal and runnable) when applicable.
* Add module to the `/docs/reference/{MY-PACKAGE}` folder for every public module/package.
* Update `README.md` if user-facing behavior changes.
* Add or update markdown documents in `/docs` for every new or updated features, configuration, or APIs.

**How Documentation Build is Implemented**

Public Reference and Markdowns are built using Material MkDocs and mkdocstrings and published to
[INSERT LOCATION, E.G., `https://your-project-docs.com`].
Docstrings are checked using Ruff (`pyproject.toml`), validation rules from `mkdocs.yml`, and
pre-commit hooks of `codespell`. Markdown files are linted using `mdformat` and `codespell` (both in pre-commit hooks).

**Architecture Decisions Documentation**

We use Architecture Decision Records to keep the log of all structurally important decisions.
- ADRs live in-repo: `docs/architecture/adr/`
- File format: Markdown (`.md`). Reuse the template provided (`docs/architecture/adr/template.md`)
- Naming: `NNNN-kebab-case-title.md` (e.g., `0007-use-kafka-for-market-events.md`)
- One ADR per decision
- **ADRs are immutable**: modifications are not allowed (you may add UPDATE section when necessary) and are rather superseded by the new ADR
- Visualization is done through C4 model. All diagrams live in (`docs/architecture/diagrams/`)
Check this [guide](docs/architecture/adr/README.md) how to create ADRs.

---

## Submitting a Pull Request

### PR checklist (expected)

* [ ] PR is scoped and focused (avoid bundling unrelated changes)
* [ ] Linked issue or rationale is provided (e.g., “Fixes #123”)
* [ ] Tests added/updated and passing
* [ ] Lint/format/type checks passing
* [ ] Documentation updated (if needed)
* [ ] Backward compatibility considered; breaking changes clearly labeled
* [ ] Changelog entry added (if your project requires it)

### PR description guidance

Include:

1. Summary of the change
2. Motivation and context
3. How to test (commands and expected behavior)
4. Risk/impact assessment and rollout plan (if applicable)
5. Screenshots/logs (if UI/observability changes)
--->
---

## Review Process

Maintainers will review contributions for:

* Correctness and test coverage
* Alignment with project scope and design principles
* Maintainability (clarity, modularity, documentation)
* Backward compatibility and migration strategy
* Security and performance impact

You may be asked to revise your PR. Please keep discussions constructive and focused on the code and requirements.

### Response times

This is an open-source project; reviews may take time. If a PR is time-sensitive, note it explicitly in the PR description.
--->

---

## Security Issues

Do not report security vulnerabilities via public issues.

Instead:

* Email: [INSERT SECURITY CONTACT]
* Or follow: `SECURITY.md` (if present)

Include:

* Affected versions
* Reproduction steps
* Impact assessment
* Suggested mitigations (if any)
--->

---

## Licensing

By contributing, you agree that your contributions will be licensed under the project’s license.

* See: `LICENSE`

If your organization requires a CLA/DCO, add details here:

* CLA: [INSERT LINK/PROCESS]
* DCO sign-off: [INSERT PROCESS, e.g., `git commit -s`]
--->
---

## Getting Help
---
* Documentation: [INSERT LINK OR PATH, e.g., `docs/`]
* Issue tracker: [INSERT LINK]
* Discussions/Chat: [INSERT LINK, e.g., GitHub Discussions/Slack/Discord]
* Maintainers: [INSERT CONTACT OR TEAM]
--->
---

## Code of Conduct

This project follows a Code of Conduct. By participating, you are expected to uphold it.

- Read: `CODE_OF_CONDUCT.md` (or equivalent policy document)
- Report violations to: [INSERT CONTACT OR EMAIL]

Thank you for contributing.

# Contributing to OddSong

Thanks for your interest in improving OddSong! This guide explains how to report issues, propose changes, and submit pull requests.

All contributors are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to contribute

- **Report a bug** — open an [issue](https://github.com/Joe-Heffer-Shef/oddsong/issues) with steps to reproduce, expected behaviour, and what you saw instead. Include OS, Python/R version, and a minimal audio sample if relevant.
- **Suggest a feature** — open an issue describing the use case before writing code, so we can agree on scope.
- **Improve documentation** — fixes to the README, docstrings, or `docs/` are very welcome.
- **Submit code** — see below.

## Development setup

```bash
git clone https://github.com/Joe-Heffer-Shef/oddsong.git
cd oddsong
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

For the R implementation, see `R/README.md`.

## Making changes

1. **Create a branch** from `main`:
   ```bash
   git checkout -b short-descriptive-name
   ```
2. **Write tests** alongside any code change. Bug fixes should include a regression test.
3. **Run the test suite and linters** before pushing:
   ```bash
   pytest
   ruff check .
   ruff format --check .
   ```
4. **Keep commits focused.** One logical change per commit, with a clear message:
   ```
   Short summary in the imperative (max 72 chars)

   Optional longer explanation of *why* the change is needed.
   Reference issues with "Fixes #123" where appropriate.
   ```

## Pull requests

- Target the `main` branch.
- Fill in the PR description: what changed, why, and how you tested it.
- Keep PRs small and focused — easier to review, easier to merge.
- Update `README.md` or `docs/` if you change user-facing behaviour.
- CI must pass before review.

A maintainer will review and may request changes. Once approved, we'll squash-merge.

## Coding style

- **Python**: follow PEP 8; formatting and linting are enforced by `ruff`. Type hints are encouraged.
- **R**: follow the [tidyverse style guide](https://style.tidyverse.org/).
- Prefer clear names over comments. Comment the *why*, not the *what*.

## Reporting security issues

Please do **not** open a public issue for security vulnerabilities. Email the maintainer directly — see `pyproject.toml` or `git log` for contact.

## Licence

By contributing, you agree that your contributions will be licensed under the same terms as the project (see [LICENSE](LICENSE)).

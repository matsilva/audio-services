# Getting started

Welcome to the project! This guide will help you set up your development environment and get started quickly.

## 1. Setting Up the Environment

We use Poetry to manage dependencies and virtual environments. Follow these steps to get your environment ready:

1. **Install Poetry**:

   ```bash
   pipx install poetry
   ```

2. **Install portaudio on mac**: (this is needed for pyaudio to be installed)

   ```bash
   brew install portaudio
   ```

3. **Install Dependencies**:

   ```bash
   poetry install
   ```

4. **Activate the Virtual Environment**:
   Poetry automatically manages virtual environments. To activate it:
   ```bash
   poetry shell
   ```

## 2. Automated Testing with pytest

We use `pytest` for testing. Here’s how to run the tests:

1. **Run All Tests**:

   ```bash
   poetry run pytest
   ```

2. **Run Tests in a Specific File**:

   ```bash
   poetry run pytest tests/test_my_module.py
   ```

3. **Run a Specific Test Function**:
   ```bash
   poetry run pytest tests/test_my_module.py::test_my_function
   ```

## 3. Test Coverage

We use `pytest-cov` to measure test coverage. Here’s how to check it:

1. **Run Tests with Coverage**:
   ```bash
   poetry run pytest --cov=my_project tests/
   ```

## 4. Continuous Integration (CI)

We use CI pipelines to automatically run tests on every commit. Ensure your changes pass all tests before pushing to the repository.

## 5. Linting and Formatting

We use `flake8` for linting and `black` for formatting to maintain code quality and consistency.

1. **Check for Linting Errors**:

   ```bash
   poetry run flake8 my_project/
   ```

2. **Format the Code**:
   ```bash
   poetry run black my_project/
   ```

## 6. Development Workflow

### Write Tests First

Follow Test-Driven Development (TDD) practices by writing tests before implementing new features or fixing bugs.

### Run Tests Frequently

Use a test watcher like `pytest-watch` to automatically re-run tests when files change.

1. **Run pytest-watch**:
   ```bash
   poetry run ptw
   ```

### VSCode Setup

1. **Install Extensions**:

   - Python
   - pytest

2. **Configure Test Discovery**:
   Ensure VSCode is set to discover and run tests using `pytest`.

3. **Run and Debug Tests**:
   Use the test explorer in VSCode to run and debug tests directly from the IDE.

## Quick Reference for Makefile Commands

- Install dependencies: `make install`
- Activate the virtual environment: `make activate`
- Run all tests: `make test`
- Run tests in a specific file: `make test-file`
- Run a specific test function: `make test-function`
- Run tests with coverage: `make coverage`
- Check for linting errors: `make lint`
- Format the code: `make format`
- Watch for changes and re-run tests: `make watch`

## Summary

- **Environment Setup**: Use Poetry to manage dependencies and virtual environments.
- **Testing**: Use `pytest` for running tests and `pytest-cov` for coverage.
- **CI**: Ensure tests pass before pushing to the repository.
- **Linting and Formatting**: Use `flake8` for linting and `black` for formatting.
- **Development Workflow**: Write tests first, run tests frequently, and use IDE features.

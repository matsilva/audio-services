# Getting started

Welcome to the project! This guide will help you set up your development environment and get started quickly.

## 1. Setting Up the Environment

1. **Install deps**:

   ```bash
   make install
   ```

2. **Install portaudio and ffmpeg on mac**: (this is needed for pyaudio to be installed)

   ```bash
   brew install portaudio ffmpeg
   ```

## 2. Automated Testing with pytest

We use `pytest` for testing. Here’s how to run the tests:

1. **Run All Tests**:

   ```bash
   make test
   ```

This runs pytest under the hood

## Quick Reference for Makefile Commands

run `make help` to see all commands

- Install dependencies: `make install`
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

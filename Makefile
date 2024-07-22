# Makefile for managing project tasks

.PHONY: help install fix-lock activate test coverage lint format watch

help: ## Display this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

install: ## Install project dependencies using Poetry
	poetry install

fix-lock: ## Fix poetry lockfile
	poetry lock

activate: ## Activate Poetry's virtual environment
	poetry shell

test: ## Run all tests with pytest
	poetry run pytest

test-file: ## Run tests in a specific file
	@echo "Usage: make test-file FILE=tests/test_my_module.py"
	@read -p "Enter the test file path: " FILE && poetry run pytest $$FILE

test-function: ## Run a specific test function
	@echo "Usage: make test-function FILE=tests/test_my_module.py FUNCTION=test_my_function"
	@read -p "Enter the test file path: " FILE && read -p "Enter the test function name: " FUNCTION && poetry run pytest $$FILE::$$FUNCTION

coverage: ## Run tests with coverage
	poetry run pytest --cov=audio-services

lint: ## Check for linting errors with flake8
	poetry run flake8 

format: ## Format the code with black
	poetry run black 

watch: ## Automatically re-run tests when files change with pytest-watch
	poetry run ptw

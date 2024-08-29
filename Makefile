# Makefile for managing project tasks


# Define reusable logging functions
INFO_COLOR=\033[1;34m
SUCCESS_COLOR=\033[1;32m
NO_COLOR=\033[0m
HELP_COLOR=\033[1;36m

info = @echo "$(INFO_COLOR)[start] $(1)$(NO_COLOR)"
success = @echo "$(SUCCESS_COLOR)[done] $(1)$(NO_COLOR)"

.PHONY: help 
help: ## Display this help message
	@echo "$(HELP_COLOR)Usage: make [target]$(NO_COLOR)"
	@echo ""
	@echo "$(HELP_COLOR)Targets:$(NO_COLOR)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(HELP_COLOR)%-30s$(NO_COLOR) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(HELP_COLOR)Additional Targets:$(NO_COLOR)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' cmd/*/*.mk | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(HELP_COLOR)%-30s$(NO_COLOR) %s\n", $$1, $$2}'


FORCE:

.PHONY: install
install: ## Install project dependencies using pipx
	$(call info,Installing project dependencies using pipx...)
	pip install -r requirements.txt
	$(call success,Project dependencies installed.)

.PHONY: activate
activate: ## Activate the virtual environment
	$(call info,Activating virtual environment...)
	. venv/bin/activate
	$(call success,Virtual environment activated.)

.PHONY: build-clean
# Clean the dist and build directories
build-clean: ## Clean the dist and build folders
	$(call info,Cleaning dist and build folders...)
	rm -rf dist build *.spec
	$(call success,dist and build folders cleaned.)

.PHONY: cache-clean
# Remove all __pycache__ and .pytest_cache folders
cache-clean: build-clean ## Remove all __pycache__ and .pytest_cache folders
	$(call info,Removing __pycache__ and .pytest_cache folders...)
	find . -type d -name '__pycache__' -exec rm -rf {} + 
	find . -type d -name '.pytest_cache' -exec rm -rf {} +
	$(call success,__pycache__ and .pytest_cache folders removed.)

.PHONY: test
test: ## Run all tests with pytest
	$(call info,Running tests with pytest...)
	pytest
	$(call success,Tests completed.)

.PHONY: test-file
test-file: ## Run tests in a specific file
	$(call info,Running tests in a specific file...)
	@read -p "Enter the test file path: " FILE && pytest $$FILE
	$(call success,Tests in specific file completed.)

.PHONY: test-function
test-function: ## Run a specific test function
	$(call info,Running a specific test function...)
	@read -p "Enter the test file path: " FILE && read -p "Enter the test function name: " FUNCTION && pytest $$FILE::$$FUNCTION
	$(call success,Specific test function completed.)

.PHONY: test-coverage
coverage: ## Run tests with coverage
	$(call info,Running tests with coverage...)
	pytest --cov=audio-services
	$(call success,Coverage tests completed.)

.PHONY: lint
lint: ## Check for linting errors with flake8
	$(call info,Checking for linting errors with flake8...)
	flake8
	$(call success,Linting check completed.)

.PHONY: format
format: ## Format the code with black
	$(call info,Formatting code with black...)
	black .
	$(call success,Code formatting completed.)

.PHONY: watch
watch: ## Automatically re-run tests when files change with pytest-watch
	$(call info,Starting pytest-watch...)
	ptw
	$(call success,Pytest-watch running.)

include cmd/transcribe/transcribe.mk
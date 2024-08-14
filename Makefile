# Makefile for managing project tasks

.PHONY: help install fix-lock activate test test-transcribe coverage lint format watch build-docker-transcribe build-transcribe transcribe-spec

# Define reusable logging functions
INFO_COLOR=\033[1;34m
SUCCESS_COLOR=\033[1;32m
NO_COLOR=\033[0m
HELP_COLOR=\033[1;36m

info = @echo "$(INFO_COLOR)[start] $(1)$(NO_COLOR)"
success = @echo "$(SUCCESS_COLOR)[done] $(1)$(NO_COLOR)"

help: ## Display this help message
	@echo "$(HELP_COLOR)Usage: make [target]$(NO_COLOR)"
	@echo ""
	@echo "$(HELP_COLOR)Targets:$(NO_COLOR)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(HELP_COLOR)%-30s$(NO_COLOR) %s\n", $$1, $$2}'


install: ## Install project dependencies using Poetry
	$(call info,Installing project dependencies using Poetry...)
	poetry install --with transcribe
	$(call success,Project dependencies installed.)

fix-lock: ## Fix poetry lockfile
	$(call info,Fixing Poetry lockfile...)
	poetry lock
	$(call success,Poetry lockfile fixed.)

activate: ## Activate Poetry's virtual environment
	$(call info,Activating Poetry virtual environment...)
	poetry shell
	$(call success,Poetry virtual environment activated.)

test: ## Run all tests with pytest
	$(call info,Running tests with pytest...)
	poetry run pytest
	$(call success,Tests completed.)

test-transcribe: ## Run all tests with pytest
	$(call info,Running tests with pytest...)
	poetry run pytest libs/transcript_processor
	$(call success,Tests completed.)

test-file: ## Run tests in a specific file
	$(call info,Running tests in a specific file...)
	@read -p "Enter the test file path: " FILE && poetry run pytest $$FILE
	$(call success,Tests in specific file completed.)

test-function: ## Run a specific test function
	$(call info,Running a specific test function...)
	@read -p "Enter the test file path: " FILE && read -p "Enter the test function name: " FUNCTION && poetry run pytest $$FILE::$$FUNCTION
	$(call success,Specific test function completed.)

coverage: ## Run tests with coverage
	$(call info,Running tests with coverage...)
	poetry run pytest --cov=audio-services
	$(call success,Coverage tests completed.)

lint: ## Check for linting errors with flake8
	$(call info,Checking for linting errors with flake8...)
	poetry run flake8
	$(call success,Linting check completed.)

format: ## Format the code with black
	$(call info,Formatting code with black...)
	poetry run black .
	$(call success,Code formatting completed.)

watch: ## Automatically re-run tests when files change with pytest-watch
	$(call info,Starting pytest-watch...)
	poetry run ptw
	$(call success,Pytest-watch running.)

build-docker-transcribe:
	docker build -f cmd/transcribe/Dockerfile -t audio-services .

build-transcribe: transcribe-spec ## Build the transcribe CLI as a standalone binary
	$(call info,Building transcribe CLI as a standalone binary...)
	poetry run pyinstaller transcribe.spec
	$(call success,Transcribe CLI built successfully.)

archive-transcribe-artifacts: FORCE
	$(call info,Archiving transcribe CLI artifacts)
	tar -czvf transcribe.tar.gz dist/transcribe
	$(call success,Transcribe CLI artifacts archived successfully)

transcribe-spec: ## Create and build using a custom spec file
	$(call info,Creating transcribe.spec file...)
	poetry run pyinstaller --onefile --name=transcribe --hidden-import=libs --specpath . cmd/transcribe/transcribe.py
	$(call info,Modifying transcribe.spec file...)
	@sed -i '' 's/hiddenimports = \[\]/hiddenimports = \["libs"\]/' transcribe.spec
	@sed -i '' 's/datas=\[\]/datas=\[\("libs\/\*", "libs"\)\]/' transcribe.spec
	@sed -i '' 's/pathex=\[\]/pathex=\["."\]/' transcribe.spec
	$(call success,transcribe.spec file saved successfully.)

FORCE:
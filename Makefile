# Makefile for managing project tasks

.PHONY: help install activate test test-transcribe coverage lint format watch build-docker-transcribe build-transcribe transcribe-spec archive-transcribe-artifacts

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

install: ## Install project dependencies using pipx
	$(call info,Installing project dependencies using pipx...)
	pip install -r requirements.txt
	$(call success,Project dependencies installed.)

activate: ## Activate the virtual environment
	$(call info,Activating virtual environment...)
	. venv/bin/activate
	$(call success,Virtual environment activated.)

.PHONY: build-clean
# Clean the dist and build directories
build-clean: ## Clean the dist and build folders
	$(call info,Cleaning dist and build folders...)
	rm -rf dist build
	$(call success,dist and build folders cleaned.)

.PHONY: cache-clean
# Remove all __pycache__ and .pytest_cache folders
cache-clean: build-clean ## Remove all __pycache__ and .pytest_cache folders
	$(call info,Removing __pycache__ and .pytest_cache folders...)
	find . -type d -name '__pycache__' -exec rm -rf {} + 
	find . -type d -name '.pytest_cache' -exec rm -rf {} +
	$(call success,__pycache__ and .pytest_cache folders removed.)

test: ## Run all tests with pytest
	$(call info,Running tests with pytest...)
	pytest
	$(call success,Tests completed.)

test-transcribe: ## Run all transcribe-related tests with pytest
	$(call info,Running transcribe tests with pytest...)
	pytest libs/transcript_processor
	$(call success,Transcribe tests completed.)

test-file: ## Run tests in a specific file
	$(call info,Running tests in a specific file...)
	@read -p "Enter the test file path: " FILE && pytest $$FILE
	$(call success,Tests in specific file completed.)

test-function: ## Run a specific test function
	$(call info,Running a specific test function...)
	@read -p "Enter the test file path: " FILE && read -p "Enter the test function name: " FUNCTION && pytest $$FILE::$$FUNCTION
	$(call success,Specific test function completed.)

coverage: ## Run tests with coverage
	$(call info,Running tests with coverage...)
	pytest --cov=audio-services
	$(call success,Coverage tests completed.)

lint: ## Check for linting errors with flake8
	$(call info,Checking for linting errors with flake8...)
	flake8
	$(call success,Linting check completed.)

format: ## Format the code with black
	$(call info,Formatting code with black...)
	black .
	$(call success,Code formatting completed.)

watch: ## Automatically re-run tests when files change with pytest-watch
	$(call info,Starting pytest-watch...)
	ptw
	$(call success,Pytest-watch running.)

build-docker-transcribe: ## Build the transcribe Docker image
	$(call info,Building Docker image for transcribe CLI...)
	docker build -f cmd/transcribe/Dockerfile -t audio-services .
	$(call success,Transcribe Docker image built successfully.)

build-transcribe: transcribe-spec ## Build the transcribe CLI as a standalone binary
	$(call info,Building transcribe CLI as a standalone binary...)
	pyinstaller transcribe.spec
	$(call success,Transcribe CLI built successfully.)

archive-transcribe-artifacts: FORCE ## Archive transcribe CLI artifacts
	$(call info,Archiving transcribe CLI artifacts...)
	tar -czvf transcribe.tar.gz dist/transcribe
	$(call success,Transcribe CLI artifacts archived successfully.)

transcribe-spec: ## Create and build using a custom spec file
	$(call info,Creating transcribe.spec file...)
	pyinstaller --onefile --name=transcribe --hidden-import=libs --specpath . cmd/transcribe/transcribe.py
	$(call info,Modifying transcribe.spec file...)
	@sed -i '' 's/hiddenimports = \[\]/hiddenimports = \["libs"\]/' transcribe.spec
	@sed -i '' 's/datas=\[\]/datas=\[\("libs\/\*", "libs"\)\]/' transcribe.spec
	@sed -i '' 's/pathex=\[\]/pathex=\["."\]/' transcribe.spec
	$(call success,transcribe.spec file saved successfully.)

FORCE:
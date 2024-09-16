## This makefile is used for all transcribe related tasks

# Docker settings
DOCKER_IMAGE = transcribe-cli
DOCKER_RUN = docker run --rm -v ./:/src $(DOCKER_IMAGE)

.PHONY: test-transcribe
test-transcribe: ## Run all transcribe-related tests with pytest
	$(call info,Running transcribe tests with pytest...)
	$(VENV_PATH)/pytest libs/transcript_processor
	$(call success,Transcribe tests completed.)

.PHONY: test-transcribe-docker
test-transcribe-docker: ## Run test-transcribe in docker container
	$(DOCKER_RUN) test-transcribe


.PHONY: build-transcribe-image 
build-transcribe-image: ## Build the transcribe Docker image
	$(call info,Building Docker image for transcribe CLI...)
	docker build -f cmd/transcribe/Dockerfile -t $(DOCKER_IMAGE) .
	$(call success,Transcribe Docker image built successfully.)

.PHONY: build-transcribe
build-transcribe: transcribe-spec ## Build the transcribe CLI as a standalone binary
	$(call info,Building transcribe CLI as a standalone binary...)
	$(VENV_PATH)/pyinstaller transcribe.spec
	$(call success,Transcribe CLI built successfully.)

.PHONY: build-transcribe-docker
build-transcribe-docker: ## Runs build-transcribe within docker container
	$(DOCKER_RUN) build-transcribe

.PHONY: transcribe-spec
transcribe-spec: ## Create and build using a custom spec file
	$(call info,Creating and modifying transcribe.spec file...)
	$(VENV_PATH)/python3 ./cmd/transcribe/generate_spec.py
	$(call success,transcribe.spec file created and modified successfully.)

# TODO: move this to the mac recorder app because it requires specific signing
.PHONY: codesign-transcribe
codesign-transcribe: ## Codesigns the transcribe binary
	$(call info,codesigning transcribe binary...)
	codesign --deep --force --sign "Mathew Silva (Personal Team)" ./dist/transcribe
	$(call success,transcribe binary signed.)


.PHONY: lint-transcribe-docker
lint-transcribe-docker: ## Runs lint within docker container
	$(DOCKER_RUN) lint 

.PHONY: archive-transcribe-artifacts
archive-transcribe-artifacts: FORCE ## Archive transcribe CLI artifacts
	$(call info,Archiving transcribe CLI artifacts...)
	@mkdir -p dist
	@chmod 755 dist
	tar -czvf dist/transcribe.tar.gz -C dist transcribe
	$(call success,Transcribe CLI artifacts archived successfully.)

.PHONY: archive-transcribe-artifacts-docker
archive-transcribe-artifacts-docker: ## Runs archive-transcribe-artifacts target in a Docker container
	$(DOCKER_RUN) archive-transcribe-artifacts

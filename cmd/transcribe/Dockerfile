# Start base image

FROM python:3.12.4

ARG POETRY_VERSION=1.8.3

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=${POETRY_VERSION} \
    POETRY_HOME=/usr/local/bin \
    VENV_PATH=/venv

RUN addgroup --gid 10001 nonroot && \
    adduser --uid 10000 --system --home /home/nonroot nonroot && \
    usermod -g nonroot nonroot

RUN apt-get update && \
    apt-get install tini --no-install-recommends -y

RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv $VENV_PATH

# Start build steps
COPY pyproject.toml poetry.lock ./
# Poetry is installed with `pip`, so active our virtual environmentn and install projects dependecies there, so they don't conflict with poetry's dependencies.
RUN . $VENV_PATH/bin/activate && $POETRY_HOME/poetry lock
RUN . $VENV_PATH/bin/activate && $POETRY_HOME/poetry install --with transcribe 

WORKDIR /app
COPY . .

# Our user has an ID of 10000 and the group an ID of 10001.
RUN chown 10000:10001 -R /app

# Our non-root username.
USER nonroot

# # Lint the project using flake8
# RUN make lint

# # Run tests using pytest
# RUN make test

# # Build the transcribe CLI
# RUN make build-transcribe

# # Archive the transcribe binary
# RUN tar -czvf transcribe.tar.gz dist/transcribe

# Use ENTRYPOINT to pass arguments to the script
ENTRYPOINT ["make"]

CMD [ "help" ]

# Example usage: 
# $ docker run -it --rm audio-services --arg1 value1 --arg2 value2

# # Use an official Python runtime as a parent image
# FROM python:3.12.4 as builder

# # Set the working directory in the container
# WORKDIR /usr/src/app

# # Install system dependencies (if any)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

# # Copy the project files into the container
# COPY . .

# # Install Poetry for dependency management
# RUN pip install poetry==1.8.3

# # Install Python dependencies using Poetry
# RUN poetry install --without dev --no-root

# # Lint the project using flake8
# RUN make lint

# # Run tests using pytest
# RUN make test

# # Build the transcribe CLI
# RUN make build-transcribe

# # Archive the transcribe binary
# RUN tar -czvf transcribe.tar.gz dist/transcribe

# # Use ENTRYPOINT to pass arguments to the script
# ENTRYPOINT ["poetry", "run", "python", "cmd/transcribe/transcribe.py"]

# # Example usage: 
# # $ docker run -it --rm audio-services --arg1 value1 --arg2 value2
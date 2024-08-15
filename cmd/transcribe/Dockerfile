FROM python:3.12.4 as Builder

RUN apt-get update &&\
    apt-get install --no-install-suggests --no-install-recommends --yes pipx

ENV PATH="/root/.local/bin:${PATH}"

RUN pipx install poetry==1.8.3
RUN pipx inject poetry poetry-plugin-bundle

WORKDIR /src

COPY . .

# RUN poetry install --with transcribe --sync

RUN poetry bundle venv --only=transcribe /venv

# Use ENTRYPOINT to pass arguments to the script
ENTRYPOINT ["make"]

CMD [ "help" ]

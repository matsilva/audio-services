FROM python:3.12.4 as Builder

# Update package list and install necessary system packages
RUN apt-get update && apt-get install -y \
    gcc \
    ffmpeg \ 
    && apt-get clean

# Set the PATH for the virtual environment
ENV VENV_PATH="/src/venv"
ENV PATH="$VENV_PATH/bin:$PATH"

WORKDIR /src

COPY . .

# Install Python dependencies
RUN make install

# Use ENTRYPOINT to pass arguments to the script
ENTRYPOINT ["make"]

CMD ["make help"]
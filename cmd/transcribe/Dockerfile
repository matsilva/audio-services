FROM python:3.12.4 as Builder

# Update package list and install necessary system packages
RUN apt-get update && apt-get install -y \
    libportaudio2 \
    libportaudiocpp0 \
    portaudio19-dev \
    gcc \
    ffmpeg \ 
    && apt-get clean

ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /src

COPY . .

# Exclude pyobjc from the requirements as it's macOS-specific
RUN sed '/pyobjc/d' requirements.txt > requirements-no-mac.txt

# Install Python dependencies
RUN pip install -r requirements-no-mac.txt

# Use ENTRYPOINT to pass arguments to the script
ENTRYPOINT ["make"]

CMD ["help"]
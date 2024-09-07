# Getting started

**Prerequisites: Install portaudio and ffmpeg**

On Mac:

```bash
brew install portaudio ffmpeg
```

...TODO: Add Windows and Linux instructions.

## Quick Reference for Makefile Commands

run `make help` to see all commands

- Install dependencies: `make install`
- Run all tests: `make test`
- Run tests with coverage: `make coverage`
- Check for linting errors: `make lint`
- Format the code: `make format`
- Watch for changes and re-run tests: `make watch`

### CLI usage example

`./dist/transcribe -i path/to/audio.m4a -o path/to/transcription.json`

### TODOS:

- Support output to plain text (stripped of time stamps, etc, just text)
- Support output to csv

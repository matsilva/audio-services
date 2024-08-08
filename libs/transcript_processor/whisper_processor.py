import whisper
import ssl
from datetime import datetime, timedelta
from .transcript_segment import TranscriptSegment


class WhisperProcessor:
    def __init__(self, model_name="small"):
        # Bypass SSL certificate verification
        ssl._create_default_https_context = ssl._create_unverified_context

        # Load the model
        self.model = whisper.load_model(model_name)

    def load_and_prepare_audio(self, audio_path):
        # Load audio and pad/trim it to fit 30 seconds
        audio = whisper.load_audio(audio_path)
        audio = whisper.pad_or_trim(audio)
        return audio

    def get_mel_spectrogram(self, audio):
        # Make log-Mel spectrogram and move to the same device as the model
        mel = whisper.log_mel_spectrogram(audio).to(self.model.device)
        return mel

    def detect_language(self, mel):
        # Detect the spoken language
        _, probs = self.model.detect_language(mel)
        language = max(probs, key=probs.get)
        return language

    def decode_audio(self, mel):
        # Decode the audio
        options = whisper.DecodingOptions()
        result = whisper.decode(self.model, mel, options)
        return result.text

    def process_audio(self, audio_path, recording_start_time=datetime.now()):
        audio = self.load_and_prepare_audio(audio_path)
        mel = self.get_mel_spectrogram(audio)
        language = self.detect_language(mel)

        result = self.model.transcribe(audio_path)
        segments = []

        for segment in result["segments"]:
            start_time = recording_start_time + timedelta(
                seconds=segment["start"]
            )
            end_time = recording_start_time + timedelta(seconds=segment["end"])
            text = segment["text"]
            transcript_segment = TranscriptSegment(start_time, end_time, text)
            segments.append(transcript_segment)

        return language, segments


# Example usage
if __name__ == "__main__":
    audio_path = "path/to/your/audio/file.wav"
    recording_start_time = (
        datetime.now()
    )  # Replace with actual recording start time if available

    processor = WhisperProcessor(model_name="small")
    language, segments = processor.process_audio(
        audio_path, recording_start_time
    )

    print(f"Detected language: {language}")
    for segment in segments:
        print(segment)

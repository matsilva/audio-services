import whisper
import ssl

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

    def process_audio(self, audio_path):
        audio = self.load_and_prepare_audio(audio_path)
        mel = self.get_mel_spectrogram(audio)
        language = self.detect_language(mel)
        text = self.decode_audio(mel)
        return language, text


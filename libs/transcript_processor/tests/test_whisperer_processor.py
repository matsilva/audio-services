import unittest
import os
from transcript_processor.whisper_processor import WhisperProcessor

class TestWhisperProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = WhisperProcessor(model_name="small")
        test_dir = os.path.dirname(__file__)
        self.test_audio_file = os.path.join(test_dir, "audiotest.m4a")
        if not os.path.exists(self.test_audio_file):
            self.fail(f"Test audio file '{self.test_audio_file}' does not exist. Please ensure the file is available.")

    def test_load_and_prepare_audio(self):
        audio = self.processor.load_and_prepare_audio(self.test_audio_file)
        self.assertIsNotNone(audio)

    def test_get_mel_spectrogram(self):
        audio = self.processor.load_and_prepare_audio(self.test_audio_file)
        mel = self.processor.get_mel_spectrogram(audio)
        self.assertIsNotNone(mel)

    def test_detect_language(self):
        audio = self.processor.load_and_prepare_audio(self.test_audio_file)
        mel = self.processor.get_mel_spectrogram(audio)
        language = self.processor.detect_language(mel)
        self.assertIsInstance(language, str)

    def test_decode_audio(self):
        audio = self.processor.load_and_prepare_audio(self.test_audio_file)
        mel = self.processor.get_mel_spectrogram(audio)
        text = self.processor.decode_audio(mel)
        self.assertIsInstance(text, str)
        self.assertEqual(text, "Alright, I am testing out the audio here and seeing how well it can transcribe all of this for me.")

if __name__ == "__main__":
    unittest.main()

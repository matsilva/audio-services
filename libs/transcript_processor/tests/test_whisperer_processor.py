import unittest
import os
from datetime import datetime, timedelta
from transcript_processor.whisper_processor import WhisperProcessor
from transcript_processor.transcript_segment import TranscriptSegment

class TestWhisperProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = WhisperProcessor(model_name="small")
        self.audio_path = "test_audio.wav"  # Path to a test audio file
        self.recording_start_time = datetime(2024, 7, 22, 15, 30, 0)  # Example start time

    def test_transcript_segment(self):
        start_time = datetime(2024, 7, 22, 15, 30, 0)
        end_time = datetime(2024, 7, 22, 15, 30, 2)
        text = "Hello, this is a test recording."

        segment = TranscriptSegment(start_time, end_time, text)
        self.assertEqual(segment.start_time, start_time)
        self.assertEqual(segment.end_time, end_time)
        self.assertEqual(segment.text, text)
        self.assertEqual(segment.get_start_time(), "2024-07-22 15:30:00")
        self.assertEqual(segment.get_end_time(), "2024-07-22 15:30:02")
        self.assertEqual(str(segment), "[2024-07-22 15:30:00 - 2024-07-22 15:30:02]: Hello, this is a test recording.")

    def test_process_audio(self):
        # Assume that the Whisper model and the test audio file are correctly set up
        language, segments = self.processor.process_audio(self.audio_path, self.recording_start_time)

        # Check language detection
        self.assertEqual(language, "en")  # Assuming the language is English

        # Check transcript segments
        self.assertIsInstance(segments, list)
        self.assertGreater(len(segments), 0)

        for segment in segments:
            self.assertIsInstance(segment, TranscriptSegment)
            self.assertIsInstance(segment.start_time, datetime)
            self.assertIsInstance(segment.end_time, datetime)
            self.assertIsInstance(segment.text, str)

if __name__ == "__main__":
    unittest.main()
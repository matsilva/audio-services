import unittest
import tempfile
import os
from audio_recorder.apple_audio_recorder_mic import AppleSystemAudioRecorder

class TestAppleSystemAudioRecorder(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(suffix=".m4a", delete=False).name
        self.recorder = AppleSystemAudioRecorder(output_file=self.temp_file)

    def tearDown(self):
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    def test_setup(self):
        self.assertIsNotNone(self.recorder.session)
        self.assertIsNotNone(self.recorder.recorder)

    def test_start_recording(self):
        self.recorder.start_recording()
        self.assertTrue(self.recorder.recorder.isRecording())
        self.recorder.stop_recording()

    def test_stop_recording(self):
        self.recorder.start_recording()
        self.recorder.stop_recording()
        self.assertFalse(self.recorder.recorder.isRecording())

if __name__ == "__main__":
    unittest.main()

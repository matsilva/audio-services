import unittest
import tempfile
import os
from unittest.mock import patch, MagicMock
import pyaudio

from audio_recorder.audio_recorder import AudioRecorder


class TestAudioRecorder(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(suffix=".m4a", delete=False).name
        self.recorder = AudioRecorder(output_file=self.temp_file)

    def tearDown(self):
        if os.path.exists(self.temp_file):
            os.remove(self.temp_file)

    @patch.object(pyaudio.PyAudio, "open")
    def test_start_recording(self, mock_open):
        # Mock the PyAudio stream object
        mock_stream = MagicMock()
        mock_open.return_value = mock_stream

        # Start recording
        self.recorder.start_recording()

        # Verify stream open was called with correct parameters
        mock_open.assert_called_with(
            format=pyaudio.paInt16,
            channels=self.recorder.channels,
            rate=self.recorder.rate,
            input=True,
            frames_per_buffer=self.recorder.chunk,
        )

        # Verify recording thread is started
        self.assertTrue(self.recorder.recording)
        self.assertTrue(self.recorder.recording_thread.is_alive())

    @patch.object(pyaudio.PyAudio, "open")
    def test_stop_recording(self, mock_open):
        # Mock the PyAudio stream object
        mock_stream = MagicMock()
        mock_open.return_value = mock_stream

        # Start and then stop recording
        self.recorder.start_recording()
        self.recorder.stop_recording()

        # Verify recording has stopped
        self.assertFalse(self.recorder.recording)

        # Verify stream methods were called
        mock_stream.stop_stream.assert_called_once()
        mock_stream.close.assert_called_once()

        # Verify audio interface terminate was called
        self.recorder.audio_interface.terminate.assert_called_once()

    @patch.object(pyaudio.PyAudio, "open")
    @patch("wave.open")
    def test_save_audio(self, mock_wave_open, mock_open):
        # Mock the PyAudio stream object and wave file
        mock_stream = MagicMock()
        mock_open.return_value = mock_stream
        mock_wave = MagicMock()
        mock_wave_open.return_value = mock_wave

        # Start and then stop recording to trigger save_audio
        self.recorder.start_recording()
        self.recorder.stop_recording()

        # Verify wave open was called with correct parameters
        mock_wave_open.assert_called_with(self.recorder.output_file, "wb")
        mock_wave.setnchannels.assert_called_with(self.recorder.channels)
        mock_wave.setsampwidth.assert_called_with(self.recorder.audio_interface.get_sample_size(pyaudio.paInt16))
        mock_wave.setframerate.assert_called_with(self.recorder.rate)
        mock_wave.writeframes.assert_called_once()
        mock_wave.close.assert_called_once()

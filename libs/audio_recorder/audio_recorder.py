import pyaudio
import wave
import AVFoundation
import threading


class AudioRecorder:
    def __init__(
        self, output_file="output-mic.wav", channels=2, rate=44100, chunk=1024
    ):
        # todo: change this to a temp file path
        self.output_file = output_file
        self.channels = channels
        self.rate = rate
        self.chunk = chunk
        self.audio_interface = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.recording = False

    def start_recording(self):
        self.stream = self.audio_interface.open(
            format=pyaudio.paInt16,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk,
        )
        self.frames = []
        self.recording = True
        print("Recording...")

        def record():
            while self.recording:
                data = self.stream.read(self.chunk)
                self.frames.append(data)

        self.recording_thread = threading.Thread(target=record)
        self.recording_thread.start()

    def stop_recording(self):
        self.recording = False
        self.recording_thread.join()
        self.stream.stop_stream()
        self.stream.close()
        self.audio_interface.terminate()
        print("Recording finished.")
        self.save_audio()

    def save_audio(self):
        wf = wave.open(self.output_file, "wb")
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.audio_interface.get_sample_size(pyaudio.paInt16))
        wf.setframerate(self.rate)
        wf.writeframes(b"".join(self.frames))
        wf.close()

    def record_microphone(self):
        self.start_recording()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            self.stop_recording()

    def record_system_audio(self):
        # This method requires Soundflower
        # or similar software to reroute system audio
        print("Starting system audio recording...")
        self.start_recording()
        try:
            while True:
                pass
        except KeyboardInterrupt:
            self.stop_recording()


# //TODO: see if we can use this lib to combine microphone and system audio
# abstract to m_chip lib and use this dynamically if the system is m1
class AppleSystemAudioRecorder:
    def __init__(self, output_file="output-system.m4a"):
        # todo: change this to a temp file path as a default
        self.output_file = output_file
        self.setup()

    def setup(self):
        self.session = AVFoundation.AVAudioSession.sharedInstance()
        self.session.setCategory_error_(
            AVFoundation.AVAudioSessionCategoryRecord, None
        )
        self.session.setActive_error_(True, None)

        self.settings = {
            AVFoundation.AVFormatIDKey: AVFoundation.kAudioFormatMPEG4AAC,
            AVFoundation.AVSampleRateKey: 44100.0,
            AVFoundation.AVNumberOfChannelsKey: 2,
        }

        (
            recorder,
            err,
        ) = AVFoundation.AVAudioRecorder.alloc().initWithURL_settings_error_(
            AVFoundation.NSURL.fileURLWithPath_(self.output_file),
            self.settings,
            None,
        )
        if err:
            raise ValueError(err)

        self.recorder = recorder

    def start_recording(self):
        if self.recorder.prepareToRecord():
            self.recorder.record()
            print("Recording started...")

    def stop_recording(self):
        if self.recorder.isRecording():
            self.recorder.stop()
            print("Recording stopped.")

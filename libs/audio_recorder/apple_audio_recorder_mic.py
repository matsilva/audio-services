import AVFoundation
# //TODO: see if we can use this lib to combine microphone and system audio
# abstract to m_chip lib and use this dynamically if the system is m1
class AppleSystemAudioRecorder:
    def __init__(self, output_file="output-system.m4a"):
        # todo: change this to a temp file path as a default
        self.output_file = output_file
        self.setup()

    def setup(self):
        self.session = AVFoundation.AVAudioSession.sharedInstance()
        self.session.setCategory_error_(AVFoundation.AVAudioSessionCategoryRecord, None)
        self.session.setActive_error_(True, None)

        self.settings = {
            AVFoundation.AVFormatIDKey: AVFoundation.kAudioFormatMPEG4AAC,
            AVFoundation.AVSampleRateKey: 44100.0,
            AVFoundation.AVNumberOfChannelsKey: 2,
        }

        recorder, err = AVFoundation.AVAudioRecorder.alloc().initWithURL_settings_error_(
            AVFoundation.NSURL.fileURLWithPath_(self.output_file), self.settings, None
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
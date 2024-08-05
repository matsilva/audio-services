from libs.transcript_processor.whisper_processor import WhisperProcessor

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Process audio with Whisper.")
    parser.add_argument('-i', 'input', type=str, help="Path to the input audio file")
    parser.add_argument('-o', 'output', type=str, help="Desired path to transcription file")
    args = parser.parse_args()

    processor = WhisperProcessor(model_name="small")
    language, text = processor.process_audio(args.audio_path)
    print(f"Detected language: {language}")
    print(f"Recognized text: {text}")

if __name__ == "__main__":
    main()

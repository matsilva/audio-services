from libs.transcript_processor.transcript_file import TranscriptFile
from libs.transcript_processor.whisper_processor import WhisperProcessor


def main():
    import argparse

    parser = argparse.ArgumentParser(description="trancribe audio files")
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help="Path to the input audio file",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=True,
        help="Desired path to transcription file",
    )
    args = parser.parse_args()

    processor = WhisperProcessor(model_name="small")
    _, segments = processor.process_audio(args.input)
    writer = TranscriptFile(args.output)
    writer.write_segments_to_json(segments)


if __name__ == "__main__":
    main()

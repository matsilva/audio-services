import json


class TranscriptFile:
    def __init__(self, filePathWithName=str):
        self.filePath = filePathWithName

    def write_segments_to_json(self, segments: list):
        """
        Write the list of transcript segments to a JSON file at the specified file path.

        Parameters
        ----------
        segments: list
            The list of transcript segments to write to the JSON file.
        """
        try:
            # Convert each segment to a dictionary
            segments_dict = [
                segment.to_dict() if hasattr(segment, "to_dict") else segment
                for segment in segments
            ]
            with open(self.filePath, "w", encoding="utf-8") as json_file:
                json.dump(
                    segments_dict, json_file, ensure_ascii=False, indent=4
                )
            print(f"Successfully wrote segments to {self.filePath}")
        except Exception as e:
            print(f"Failed to write segments to {self.filePath}: {e}")


# Example usage
if __name__ == "__main__":
    transcript = TranscriptFile("transcript.json")
    segments = [
        {"start": 0.0, "end": 5.0, "text": "Hello, world!"},
        {"start": 5.1, "end": 10.0, "text": "This is a test transcript."},
    ]
    transcript.write_segments_to_json(segments)

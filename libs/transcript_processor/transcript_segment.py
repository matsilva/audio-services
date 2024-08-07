from datetime import datetime, timedelta

class TranscriptSegment:
    def __init__(self, start_time: datetime, end_time: datetime, text: str):
        self.start_time = start_time
        self.end_time = end_time
        self.text = text

    def get_start_time(self, format='%Y-%m-%d %H:%M:%S'):
        return self.start_time.strftime(format)

    def get_end_time(self, format='%Y-%m-%d %H:%M:%S'):
        return self.end_time.strftime(format)

    def to_dict(self):
        return {
            "start_time": self.get_start_time(),
            "end_time": self.get_end_time(),
            "text": self.text
        }

    def __str__(self):
        return f"[{self.get_start_time()} - {self.get_end_time()}]: {self.text}"

# Example usage
if __name__ == "__main__":
    # Sample start and end times
    recording_start_time = datetime.now()
    segment_start = recording_start_time + timedelta(seconds=0)
    segment_end = recording_start_time + timedelta(seconds=2)
    
    # Create a TranscriptSegment instance
    segment = TranscriptSegment(segment_start, segment_end, "Hello, this is a test recording.")
    
    # Print segment in default format
    print(segment)
    
    # Print segment in custom format
    print(f"[{segment.get_start_time('%H:%M:%S')} - {segment.get_end_time('%H:%M:%S')}]: {segment.text}")
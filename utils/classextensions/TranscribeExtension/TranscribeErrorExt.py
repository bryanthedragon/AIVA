class TranscribeError(Exception):
    """Custom exception for transcribing audio file-related errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def Transcribe_the_audio(filename, content):
        try:
            with open(filename, 'w') as file:
                    file.write(content)
        except FileNotFoundError:
            raise TranscribeError(f"Error: The audio file '{filename}' does not exist.")
        except PermissionError:
            raise TranscribeError(f"Error: Permission denied when trying to TranscribeE to '{filename}'. .AudioFile")
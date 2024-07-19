class DetectError(Exception):
    """Custom exception for detection errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
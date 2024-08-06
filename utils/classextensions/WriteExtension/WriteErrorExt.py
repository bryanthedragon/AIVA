class Writerror(Exception):
    """Custom exception for write file-related errors."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def write_to_file(filename, content):
        try:
            with open(filename, 'w') as file:
                file.write(content)
        except FileNotFoundError:
            raise Writerror(f"Error: The file '{filename}' does not exist.")
        except PermissionError:
            raise Writerror(f"Error: Permission denied when trying to write to '{filename}'.")
        except IOError as e:
            raise Writerror(f"Error: An I/O error occurred: {e}")

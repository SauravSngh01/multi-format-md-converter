from abc import ABC, abstractmethod

class BaseConverter(ABC):
    """
    Abstract base class for all file converters.
    Requires implementation of a `convert` method that returns Markdown-formatted text.
    """

    def __init__(self, file_path: str):
        self.file_path: str = file_path

    @abstractmethod
    def convert(self) -> str:
        """
        Convert the input file to a Markdown-formatted string.
        Must be implemented by subclasses.
        """
        pass

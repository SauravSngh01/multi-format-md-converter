from pathlib import Path

def get_extension(file_path: str) -> str:
    """
    Extracts and returns the lowercase file extension from a given file path.

    Args:
        file_path (str): The path to the input file.

    Returns:
        str: Lowercase file extension (e.g., '.pdf'), or empty string if none.
    """
    return Path(file_path.strip()).suffix.lower()

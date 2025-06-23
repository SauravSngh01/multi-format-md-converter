from .base_converter import BaseConverter

class TXTConverter(BaseConverter):
    """
    Converter for plain text (.txt) files to Markdown.
    """

    def convert(self) -> str:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                return content + "\n"  # Ensure single newline at end
        except Exception as e:
            return f"**Error reading TXT file:** {e}\n"

from docx import Document
from .base_converter import BaseConverter

class DOCXConverter(BaseConverter):
    def convert(self) -> str:
        doc = Document(self.file_path)
        markdown = ""

        for para in doc.paragraphs:
            style_name = para.style.name.lower()

            if "heading" in style_name:
                # Safely extract heading level
                try:
                    level = int(''.join(filter(str.isdigit, style_name))) or 1
                    markdown += f"{'#' * level} {para.text.strip()}\n\n"
                except ValueError:
                    markdown += f"# {para.text.strip()}\n\n"
            elif para.text.strip():
                markdown += f"{para.text.strip()}\n\n"

        return markdown

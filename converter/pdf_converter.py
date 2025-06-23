import pdfplumber
from .base_converter import BaseConverter

class PDFConverter(BaseConverter):
    def convert(self) -> str:
        """
        Extracts text from each page of the PDF and converts it into a Markdown-compatible string.
        """
        markdown = ""

        try:
            with pdfplumber.open(self.file_path) as pdf:
                for i, page in enumerate(pdf.pages, start=1):
                    text = page.extract_text()
                    if text:
                        markdown += f"## Page {i}\n\n{text.strip()}\n\n"
                    else:
                        markdown += f"## Page {i}\n\n_(No extractable text on this page)_\n\n"
        except Exception as e:
            markdown = f"**Error reading PDF file:** {e}\n"

        return markdown

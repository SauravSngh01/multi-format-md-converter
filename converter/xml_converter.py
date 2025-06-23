import xml.etree.ElementTree as ET
from .base_converter import BaseConverter

class XMLConverter(BaseConverter):
    """
    Converts XML files into structured Markdown format using nested headings.
    """

    def convert(self) -> str:
        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()

            def recurse(element, depth=0) -> str:
                markdown = f"{'#' * (depth + 1)} {element.tag}"

                # Append attributes if any
                if element.attrib:
                    attr_str = ' '.join(f'{k}=\"{v}\"' for k, v in element.attrib.items())
                    markdown += f" ({attr_str})"

                markdown += "\n"

                # Append text content
                if element.text and element.text.strip():
                    markdown += f"{element.text.strip()}\n"

                markdown += "\n"

                # Recurse through child elements
                for child in element:
                    markdown += recurse(child, depth + 1)

                return markdown

            return recurse(root).strip() + "\n"

        except Exception as e:
            return f"**Error parsing XML file:** {e}\n"

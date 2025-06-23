import json
from .base_converter import BaseConverter

class JSONConverter(BaseConverter):
    def convert(self) -> str:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        def format_json(data, indent=0):
            md = ""
            prefix = "  " * indent

            if isinstance(data, dict):
                for key, value in data.items():
                    md += f"{prefix}- **{key}**:"
                    if isinstance(value, (dict, list)):
                        md += "\n" + format_json(value, indent + 1)
                    else:
                        md += f" {value}\n"

            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, (dict, list)):
                        md += f"{prefix}-\n" + format_json(item, indent + 1)
                    else:
                        md += f"{prefix}- {item}\n"

            else:
                md += f"{prefix}{data}\n"

            return md

        return format_json(data)

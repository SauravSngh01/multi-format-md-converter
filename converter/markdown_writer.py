from pathlib import Path
from typing import Optional

def save_markdown(md_content: str, original_path: str, output_dir: Optional[str] = None) -> Path:
    """
    Save the given Markdown content to a `.md` file.

    Args:
        md_content (str): The Markdown-formatted text.
        original_path (str): Original input file path to derive the output name.
        output_dir (str, optional): Directory to save the .md file. Defaults to input file's directory.

    Returns:
        Path: The full path to the saved Markdown file.
    """
    base = Path(original_path).stem
    output_dir = Path(output_dir or Path(original_path).parent)
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / f"{base}.md"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content.rstrip() + "\n")

    # Optional: print(f"✅ Markdown file saved: {output_file}")
    return output_file

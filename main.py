import os
from utils.file_detector import get_extension
from utils.logger import logger
from converter import (
    pdf_converter,
    docx_converter,
    xml_converter,
    json_converter,
    txt_converter,
    markdown_writer
)

SUPPORTED_EXTENSIONS = {
    ".pdf": pdf_converter.PDFConverter,
    ".docx": docx_converter.DOCXConverter,
    ".xml": xml_converter.XMLConverter,
    ".json": json_converter.JSONConverter,
    ".txt": txt_converter.TXTConverter,
}

def convert_to_markdown(file_path: str, output_dir: str = None):
    logger.info(f"📄 Input file: {file_path}")

    if not os.path.isfile(file_path):
        logger.error(f"❌ File does not exist: {file_path}")
        return

    ext = get_extension(file_path)
    logger.info(f"📦 Detected file extension: {ext}")

    if ext not in SUPPORTED_EXTENSIONS:
        logger.warning(f"⚠️ Unsupported file type: {ext}")
        return

    try:
        converter_class = SUPPORTED_EXTENSIONS[ext]
        logger.info(f"🔧 Using converter: {converter_class.__name__}")
        converter = converter_class(file_path)
        md_content = converter.convert()

        if not md_content.strip():
            logger.warning("⚠️ Converted content is empty. Skipping file save.")
            return

        output_file = markdown_writer.save_markdown(md_content, file_path, output_dir)
        logger.info(f"✅ Saved Markdown to: {output_file}")
    except Exception as e:
        logger.exception(f"❌ Failed to convert {file_path}: {e}")

if __name__ == "__main__":
    input_dir = "examples/"
    output_dir = "converted/"

    print(f"🔁 Starting batch conversion in: {input_dir}")

    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        if os.path.isfile(file_path):
            convert_to_markdown(file_path, output_dir=output_dir)

    print("✅ All supported files have been processed.")


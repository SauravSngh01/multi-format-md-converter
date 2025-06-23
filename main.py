from utils.file_detector import get_extension
from utils.logger import logger
from converter import pdf_converter, docx_converter, xml_converter, json_converter, txt_converter, markdown_writer
import os

def convert_to_markdown(file_path: str, output_dir: str = None):
    logger.info(f"📄 Input file: {file_path}")

    if not os.path.isfile(file_path):
        logger.error(f"❌ File does not exist: {file_path}")
        return

    ext = get_extension(file_path)
    logger.info(f"📦 Detected file extension: {ext}")

    converters = {
        ".pdf": pdf_converter.PDFConverter,
        ".docx": docx_converter.DOCXConverter,
        ".xml": xml_converter.XMLConverter,
        ".json": json_converter.JSONConverter,
        ".txt": txt_converter.TXTConverter,
    }

    if ext not in converters:
        logger.error(f"❌ Unsupported file format: {ext}")
        return

    try:
        logger.info(f"🔧 Using converter: {converters[ext].__name__}")
        converter = converters[ext](file_path)
        md_content = converter.convert()
        
        if not md_content.strip():
            logger.warning("⚠️ Converted content is empty. Skipping file save.")
            return

        output_file = markdown_writer.save_markdown(md_content, file_path, output_dir)
        logger.info(f"✅ Successfully converted and saved to: {output_file}")
    except Exception as e:
        logger.exception(f"❌ Conversion failed: {e}")

if __name__ == "__main__":
    file_path = "examples/sample.docx"
    output_dir = "converted/"

    print(f"🔁 Starting Markdown conversion for: {file_path}")
    convert_to_markdown(file_path, output_dir=output_dir)
    print("✅ Conversion process complete.")

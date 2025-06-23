# 📝 Multi-format File to Markdown Converter

This Python module allows you to convert input files in various formats—**PDF, DOCX, XML, JSON, and TXT**—into clean, structured **Markdown (.md)** files.

---

## 🚀 Features

- 📄 Auto-detects file type based on extension
- 🔄 Converts to Markdown with headings, lists, code blocks, etc.
- 🧱 Modular architecture
- 🧪 Unit-testable structure with `unittest`
- 🪵 Built-in logging and error handling
- ✅ Follows PEP8 standards

---

## 📦 Supported Formats

| Input Format | Output Format | Required Library       |
|--------------|----------------|-------------------------|
| `.pdf`       | `.md`          | `pdfplumber`            |
| `.docx`      | `.md`          | `python-docx`           |
| `.xml`       | `.md`          | `lxml` or `xml.etree`   |
| `.json`      | `.md`          | Python standard lib     |
| `.txt`       | `.md`          | Python standard lib     |

---

## 📁 Project Structure

multi_format_to_md/
│
├── converter/
│   ├── __init__.py
│   ├── base_converter.py
│   ├── pdf_converter.py
│   ├── docx_converter.py
│   ├── xml_converter.py
│   ├── json_converter.py
│   ├── txt_converter.py
│   └── markdown_writer.py
│
├── utils/
│   ├── __init__.py
│   ├── file_detector.py
│   └── logger.py
│
├── tests/
│   ├── test_pdf.py
│   ├── test_docx.py
│   ├── test_xml.py
│   ├── test_json.py
│   ├── test_txt.py
│   └── test_output_format.py
│
├── examples/
│   ├── sample.pdf
│   ├── sample.docx
│   ├── sample.xml
│   ├── sample.json
│   └── sample.txt
│
├── requirements.txt
├── README.md
└── main.py

## Requirements Installation
   pip install -r requirements.txt
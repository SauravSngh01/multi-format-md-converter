# 📝 Multi-format File to Markdown Converter

A Python module that accepts input files in various formats—**PDF, DOCX, XML, JSON, and TXT**—and converts their content into clean, structured **Markdown (.md)** format.

---

## 🚀 Features

- 📄 Auto-detects file type based on extension
- 🔄 Converts to Markdown using headings, lists, code blocks, etc.
- 🧱 Modular and extensible architecture
- 🧪 Includes unit tests using `unittest`
- 🪵 Built-in logging and error handling
- ✅ Follows Python's PEP8 style guide

---

## 📦 Supported Formats

| Input Format | Output Format | Required Library       |
|--------------|----------------|-------------------------|
| `.pdf`       | `.md`          | `pdfplumber`            |
| `.docx`      | `.md`          | `python-docx`           |
| `.xml`       | `.md`          | `lxml` or `xml.etree`   |
| `.json`      | `.md`          | Python standard library |
| `.txt`       | `.md`          | Python standard library |

---

## 📁 Project Structure
multi_format_to_md/
│
├── converter/
│ ├── init.py
│ ├── base_converter.py
│ ├── pdf_converter.py
│ ├── docx_converter.py
│ ├── xml_converter.py
│ ├── json_converter.py
│ ├── txt_converter.py
│ └── markdown_writer.py
│
├── utils/
│ ├── init.py
│ ├── file_detector.py
│ └── logger.py
│
├── tests/
│ ├── test_pdf.py
│ ├── test_docx.py
│ ├── test_xml.py
│ ├── test_json.py
│ ├── test_txt.py
│ └── test_output_format.py
│
├── examples/
│ ├── sample.pdf
│ ├── sample.docx
│ ├── sample.xml
│ ├── sample.json
│ └── sample.txt
│
├── requirements.txt
├── README.md
└── main.py

⚙️ Installation
1. Clone the Repository
  git clone https://github.com/SauravSngh01/multi-format-md-converter.git
  cd multi-format-md-converter

2. Install the Required Libraries
  pip install -r requirements.txt
This installs: pdfplumber – ( for PDF parsing ) , python-docx – ( for DOCX parsing ) , lxml – ( for XML parsing )

🧪 Running Tests
Run all unit tests using:
  python -m unittest discover tests
  
🔄 Command Line Usage
You can also run the converter directly from the command line:
  python main.py
This runs the default file specified in main.py.

To convert other files, update the path in main.py:
if __name__ == "__main__":
    convert_to_markdown("examples/sample.pdf", output_dir="converted/")

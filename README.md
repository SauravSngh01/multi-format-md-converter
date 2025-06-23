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
│   ├── __init__.py
│   ├── base_converter.py       # Abstract base class
│   ├── pdf_converter.py        # PDF to Markdown logic
│   ├── docx_converter.py       # DOCX to Markdown logic
│   ├── xml_converter.py        # XML to Markdown logic
│   ├── json_converter.py       # JSON to Markdown logic
│   ├── txt_converter.py        # TXT to Markdown logic
│   └── markdown_writer.py      # Writes .md output files
│
├── utils/
│   ├── __init__.py
│   ├── file_detector.py        # Detect file extension
│   └── logger.py               # Logging setup
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
├── requirements.txt            # Includes pdfplumber, python-docx, lxml, etc.
├── README.md                   # Instructions, usage examples
└── main.py                     # Batch converter script


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

Running main file 
write the run command in terminal 
python main.py

To convert other files, update the path in main.py:
if __name__ == "__main__":
    convert_to_markdown("examples/sample.pdf", output_dir="converted/")

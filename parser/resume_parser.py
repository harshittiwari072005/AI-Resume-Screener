import PyPDF2
import docx2txt
import os

def parse_pdf(file_path):
    text = ""

    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "

    return text.strip()


def parse_docx(file_path):
    return docx2txt.process(file_path).strip()


def parse_resume(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return parse_pdf(file_path)
    elif ext == ".docx":
        return parse_docx(file_path)
    else:
        raise ValueError("Unsupported file format")

import pdfplumber
from docx import Document

def extract_text(file):
    if file.name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            return "\n".join(page.extract_text() or "" for page in pdf.pages)
    elif file.name.endswith(".docx"):
        return "\n".join(p.text for p in Document(file).paragraphs)
    return ""
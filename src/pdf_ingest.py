import pdfplumber

def extract_text(pdf_path):
    pages_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for p in pdf.pages:
            text = p.extract_text() or ""
            pages_text.append(text)
    return pages_text

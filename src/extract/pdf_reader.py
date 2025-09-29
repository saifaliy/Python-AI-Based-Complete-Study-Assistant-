import pdfplumber
import numpy as np

print("PDFPlumber and NumPy working ✅")

def extract_text_from_pdf(pdf_path: str) -> str:
    all_text = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                all_text.append(text)

    # join all text and normalize using NumPy
    text_data = "\n".join(all_text)
    lines = np.array(text_data.splitlines())
    cleaned = "\n".join(lines[lines != ""])  # remove empty lines

    return cleaned       

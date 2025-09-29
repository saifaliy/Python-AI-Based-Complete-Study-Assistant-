import sys
import os
sys.path.append(os.path.abspath('.')) 

from src.extract.pdf_reader import extract_text_from_pdf
from src.summarize.langchain_summarizer import summarize_text

text = extract_text_from_pdf("data/System Design Interview An Insider’s Guide (Alex Xu) (Z-Library).pdf")
summary = summarize_text(text[:3000])  # truncate to avoid token overflow
print("\n=== Summary ===\n")
print(summary)

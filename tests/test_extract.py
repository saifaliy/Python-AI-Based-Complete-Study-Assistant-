import sys
import os
sys.path.append(os.path.abspath('.')) 

from src.extract.pdf_reader import extract_text_from_pdf

text = extract_text_from_pdf("data/System Design Interview An Insider’s Guide (Alex Xu) (Z-Library).pdf")  # make sure you place a sample PDF here
print(text[:1000])  # Print first 1000 characters

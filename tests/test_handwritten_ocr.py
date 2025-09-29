import sys
import os
sys.path.append(os.path.abspath('.')) 

from src.extract.ocr_reader import extract_text_from_image

text = extract_text_from_image("data/handwritten_sample.jpg")
print("OCR Output:\n", text)

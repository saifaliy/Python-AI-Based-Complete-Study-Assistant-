import easyocr

reader = easyocr.Reader(['en'])

def extract_text_from_image(image_path: str) -> str:
    result = reader.readtext(image_path, detail=0)
    return "\n".join(result)

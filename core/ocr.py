import pytesseract
from PIL import Image

def ocr(image_path):
    # Open the image file
    image = Image.open(image_path)

    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(image)

    # Return the extracted text
    return text



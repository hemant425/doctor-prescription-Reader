import pytesseract
from PIL import Image
import os

# 1) Tell pytesseract where Tesseract is installed on your PC:
#    — adjust this path to match where your .exe actually lives
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\heman\OneDrive\Documents\Python projects\Mini project-5 sem\Jarvis\project trail 1\finalproject8\tesseract.exe"

def extract_text_from_image(image_path):
    # 2) (Optional) If you need to tell Tesseract where its language-data lives:
    # os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"
    
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

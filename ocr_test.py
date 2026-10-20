import pytesseract
from PIL import Image

# Tell Python where the Tesseract program lives
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Open the screenshot
image = Image.open("test.png")

# Read the text out of the picture
text = pytesseract.image_to_string(image)

print(text)
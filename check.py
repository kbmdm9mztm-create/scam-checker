import pytesseract
from PIL import Image
from scam_rules import analyze

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open("test.png")
text = pytesseract.image_to_string(image)

result = analyze(text)

print("Text found:")
print(text)
print("Verdict:", result["verdict"], "(score " + str(result["score"]) + ")")
for r in result["reasons"]:
    print("-", r["name"] + ":", r["why"])
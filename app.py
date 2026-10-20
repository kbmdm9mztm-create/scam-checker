
from flask import Flask, render_template, request
from PIL import Image, UnidentifiedImageError
import pytesseract
from scam_rules import analyze
from io import BytesIO

app = Flask(__name__)

# Maximum upload size: 5 MB
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

# Update this path if Tesseract is installed elsewhere
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    extracted_text = None
    error = None

    if request.method == "POST":
        file = request.files.get("screenshot")

        if not file or file.filename == "":
            error = "Please choose a screenshot first."
        else:
            try:
                image_data = file.read()

                if not image_data:
                    raise ValueError("The uploaded file is empty.")

                image = Image.open(BytesIO(image_data))
                image.verify()

                # Reopen after verify, then extract the text
                image = Image.open(BytesIO(image_data))
                image = image.convert("RGB")
                extracted_text = pytesseract.image_to_string(image).strip()

                if not extracted_text:
                    error = "No readable text found. Try a clearer screenshot."
                else:
                    result = analyze(extracted_text)

            except (UnidentifiedImageError, OSError, ValueError):
                error = "That file could not be read as an image. Try PNG or JPG."

    return render_template(
        "index.html",
        result=result,
        extracted_text=extracted_text,
        error=error,
    )


@app.errorhandler(413)
def file_too_large(error):
    return "File too large. Please upload an image under 5 MB.", 413


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=False)
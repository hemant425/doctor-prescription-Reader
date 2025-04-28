from flask import Flask, render_template, request
from ocr_reader import extract_text_from_image
from llm_simplifier import simplify_prescription
from allergy_detector import detect_allergy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'prescription' not in request.files:
        return "No file uploaded."

    file = request.files['prescription']
    file.save('static/uploaded.jpg')  # Save uploaded file

    # Step 1: OCR
    raw_text = extract_text_from_image('static/uploaded.jpg')

    # Step 2: Simplify Text
    simplified_text = simplify_prescription(raw_text)

    # Step 3: Detect Allergy (optional for future, not needed for speaking)
    allergy_warning = detect_allergy(raw_text)

    # You must pass both texts if you want to show warnings too
    return render_template('result.html', simplified_text=simplified_text, allergy_warning=allergy_warning)

if __name__ == "__main__":
    app.run(debug=True)

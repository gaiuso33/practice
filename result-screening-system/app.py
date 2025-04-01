from flask import Flask, render_template, request, redirect, url_for, jsonify
from docx import Document
import pdfplumber
import os
import sys
import subprocess
app = Flask(__name__)
#get the absolute path of the src directory
SRC_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
#check for uploads directory
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def extract_text(file_path):
    """Extracts text from PDF or DOCX files."""
    if file_path.endswith('.pdf'):
        with pdfplumber.open(file_path) as pdf:
            return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    return "Unsupported file format"
#train the model
def train_model():
    print("Training the model...")
    process = subprocess.run([sys.executable, os.path.join(SRC_DIR, 'train_model.py')], capture_output=True, text=True)
    if process.returncode != 0:
        print("Error: Training failed.", process.stderr)
        return False
    return True
#rank candidates
def rank_candidates():
    print("Ranking candidates...")
    process = subprocess.run([sys.executable, os.path.join(SRC_DIR, 'rank_candidates.py')], capture_output=True, text=True)
    if process.returncode != 0:
        print("Error: Ranking failed.", process.stderr)
        return False
    return True
@app.route('/')
def upload_page():
    return render_template('upload_resume.html')
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'resume' not in request.files:
        return "No file part"
    file = request.files['resume']
    if file.filename == '':
        return "No selected file"
     # Validate file extension
    allowed_extensions = {'.pdf', '.docx'}
    file_ext = os.path.splitext(file.filename)[1].lower()

    if file_ext not in allowed_extensions:
        return "Invalid file type. Only PDF and DOCX files are allowed."

    # Save the uploaded file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    print(f"✅ File saved to: {filepath}")  # Debug log

     # Extract text from resume
    resume_text = extract_text(filepath)
    print(f"📄 Extracted Text (First 500 chars): {resume_text[:500]}")  # Print preview of extracted text

    return f"File {file.filename} uploaded and processed successfully!"

@app.route('/screen', methods=['GET'])
def screen_resumes():
    """Allows screener to access all uploaded resumes and process them."""
    resume_texts = {}
    
    # List all files in the uploads folder
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        text = extract_text(file_path)
        resume_texts[filename] = text[:500]  # Preview of extracted text

    return jsonify(resume_texts)
@app.route('/train', methods=['POST'])
def train():
    if train_model():
        return "Model training completed successfully!"
    return "Model training failed!", 500
@app.route('/rank', methods=['POST'])
def rank():
    if rank_candidates():
        return "Candidate ranking completed successfully!"
    return "Candidate ranking failed!", 500
if __name__ == '__main__':
    app.run(debug=True)

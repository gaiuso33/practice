from flask import Flask, render_template, request

app = Flask(__name__)

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
    
    # Save the uploaded file
    file.save(f"uploads/{file.filename}")
    return f"File {file.filename} uploaded successfully!"

if __name__ == "__main__":
    app.run(debug=True)

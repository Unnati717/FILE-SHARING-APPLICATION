import os
from create_qr import create_qr
from flask import Flask, render_template, request
import shutil

app = Flask(__name__) # Initialize Flask app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qr', methods=['POST'])
def qr():    
    if request.method == 'POST':
        folder = 'static/uploads/user'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

        for file in request.files.getlist("file[]"):
            file.save(os.path.join('static', 'uploads', 'user', file.filename))
        urls = create_qr()
    return render_template('qr.html', urls=urls)

app.run(debug=True)
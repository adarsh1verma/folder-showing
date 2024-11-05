from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


FOLDER_PATH = 'Practical File'




@app.route('/')
def index():
    # Get list of files in the folder
    files = os.listdir(FOLDER_PATH)
    return render_template('index.html', files=files)

@app.route('/contributor')
def contributor():
    return render_template('contributors.html')

@app.route('/files/<filename>')
def download_file(filename):
    # Serve files for download or display
    return send_from_directory(FOLDER_PATH, filename)

if __name__ == '__main__':
    app.run(debug=True)

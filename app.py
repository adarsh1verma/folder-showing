from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)

# Root directory to display
FOLDER_PATH = 'Practical File'


def get_files_structure(folder_path):
    """
    Recursively retrieve folder structure to display files and folders.
    """
    structure = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isdir(item_path):
            # Recursively get the subfolder structure
            structure.append({
                'name': item,
                'type': 'folder',
                'content': get_files_structure(item_path)
            })
        else:
            # Append file information
            structure.append({
                'name': item,
                'type': 'file'
            })
    return structure


@app.route('/')
def index():
    # Pass the folder structure to the template
    files_structure = get_files_structure(FOLDER_PATH)
    return render_template('index.html', files_structure=files_structure)


@app.route('/files/<path:filename>')
def download_file(filename):
    # Serve files for download or display
    try:
        return send_from_directory(FOLDER_PATH, filename)
    except FileNotFoundError:
        abort(404)


@app.route('/contributor')
def contributor():
    return render_template('contributors.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request, render_template
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




@app.route('/upload', methods=['POST'])
def upload_file():
  
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400  # Return 400 Bad Request status


    folder_name = request.form.get('folder_name', 'default_folder')
    target_folder = os.path.join(app.config['UPLOAD_FOLDER'], folder_name)
    
    print(target_folder)
    print(folder_name)

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    else:
        # Remove folder and create new one
        os.rmdir(target_folder)
        os.makedirs(target_folder)

    file.save(os.path.join(target_folder, file.filename))

    return ({'Result': 'File uploaded successfully!'}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

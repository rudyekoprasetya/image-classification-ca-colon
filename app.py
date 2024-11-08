from flask import Flask, render_template, request
from markupsafe import escape
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

upload_folder = os.path.join('static','uploads')

app.config['UPLOAD'] = upload_folder

# fungsi hapus gambar di folder uploads
def delete_files_in_directory(directory_path):
   try:
     with os.scandir(directory_path) as entries:
       for entry in entries:
         if entry.is_file():
            os.unlink(entry.path)
     print("All files deleted successfully.")
   except OSError:
     print("Error occurred while deleting files.")


# index
@app.route("/", methods=['GET','POST'])
def home():
	if request.method == 'POST':
		# hapus file lama
		delete_files_in_directory(app.config['UPLOAD'])
		# upload file baru
		file = request.files['img']
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD'], filename))
		img = os.path.join(app.config['UPLOAD'], filename)
		return render_template('home.html', img=img)
	else:
		file = os.path.join('static/images', 'no-image.jpg')
		return render_template('home.html', img=file)
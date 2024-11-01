from flask import Flask, render_template, request
from markupsafe import escape
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

upload_folder = os.path.join('static','uploads')

app.config['UPLOAD'] = upload_folder

# index
@app.route("/", methods=['GET','POST'])
def home():
	if request.method == 'POST':
		file = request.files['img']
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD'], filename))
		img = os.path.join(app.config['UPLOAD'], filename)
		return render_template('home.html', img=img)
	else:
		file = os.path.join('static/images', 'no-image.jpg')
		return render_template('home.html', img=file)
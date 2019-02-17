from flask import Flask, redirect, request, url_for, session, flash, render_template, make_response
import face_recognition

import os
from os import listdir
from os.path import isfile, join
import sys
from werkzeug.utils import secure_filename
import urllib3


app = Flask(__name__, template_folder='templates') #Initializes the app with templates as the HTML folder

app.config['UPLOAD_FOLDER'] = '/static/faces'
app.config['SECRET_KEY'] = "deve" #Encryption key
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 #This is essential for allowing the images to be refreshed in the management page, it sets the expirery for the browser cache to 0



ALLOWED_EXT = ['jpg', 'jpeg', 'png'] #List of filetypes allowed to be served to the server
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #Disables a very annoying warning when starting flask



'''
allowed_file()
returns a boolean if the file extension of the filename provided is in the ALLOWED_EXT list
'''
def allowed_file(filename):
	return '.' in filename and \
	filename.rsplit('.', 1)[1].lower() in ALLOWED_EXT


@app.route('/',methods=['GET','POST'])
def index():
	try:
		os.remove('static/faces/you.jpg')
	except:
		pass
	if request.method == 'POST':
		print("Here!",file=sys.stderr)
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files['file']
		rating = compareFaces(file)
		#print(rating,file=sys.stderr)
		return redirect(url_for('result')+'?result='+str(rating))
	return render_template("index.html") #renders the index.html template
	#return 'Goes somewhere'



@app.route('/howmuchikedannydevitoareyou', methods=['GET'])
def result():
	if request.args is not None:
		results = request.args.get('res')
		return render_template("result.html", results = results)
	return "Bad routing"





def stripPostData(base64):
	return str(base64)[str(base64).find(','):] #Removes added post data before comma of base64 image encoding


def saveFile(file):
	try:
		os.makedirs('static/faces') #tries to make the listed directories
	except:
		pass
	path = os.path.abspath('static/faces')#Gets absoulute path of service
	#file = open(path+'/you.jpg','wb')
	print(file,file=sys.stderr)
	#img = base64.b64decode(stripPostData(base64))#Decodes string data to base64
	file.save(os.path.join(app.config['UPLOAD_FOLDER'],'you.jpg'))

def compareFaces(you):
	#saveFile(you)
	#saveFile(them)
	try:
		os.makedirs('static/faces')
	except:
		pass
	path = os.path.abspath('static/faces')
	you.save(os.path.join(path,'you.jpg'))
	pretty_image = face_recognition.load_image_file('static/faces/you.jpg')
	them_image = face_recognition.load_image_file('static/faces/them.jpg')
	you_encoding = face_recognition.face_encodings(pretty_image)[0]
	them_encoding = face_recognition.face_encodings(them_image)[0]
	return  int(100 - (face_recognition.face_distance([you_encoding],them_encoding).tolist()[0]*100))



if __name__ == "__main":
	app.run(host=='0.0.0.0',ssl_context='adhoc')

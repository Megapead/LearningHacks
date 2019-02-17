from flask import Flask, redirect, request, url_for, session, flash, render_template, make_response
import face_recognition

import os
from os import listdir
from os.path import isfile, join
import sys
from werkzeug.utils import secure_filename
import urllib3


app = Flask(__name__, template_folder='templates') #Initializes the app with templates as the HTML folder


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
	if request.method is 'POST'
        you = request.form['you']
        them = request.form['them']
		rating = compareFaces(you,them)
        return redirect(url_for('result')+'?res='+rating)
	return render_template("index.html") #renders the index.html template



@app.route('/howmuchikedannydevitoareyou', methods=['GET'])
def result():
    if request.args not None:
        results = request.args.get('res')
        return render_template("results.html")
    return "Bad routing"





def stripPostData(base64):
    return str(base64)[str(base64).find(','):] #Removes added post data before comma of base64 image encoding


def saveFile(base64,filename):
    try:
        os.makedirs('static/faces') #tries to make the listed directories
    path = os.path.abspath('static/faces')#Gets absoulute path of service
    file = open(path+'/'+filename+'.jpg','wb')
    img = base64.b64decode(stripPostData(base64))#Decodes string data to base64
    file.write(img)

def compareFaces(you,them):
    saveFile(you)
    saveFile(them)
    try:
        pretty_image = face_recognition.load_image_file('static/faces/you.jpg')
        them_image = face_recognition.load_image_file('static/faces/them.jpg')
        you_encoding = face_recognition.face_encodings(pretty_image)[0]
        them_encoding = face_recognition.face_encodings(them_image)[0]
        return face_recognition.face_distance(you_encoding,them_encoding)
    except:
        return -1

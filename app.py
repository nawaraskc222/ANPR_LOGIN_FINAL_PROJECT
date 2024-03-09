from flask import Flask, render_template, request, redirect
from deeplearning import OCR
import os 

app = Flask(__name__)

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH,'static/upload/')

# Dummy user data (replace this with your actual user authentication logic)
users = {
    'nawaras': 'root',
    'bibek': 'root',
    'manish': 'root'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print('username is 1: ' + username)
        if username in users and users[username] == password:
            # Here you can perform any additional logic like setting up sessions, cookies, etc.
            return render_template('index.html')
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')
    

@app.route('/extract',methods=['POST','GET'])
def extract():
    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        path_save = os.path.join(UPLOAD_PATH,filename)
        upload_file.save(path_save)
        text = OCR(path_save,filename)

        return render_template('index.html',upload=True,upload_image=filename,text=text)

    return render_template('index.html',upload=False)


@app.route('/extractpage')
def extractpage():
    
    return render_template('index.html')  

if __name__ == '__main__':
    app.run(debug=True)

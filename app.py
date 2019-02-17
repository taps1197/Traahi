#This is the main.py of our project 

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def RunApp():
    return render_template("index.html")

@app.route('/videochat')
def VideoChat():
    return render_template("videochat.html",title='Video Chat platform')
@app.route('/doctor')
def Doctor():
    return render_template("doctor.html")
@app.route('/patient')
def Patient():
	return render_template("patient.html",title="Patients")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

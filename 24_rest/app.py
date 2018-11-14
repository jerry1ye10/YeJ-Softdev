#Jerry Ye
#SoftDev1 pd7
#K24 - A RESTful Journey Skyward
#2018-11-13
from flask import Flask, render_template  #imports class Flask
import urllib.request
import json
app = Flask(__name__)#Creates an instance of Flask

@app.route('/')#Defines index
def hello_world():
    f =  urllib.request.urlopen('https://api.nasa.gov/planetary/apod?api_key=KZA7h2LSwdHWgjPm5eQSFcO5QhFBJcWnGe8fJYoj')
    d = f.read()#Reads f and stores Json inside d
    data = json.loads(d)
    return render_template("template.html", pic = data['url'], explanation = data['explanation'])

if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()

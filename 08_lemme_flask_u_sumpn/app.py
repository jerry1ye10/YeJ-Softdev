#Jerry Ye
#SoftDev1 pd7
#K08 -- Fill Yer Flask
#2018-09-20
from flask import Flask #imports class Flask
app = Flask(__name__)#Creates an instance of Flask

@app.route('/')#Defines index
def hello_world():
    return "Hello world!"

@app.route('/awesome')#Defines 2nd route
def hello_awesome():
    return "Hello awesome!"

@app.route('/amazing')#Defines 3rd route
def hello_amazing():
    return "Hello Amazing!"

if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()

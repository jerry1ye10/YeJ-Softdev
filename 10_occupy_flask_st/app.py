#Jerry Ye and Ryan Aday: Team Bob
#SoftDev1 pd07
#K10 -- Jinja Tuning
#2018-09-24
from flask import Flask, render_template#imports class Flask
from occupations_data import main
app = Flask(__name__)#Creates an instance of Flask

@app.route('/')#Defines index
def index():
    return "This site will show occupations!"

@app.route('/occupations')#Defines occupations route
def show_occupations():
    randomOccupation,occupationsData, h1, h2 = main()
    return render_template("occupations.html",randomOccupation = randomOccupation, occupationsData = occupationsData,h1 = h1,h2= h2)

if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()

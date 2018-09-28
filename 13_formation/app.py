from flask import Flask, render_template, request #imports class Flask
app = Flask(__name__)#Creates an instance of Flask

@app.route('/')#Defines index
def hello_world():
    return render_template("template.html")

@app.route('/auth')
def test():
    args = request.args['username']
    greeting = "Hello friend!"
    return render_template("auth.html", method = request.method, username = args, greeting = greeting)

if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()

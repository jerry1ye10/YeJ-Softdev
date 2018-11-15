#Jerry Ye
#SoftDev1 pd7
#K25 - Getting More REST
#2018-11-14
from flask import Flask, render_template  #imports class Flask
import urllib.request
import json
import ssl

app = Flask(__name__)#Creates an instance of Flask

@app.route('/')#Defines index
def hello_world():
    context = ssl._create_unverified_context()
    API_KEY = "cdae74df30d0c8150058689d2e9e6e3a"
    url = 'https://developers.zomato.com/api/v2.1/restaurant?res_id=10'
    q = urllib.request.Request(url)
    q.add_header("user-key",API_KEY)
    q.add_header('User-Agent','Mozilla/5.0')
    f =  urllib.request.urlopen(q,context=context)
    d = f.read()#Reads f and stores Json inside d
    data = json.loads(d)
    print(data)
    return render_template("template.html", name=data['name'], location=data['location']['address'])

if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()

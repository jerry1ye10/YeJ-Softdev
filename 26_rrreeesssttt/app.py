#Jerry Ye
#SoftDev1 pd7
#K26 - Getting More REST
#2018-11-15
from flask import Flask, render_template  #imports class Flask

import urllib.request
import json
import ssl

app = Flask(__name__)#Creates an instance of Flask

@app.route('/')#Defines index
def hello_world():
    context = ssl._create_unverified_context()
    #API_KEY = "cdae74df30d0c8150058689d2e9e6e3a" -- None required
    url1 = 'https://swapi.co/api/planets/1/'
    q1 = urllib.request.Request(url1)
    #q.add_header("user-key",API_KEY) -- No API Key
    q1.add_header('User-Agent','Mozilla/5.0')
    f1 =  urllib.request.urlopen(q1,context=context)
    d1 = f1.read()#Reads f and stores Json inside d
    data1 = json.loads(d1)
    url2 = 'http://universities.hipolabs.com/search?name=middle&country=turkey'
    q2 = urllib.request.Request(url2)
    #q.add_header("user-key",API_KEY) -- No API Key
    q2.add_header('User-Agent','Mozilla/5.0')
    f2 =  urllib.request.urlopen(q2,context=context)
    d2 = f2.read()#Reads f and stores Json inside d
    data2 = json.loads(d2)
    data2 = data2[0] #Takes the first dictionary inside the list
    url3 = 'https://www.boredapi.com/api/activity'
    q3 = urllib.request.Request(url3)
    #q.add_header("user-key",API_KEY) -- No API Key
    q3.add_header('User-Agent','Mozilla/5.0')
    f3 =  urllib.request.urlopen(q3,context=context)
    d3 = f3.read()#Reads f and stores Json inside d
    data3 = json.loads(d3)
    return render_template("template.html", name=data1['name'], gravity=data1['gravity'], activity=data3['activity'], price=data3['price'],collegeName = data2['name'], site=data2['web_pages'][0] )

if (__name__) == "__main__":#if this file is run directly then the Flask app will run
    app.debug = True#allows changes to directly affect local host without rerunning app
    app.run()

#website brain
from flask import Flask, request

#object made (app) that represents our website that tell this is the main file
app = Flask(__name__)

#establishing routes using decorators
"""
1. routes must be uniue
2. routes name must be readable
3. routes must always return something
"""
@app.route("/")
def home():
    return 'Hello user! This is my first flask app.'

@app.route("/about")
def about(): 
    return 'This is our about page.' 

@app.route("/contact")
def contact():
    return 'This is our contact page.'

"""
HTTP Methods:
when the browser interacts with the website
1. GET: only seeks information without giving any input (to get data) (only for reading)
2. POST: provides some input (to send data) (only for writing)
part of web communication tools
*DON'T SEND ANY SENSITIVE / PVT DATA FROM GET as GET puts data in the url
while POST keeps it hidden in the request body
-always defines methods explicitly (method=[" "]) as flask only allows get by default
-request.method: checks which method is used by the user to make this request
*
"""
@app.route("/submit", method=["GET", "POST"])
def submit():
    if request.method == "POST": #import request
        return 'You sent data!'
    else:
        return 'You are just viewing data.'


#TERMINAL: flask run


#!/usr/bin/python3

from flask import Flask

## Flask constructor takes the name of current
## module (__name__) as argument
app = Flask(__name__)

## route() function of the Flask class is a 
## decorator, tells the application which URL
## should call the associated function
@app.route("/")
def hello_world():
    return "Hello World\n"

@app.route("/christian")
def christian():
    return "Go UNC\n"

@app.route("/hello/<name>")
def hello_name(name):
    name1 = name.rstrip('l')
    return f"Hello {name1:20}\n"

if __name__ == "__main__":
    app.run(port=5006)    ## runs the application
##    app.run(port=5006, debug=True)  ## DEBUG MODE


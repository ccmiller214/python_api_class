#!/usr/bin/python3

from flask import Flask
from flask import url_for
from flask import redirect

## Flask constructor takes the name of current
## module (__name__) as argument
app = Flask(__name__)

## route() function of the Flask class is a 
## decorator, tells the application which URL
## should call the associated function
@app.route("/admin")
def hello_admin():
    return "Hello Admin\n"

@app.route("/guest/<guest>")
def hello_guest(guest):
    return f"Hello \n {guest} as Guest\n"

@app.route("/user/<name>")
def hello_user(name):
    if name == "admin":
        return redirect(url_for("hello_admin"))
    else:
        return redirect(url_for("hello_guest",guest=name))
                
if __name__ == "__main__":
    app.run(port=5006)    ## runs the application
##    app.run(port=5006, debug=True)  ## DEBUG MODE


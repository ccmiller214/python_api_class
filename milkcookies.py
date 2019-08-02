#!/usr/bin/python3

from flask import Flask, make_response, request, render_template
import time

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/setcookie",methods = ["POST","GET"])
def setcookie():
    try:
        if request.method == "POST":
            user = request.form['nm']
            date = request.form['dt']
            resp = make_response(render_template("readcookie.html"))
                      #cookievar  #value
            resp.set_cookie("userID", user)
            resp.set_cookie("date",date)
            return resp
        else:
            return redirect(url_for("index"))
    except:
        return redirect(url_for("index"))


@app.route("/getcookie")
def getcookie():
    try:
        if "userID" in request.cookies:
            name = request.cookies.get("userID")
            date = request.cookies.get("date")
            return "<h1>Looks like your UserName is ... " + name + "\nYou entered date: " + date + "\n</h1>"
        else: 
            return redirect(url_for("index"))
    except:
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(port=5006)



#!/usr/bin/python3

from flask import Flask, session, render_template, redirect, url_for, escape, request

app = Flask(__name__)
app.secret_key = "any random string the longer the better"

@app.route("/")
def index():
    if "username" in session:
        username = session["username"]

        if 'attempts' in session:
            session['attempts'] += 1
            if session['attempts'] > 4:
                session.pop("username",None)
                return redirect(url_for("index"))
        else: session['attempts'] = 1 

        return "You are logged in as " + username + "<br><a href = '/logout'></br>" + " Click Here to Log Out</b></a>"

    return "You are not logged in <br><a href = '/login'></br>" + "Click Here to Log In</b></a>"

@app.route("/login", methods = ["POST","GET"])
def login():
    if request.method == "POST":
        session["username"] = request.form.get("username")
        return redirect(url_for("index"))

    return """
    <form action = "" method = "POST">
        <p><input type = text name = username></p>
        <p><input type = submit value = Login></p>
    </form>
    """

@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("attempts", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(port=5006)

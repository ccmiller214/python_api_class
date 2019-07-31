#!/usr/bin/python3

from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)

path = "/home/student/pyapi/files"
@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/uploader", methods = ["GET","POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["file"]
        f.save(secure_filename(f.filename))
        with open(f.filename,'r') as readfile:
            contents = readfile.read()
            contents = contents.replace('student','XXXXXXXXX')
        with open(f.filename,'w') as updatefile:
             updatefile.write(contents)
#            updatefile.write('\nThis file has been modified\nby Christian Miller')
        return "file uploaded successfully"

if __name__ == "__main__":
    app.run(port=5006)

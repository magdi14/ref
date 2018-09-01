import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/refaie")
def birthday():
    now = datetime.datetime.now()
    birthday = now.month == 9 and now.day == 2
    #birthday = True
    return render_template("birthday.html", birthday=birthday)

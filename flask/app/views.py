from app import app
from flask import render_template

@app.route("/")
def hello():
    return "<h1>Hello From Flask!</h1>"

@app.route("/movie")
def home():
    return render_template("home.html")
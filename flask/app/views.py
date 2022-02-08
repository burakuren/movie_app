from crypt import methods
from datetime import date
from app import app
import flask
from flask import render_template,request

@app.route("/")
def hello():
    response = flask.Response("<h1>Hello From Flask!</h1>")
    response.headers["Server"] = "WebServer"
    return response

@app.route("/movie")
def home():
    response = flask.Response(render_template("home.html"))
    response.headers["Server"] = "WebServer"
    return response

@app.route("/emosea")
def emosea():
    return "<h1>AL EMO AĞLADIN AM</h1>"


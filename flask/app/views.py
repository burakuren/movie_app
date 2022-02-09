from crypt import methods
from datetime import date
from app import app
import flask
from flask import render_template,request,send_file,make_response

@app.route("/")
def home():
    response = flask.Response("<h1>Hello From Flask!</h1>")
    response.headers["Server"] = "WebServer"
    return response

@app.route("/movie")
def movie():
    response = flask.Response(render_template("movie.html"))
    response.headers["Server"] = "WebServer"
    return response

@app.route("/static/gonca.jpg")
def gonca_jpeg():
    response = flask.make_response(send_file("static/gonca.jpg",mimetype='image/jpeg'))
    response.headers["Server"] = "WebServer"
    return response

@app.route("/emosea")
def emosea():
    response = flask.make_response(render_template("emosea.html"))
    response.headers["Server"] = "WebServer"
    return response




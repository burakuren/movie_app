import flask
from flask import render_template,request,send_file,make_response,Blueprint

views = Blueprint("views",__name__)

@views.route("/")
def home():
    response = flask.Response("<h1>Hello From Flask!</h1>")
    response.headers["Server"] = "WebServer"
    return response

@views.route("/movie")
def movie():
    response = flask.Response(render_template("movie.html"))
    response.headers["Server"] = "WebServer"
    return response

@views.route("/static/gonca.jpg")
def gonca_jpeg():
    response = flask.make_response(send_file("static/gonca.jpg",mimetype='image/jpeg'))
    response.headers["Server"] = "WebServer"
    return response

@views.route("/emosea")
def emosea():
    response = flask.make_response(render_template("emosea.html"))
    response.headers["Server"] = "WebServer"
    return response


@views.route("/static/shakira.png")
def shakira_png():
    response = flask.make_response(send_file("static/shakira.png",mimetype='image/png'))
    response.headers["Server"] = "WebServer"
    return response


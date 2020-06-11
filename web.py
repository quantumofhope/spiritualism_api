#!/usr/bin/env python3
"""
Documentation

See also https://www.python-boilerplate.com/flask
"""
from flask import Flask, jsonify, render_template
from flask_cors import CORS
from logzero import logger
from blueprints.modulo1 import modulo1_blueprint
from blueprints.modulo2 import modulo2_blueprint
from blueprints.campaign import campaign_blueprint
from blueprints.urbanExtents import urbanExtents_blueprint
from blueprints.mapper import mapper_blueprint


app=Flask(__name__)


@app.route('/')
@app.route('/<name>')
def welcome(name=None):
    return render_template('welcome.html', name=name)

@app.route('/api/<username>')
def show_user_profile(username):
    # show the user profile for that user
    resp = f'User = {username}'
    return resp

@app.route('/about')
def about():
  return "What about this then!!"

@app.route("/helloworld")
def hello_world():
    logger.info("/")
    return "Hello World"

@app.route("/foo/<someId>")
def foo_url_arg(someId):
    logger.info("/foo/%s", someId)
    return jsonify({"echo": someId})

app.register_blueprint(modulo1_blueprint)
app.register_blueprint(modulo2_blueprint)
app.register_blueprint(campaign_blueprint)
app.register_blueprint(urbanExtents_blueprint)
app.register_blueprint(mapper_blueprint)

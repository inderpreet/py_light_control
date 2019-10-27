"""
@brief  FlaskWeb module to create a REST API as well as a simple dashboard
"""
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
api = Api(app)
socketio.init_app(app, cors_allowed_origins='*')

import FlaskWeb.views
import FlaskWeb.rest_ends
import FlaskWeb.socket_io



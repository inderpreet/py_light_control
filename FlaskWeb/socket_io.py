"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from flask_restful import Resource, Api
from FlaskWeb import app, socketio
from flask_socketio import SocketIO, send
from FlaskWeb.views import sensor_states


@socketio.on('message')
def handleMessage(msg):
    global sensor_states
    print('Message: ' + msg)
    # broadcast
    if sensor_states['light1']:
        resp = 'Light is ON'
    else:
        resp = 'Light is OFF'

    send(resp, broadcast=True)



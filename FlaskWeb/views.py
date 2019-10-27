"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from flask_restful import Resource, Api
from FlaskWeb import app, socketio
import html
from flask_socketio import SocketIO, send


# from FlaskWeb.socket_io import update_user_page

# using a dictionary and no history
sensor_states = {}
sensor_states['light1'] = False
sensor_states['light2'] = False


def update_user_page():
    global sensor_states
    # broadcast
    if sensor_states['light1']:
        resp = 'Light 1 is ON'
    else:
        resp = 'Light 1 is OFF'

    resp += html.unescape(' | ')

    if sensor_states['light2']:
        resp += 'Light 2 is ON'
    else:
        resp += 'Light 2 is OFF'
    socketio.send(resp, boardcast=True)


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


"""
REST End Points for sensor data coming from WI-FI Nodes
"""


@app.route('/api/rest/set/light/<a_id>/<value>', methods=["GET"])
def set_light(a_id, value):
    """
    Route to change light state - Accessed using Page GET request
    """
    global sensor_states
    if value == 'True':
        sensor_states['light' + a_id] = True
        update_user_page()
        return 'Set to True'
    else:
        sensor_states['light' + a_id] = False
        update_user_page()
        return 'Set to False'


@app.route('/api/rest/porchlight/<a_id>/<pin_state>', methods=["GET"])
def porchlight_route(a_id, pin_state):
    """
    @brief  Route Used By ESP8266 to read status
    :param a_id:
    :param pin_state:
    :return:
    """
    global sensor_states
    print ( 30 * '-' )
    print ( "Received Request for: Light " + a_id + " and state " + pin_state)
    if int(a_id) == 1:
        if sensor_states['light1']:
            print ("Setting Light 1 ON")
            return ' HIGH'
        else:
            print ("Setting Light 1 OFF")
            return ' LOW'

    elif int(a_id) == 2:
        if sensor_states['light2']:
            print ("Setting Light 2 ON")
            return ' HIGH'
        else:
            print ("Setting Light 2 ON")
            return ' LOW'
    else:
            print ("Default: Sending LOW")
        print (30 * '-')
        return ' LOW'


@app.route('/api/rest/pir/<a_id>/<count>', methods=["GET"])
def pir_data(a_id, count):
    # @brief  Function to put PIR data
    print('PIR Sensor data ' + a_id + ' with count ' + count)
    # data.append_data(count)
    return ' ACK'


@app.route('/api/rest/mag/<id>/<count>', methods=['GET'])
def mag_data(id, count):
    # @brief    Function to put Door Sensor Data
    print('Mag Sensor data ' + id + ' with count ' + count)
    # data.append_data(count)
    return ' ACK'


@app.route('/api/rest/doorbell/<id>/<count>', methods=["GET"])
def doorbell_route(id, count):
    print('Doorbell Pressed '+id+' count '+count)
    return ' ACK'

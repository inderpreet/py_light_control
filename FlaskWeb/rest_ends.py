"""
Rest End points for incoming requests
"""
from FlaskWeb import app, api
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import json

class RestEnds(Resource):
    items=[]

    """
    @brief  Class to handle REST Requests
    """
    def get(self, id, name):

        print("Received call with id: " + id + " and Name: " + name)
        myjson = {
            'id': id,
            'Name': name
        }
        self.items.append(myjson)
        myjson = {
            'id': id+'0',
            'Name': name+" was"
        }
        self.items.append(myjson)
        return ( self.items )
        #return ( json.dumps(self.items) )


class PirCount(Resource):
    """
    @brief  Class For counting PIR Hits
    """
    pirCount = 0

    def get(self, id, count):
        # REST API GET end point
        print("Received Call with id:" + id + " count " + count)
        if( int(id) == 0x01 ):
            self.pirCount += 1
        return ("ACK")

    def getPirCount(self):
        return int(self.pirCount)

# api.add_resource(RestEnds, "/api/rest/<string:id>/<string:name>")
# api.add_resource(PirCount, "/api/rest/pir/<string:id>/<string:count>")



from flask_restx import Api, Resource
from flask import jsonify, current_app, send_file, render_template, request
from sqlalchemy import create_engine
from werkzeug.datastructures import FileStorage

from flask_restx import reqparse

from app import app, auth, log, netcdf2json

# Create the api object using restx
api = Api(app)

netcdf2json_parser = reqparse.RequestParser()
netcdf2json_parser.add_argument('url', required=True, location='args', help="NetCDF URL")


@api.route('/netcdf2json')
@api.expect(netcdf2json_parser)
class NetCDF2Json(Resource):
    def get(self):
        args = netcdf2json_parser.parse_args()
        log.debug(args["url"])
        result = netcdf2json.netcdf2json(args["url"])
        return result, 200


@auth.verify_password
def authenticate(username, password):
    if username and password:
        if username == 'admin' and password == 'password':
            return True
        else:
            return False
    return False
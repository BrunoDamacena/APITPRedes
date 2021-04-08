# pylint: disable=no-member
"""
Main flask file, to create flask app
"""
import logging
import logging.handlers as handlers
import os

from flask import Flask, make_response, jsonify
from flask.logging import default_handler
from werkzeug.exceptions import HTTPException

import controllers.moisture_controller as moisture_controller
from exceptions.conflict_exception import ConflictException
from exceptions.invalid_parameter_exception import InvalidParameterException
from exceptions.missing_parameter_exception import MissingParameterException
from exceptions.not_found_exception import NotFoundException
from utils.json_encoder import ComplexEncoder
from utils.request_formatter import RequestFormatter

APP = Flask(__name__)
APP.json_encoder = ComplexEncoder

# remove default stream handler
APP.logger.removeHandler(default_handler)
logging.getLogger('werkzeug').setLevel(logging.ERROR)

# add RotationFileHandler to logging configuration
HANDLER = handlers.RotatingFileHandler(os.path.join('logs', 'api.log'), maxBytes=50000, backupCount=10)
HANDLER.setFormatter(RequestFormatter('[%(asctime)s] %(module)s %(levelname)s - %(url)s: %(message)s'))
HANDLER.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.INFO, handlers=[HANDLER])

# register blueprints with controllers for simulation, robot and dinosaur
APP.register_blueprint(moisture_controller.BP, url_prefix='/moisture/<chat_id>')


@APP.after_request
def after_request(response):
    """
    Function to execute after all requests, to log them all
    :param response: flask response object
    :return:
    """
    APP.logger.info('Requested')
    return response


@APP.errorhandler(Exception)
def handle_exception(exception):
    """
    Catch exceptions from flask routes
    :param exception: exception raised
    :return:
    """
    APP.logger.exception(exception)
    if isinstance(exception, HTTPException):
        return make_response(jsonify(description=str(exception)), exception.code)
    if isinstance(exception, MissingParameterException):
        return make_response(jsonify(description=str(exception)), 400)
    if isinstance(exception, NotFoundException):
        return make_response(jsonify(description=str(exception)), 404)
    if isinstance(exception, ConflictException):
        return make_response(jsonify(description=str(exception)), 409)
    if isinstance(exception, InvalidParameterException):
        return make_response(jsonify(description=str(exception)), 422)
    return make_response(jsonify(description=str(exception)), 500)


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000)

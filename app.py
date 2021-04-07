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

import controllers.controller as controller
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
APP.register_blueprint(controller.BP, url_prefix='/example_route')


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
    return make_response(jsonify(description=str(exception)), 500)


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000)

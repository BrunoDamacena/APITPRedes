"""
Module with Flask routes
"""

from flask import make_response, jsonify, Blueprint, request

import services.service as service

BP = Blueprint('example_route', __name__)


@BP.route('/', methods=['GET'], strict_slashes=False)
def foo():
    return make_response(jsonify(service.example()), 200)
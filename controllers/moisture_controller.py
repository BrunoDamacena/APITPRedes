"""
Module with Flask routes
"""

from flask import make_response, jsonify, Blueprint, request

import services.moisture_service as moisture_service
from exceptions.missing_parameter_exception import MissingParameterException

BP = Blueprint('moisture', __name__)


@BP.route('/', methods=['POST'], strict_slashes=False)
def moisture_your_plant(chat_id):
    body = request.json
    if body is None or "sensor_id" not in body or "umidade" not in body:
        raise MissingParameterException("Body params missing. Required: [sensor_id, umidade]")

    # here will be the code to send message to Telegram
    # 
    body["chat_id"] = chat_id

    return make_response(jsonify(body), 200)
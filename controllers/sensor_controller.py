"""
Module with Flask routes
"""

from flask import make_response, jsonify, Blueprint, request

import services.sensor_service as sensor_service
from exceptions.missing_parameter_exception import MissingParameterException

BP = Blueprint('sensor', __name__)

@BP.route('/register', methods=["POST"], strict_slashes=False)
def register_your_plant():
    body = request.json
    if body is None or "sensor_id" not in body or "sensor_name" not in body or "chat_id" not in body:
        raise MissingParameterException("Body params missing. Required: [sensor_id, sensor_name, chat_id]")
    # from_csv.save(body["sensor_id"], body["sensor_name"], body["chat_id"])

    return make_response(jsonify("success"), 200)


@BP.route('/moisture', methods=['POST'], strict_slashes=False)
def moisture_your_plant():
    body = request.json
    if body is None or "sensor_id" not in body or "umidade" not in body:
        raise MissingParameterException("Body params missing. Required: [sensor_id, umidade]")

    # Get the chat_id and the sensor_name from the CSV "database"
    # chat_id = from_csv.getChatId(body["sensor_id"])
    # sensor_name = from_csv.getSensorName(body["sensor_id"])

    # Send the message to the right user via Telegram Bot!
    # message = "O sensor" + sensor_name + " precisa ser regado!"
    # sendMessageViaTelegramBot(chat_id, message)

    return make_response(jsonify("success"), 200)
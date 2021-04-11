"""
Module with Flask routes
"""

from flask import make_response, jsonify, Blueprint, request

import services.sensor_service as sensor_service
from exceptions.missing_parameter_exception import MissingParameterException
import utils.csv.repository as repository
BP = Blueprint('sensor', __name__)


@BP.route('/register', methods=["POST"], strict_slashes=False)
def register_your_plant():
    body = request.json
    if body is None or "sensor_id" not in body or "sensor_name" not in body or "chat_id" not in body:
        raise MissingParameterException(
            "Body params missing. Required: [sensor_id, sensor_name, chat_id]")

    repository.saveRegister(
        body["sensor_id"], body["sensor_name"], body["chat_id"])

    return make_response(jsonify("success"), 200)


@BP.route('/moisture', methods=['POST'], strict_slashes=False)
def moisture_your_plant():
    body = request.json
    if body is None or "sensor_id" not in body or "umidade" not in body:
        raise MissingParameterException(
            "Body params missing. Required: [sensor_id, umidade]")

    # Setar valor de umidade de disparo e criar sendMessageViaTelegramBot

    # row = repository.readRegister(body["sensor_id"])

    # if (umidade == NAO_UMIDO):  # Send the message to the right user via Telegram Bot!
    # Disparar telagran aqui
    # message = "O sensor" + row['sensor_name'] + " precisa ser regado!"
    # sendMessageViaTelegramBot(row['chat_id'], message)

    return make_response(jsonify("success"), 200)

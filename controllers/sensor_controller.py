"""
Module with Flask routes
"""

from flask import make_response, jsonify, Blueprint, request
import requests
import uuid

import services.sensor_service as sensor_service
import services.telegram_service as telegram_service
from exceptions.missing_parameter_exception import MissingParameterException


BP = Blueprint('sensor', __name__)

keybot = "Key cmVnYWRvcjpwSVg5dkhyV0hQRVVLYjZTQ3ljWA=="

@BP.route('/register', methods=["POST"], strict_slashes=False)
def register_your_plant():
    body = request.json
    if body is None or "sensor_id" not in body or "sensor_name" not in body or "chat_id" not in body:
        raise MissingParameterException(
            "Body params missing. Required: [sensor_id, sensor_name, chat_id]")

    response = sensor_service.register(
        body["sensor_id"], body["sensor_name"], body["chat_id"])

    return make_response(jsonify(response), 200)


@BP.route('/moisture', methods=['POST'], strict_slashes=False)
def moisture_your_plant():
    body = request.json
    if body is None or "sensor_id" not in body or "umidade" not in body:
        raise MissingParameterException(
            "Body params missing. Required: [sensor_id, umidade]")

    sensor = sensor_service.getRegistry(body["sensor_id"])
    chatId = sensor["chat_id"]

    message = "O sensor " + sensor['sensor_name'] + " precisa ser regado! Nível de umidade em " + str(body["umidade"]) + "%"

    body = {
        "id": str(uuid.uuid4()),
        "to": chatId,
        "type": "text/plain",
        "content": message
    }

    botResponse = requests.post(
        "https://msging.net/messages",
        headers={"Authorization":keybot},
        json=body
    )

    return make_response(jsonify(botResponse.json()), botResponse.status_code)

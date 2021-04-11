import utils.csv.repository as repository


def register(sensor_id, sensor_name, chat_id):
    message = repository.saveRegister(
        sensor_id, sensor_name, chat_id)

    return {"message": message}

def getRegistry(sensor_id):
    row = repository.readRegister(sensor_id)
    return row
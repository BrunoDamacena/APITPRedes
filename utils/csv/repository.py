import pandas as pd
from exceptions.not_found_exception import NotFoundException
from exceptions.invalid_parameter_exception import InvalidParameterException

data_path = "data/data.csv"
cols = ["sensor_id", "sensor_name", "chat_id"]

def getRegister(): 
    try:
        data_csv = pd.read_csv(data_path, usecols=cols, )
    except FileNotFoundError:
        data_csv = pd.DataFrame(columns=cols)
        data_csv.to_csv(data_path, index=False)
    return data_csv


def saveRegister(sensorId, sensorName, chadId):

    if checkRegister(str(sensorId)):
        raise InvalidParameterException(str(sensorId) + " already registered!")

    register = pd.DataFrame({
        'sensor_id': [str(sensorId)],
        'sensor_name': [str(sensorName)],
        'chat_id': [str(chadId)]
    })
    
    register.to_csv(data_path, mode='a', header=False, index=False)

    return str(sensorId) + " registered successfully!"


def readRegister(sensorId):
    data_csv = getRegister()
    queryRes = data_csv.query('sensor_id=="' + str(sensorId) + '"').head(1)

    if queryRes.empty:
        raise NotFoundException("Sensor " + str(sensorId) + " not found!")

    return {
        'sensor_id': queryRes.values[0][0],
        'sensor_name': queryRes.values[0][1],
        'chat_id': queryRes.values[0][2]
    }

# tried to make a oneliner but I failed miserably
def checkRegister(sensorId: str):
    data_csv = getRegister()
    for sensor_id in data_csv.sensor_id:
        if str(sensor_id) == sensorId:
            return True

    return False

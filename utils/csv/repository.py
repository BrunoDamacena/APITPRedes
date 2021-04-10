import pandas as pd


def saveRegister(sensorId, sensorName, chadId):
    df = pd.DataFrame({
        'sensor_id': [sensorId],
        'sensor_name': [sensorName],
        'chat_id': [chadId]
    })

    df.to_csv('data.csv', mode='a', header=False, index=False)

    return df.tail(1)


def readRegister(sensorId):
    df = pd.read_csv("data.csv", usecols=[
                     "sensor_id", "sensor_name", "chat_id"])

    queryRes = df.query('sensor_id=="' + sensorId + '"').head(1)

    return {
        'sensor_id': queryRes.values[0][0],
        'sensor_name': queryRes.values[0][1],
        'chat_id': queryRes.values[0][2]
    }

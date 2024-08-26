import json
import pyrfc


def connect():
    connection_params = json.load(open("settings.ini", encoding="utf-8"))
    conn = pyrfc.Connection(**connection_params['SAP'])
    return conn

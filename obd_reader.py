import obd

def connect():
    print("Proba polaczenia sie z OBD...")
    
    connection = obd.OBD("COM3", fast=False, timeout=2)

    print("Status", connection.status())

    if connection.status() == obd.OBDStatus.NOT_CONNECTED:
        print("Brak polaczenia z OBD")
        return None

    print("Polaczono z OBD. Sprawdzam ECU")

    test = connection.query(obd.commands.SPEED)

    if test.is_null():
        print("ECU nie odpowiada")
        return None

    print("ECU odpowiada")    
    return connection

def get_data(connection, cmd):
    if connection is None:
        return "NO_CONNECTION"
    
    response = connection.query(cmd)

    if response.is_null():
        return "NO_RESPONSE"
    
    return response.value
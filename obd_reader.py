import obd
import serial.tools.list_ports

def connect():
    print("Proba polaczenia sie z OBD...")

    ports = serial.tools.list_ports.comports()
    print("Wykrywam porty OBD")

    for port in ports:
        print(f"Proba: {port.device} ({port.description})")
        try:
            connection = obd.OBD(port.device, fast=False, timeout=2)
            if connection.status() == obd.OBDStatus.CAR_CONNECTED:
                print(f"Polaczono z ECU na {port.device}")
                return connection
        except:
            continue
    print("Nie znaleziono dzialajacego portu.")
    return None

def get_data(connection, cmd):
    if connection is None:
        return "NO_CONNECTION"
    
    response = connection.query(cmd)

    if response.is_null():
        return "NO_RESPONSE"
    
    return response.value
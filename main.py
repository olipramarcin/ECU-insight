import obd
import time

connection = obd.OBD()

cmd = obd.command.RPM

while True:
    response = connection.query(cmd)
    if not response.is_null():
        print(f"RPM: {response.value}")
    time.sleep(1)
import obd
import time
from obd_reader import connect, get_data
from logger import log_to_file

connection = connect()

if connection is None:
    print("Kabel OBD nie jest podlaczony.")
    exit()

print("Polaczono z OBD")

commands = {
    "RPM": obd.commands.RPM,
    "Speed": obd.commands.SPEED,
    "Temperature": obd.commands.COOLANT_TEMP,
    "Throttle": obd.commands.THROTTLE_POS
}

while True:
    output = []

    for name, cmd in commands.items():
        value = get_data(connection, cmd)

        if value == "NO_RESPONSE":
            text = f"{name}: no response"
        elif value == "NO_CONNECTION":
            text = f"{name}: brak polaczenia"
        else:
            text = f"{name}: {value}"

        print(text)
        output.append(text)

    print("------------")
    log_to_file(" | ".join(output))

    time.sleep(1)
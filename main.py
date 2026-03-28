import tkinter as tk
from obd_reader import auto_connect
from logger import log_data
import obd

# Połączenie OBD
connection = auto_connect()

# GUI
root = tk.Tk()
root.title("Engine Insight GUI")

# Etykiety
rpm_label = tk.Label(root, text="RPM: --", font=("Arial", 14))
rpm_label.pack(pady=5)
speed_label = tk.Label(root, text="Speed: --", font=("Arial", 14))
speed_label.pack(pady=5)
coolant_label = tk.Label(root, text="Coolant Temp: --", font=("Arial", 14))
coolant_label.pack(pady=5)
throttle_label = tk.Label(root, text="Throttle Pos: --", font=("Arial", 14))
throttle_label.pack(pady=5)
status_label = tk.Label(root, text="Status: Łączenie...", font=("Arial", 12))
status_label.pack(pady=5)

def update_data():
    if connection:
        rpm = connection.query(obd.commands.RPM)
        speed = connection.query(obd.commands.SPEED)
        coolant = connection.query(obd.commands.COOLANT_TEMP)
        throttle = connection.query(obd.commands.THROTTLE_POS)

        rpm_val = rpm.value if not rpm.is_null() else "No response"
        speed_val = speed.value if not speed.is_null() else "No response"
        coolant_val = coolant.value if not coolant.is_null() else "No response"
        throttle_val = throttle.value if not throttle.is_null() else "No response"

        # Aktualizacja GUI
        rpm_label.config(text=f"RPM: {rpm_val}")
        speed_label.config(text=f"Speed: {speed_val}")
        coolant_label.config(text=f"Coolant Temp: {coolant_val}")
        throttle_label.config(text=f"Throttle Pos: {throttle_val}")
        status_label.config(text="Status: Połączono")

        log_data(rpm_val, speed_val, coolant_val, throttle_val)
    else:
        status_label.config(text="Status: Brak połączenia z ECU")

    root.after(1000, update_data)

update_data()
root.mainloop()
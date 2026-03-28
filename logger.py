import csv
from datetime import datetime

def log_data(rpm, speed, coolant, throttle):
    with open("engine_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), rpm, speed, coolant, throttle])
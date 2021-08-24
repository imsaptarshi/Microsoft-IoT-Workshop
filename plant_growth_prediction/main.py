import time
from os import path
import csv
from datetime import datetime

from counterfit_connection import CounterFitConnection
from counterfit_shims_seeed_python_dht import DHT

# CONSTANTS
FILE = "data.csv"
FIELDS = ["date", "temperature"]


CounterFitConnection.init('127.0.0.1', 5000)

sensor = DHT("11", 0)

while True:
    _, temperature = sensor.read()

    # if file doesn't exists
    if not path.exists(FILE):
        with open(FILE, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=FIELDS)
            writer.writeheader()

    with open(FILE, mode='a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDS)
        writer.writerow({
            "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "temperature": temperature
        })

    #record new telemetry after 10mins interval
    time.sleep(60*10)

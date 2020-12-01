import csv
import os
from models.Vehicle import Vehicle

class VehicleData:
    def __init__(self):
        print("inside data layer")

    def get_vehicles(self):
        retList = []
        with open('data/vehicles.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                vehicle = Vehicle(row["manufacturer"], row["model"], row["vehicle_type"], row["status"], row["man_year"], row["color"], row["licence_type"], row["location"])
                retList.append(vehicle)
        return retList


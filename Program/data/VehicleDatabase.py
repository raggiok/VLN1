import csv
import os
from models.Vehicle import Vehicle

class VehicleData:
    def __init__(self):
        print("inside data layer")

    def new_vehicle(self, unique_id, manufacturer, model, vehicle_type, status, man_year, color, licence_type, location):
        with open('data/vehicles.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['unique_id', 'manufacturer', 'model', 'vehicle_type', 'status', 'man_year', 'color', 'license_type', 'location']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,)
            writer.writerow({'unique_id': unique_id, 'manufacturer': manufacturer, 'model': model, 'vehicle_type': vehicle_type, 'status': status, 'man_year': man_year, 'color': color, 'license_type': licence_type, 'location': location})


    def get_vehicles(self):
        retList = []
        with open('data/vehicles.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                vehicle = Vehicle(row["unique_id"],row["manufacturer"], row["model"], row["vehicle_type"], row["status"], row["man_year"], row["color"], row["licence_type"], row["location"])
                retList.append(vehicle)
        return retList


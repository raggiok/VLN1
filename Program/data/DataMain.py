import csv
import os
from models.Employee import Employee
from models.Vehicle import Vehicle

class DataMain:
    def __init__(self):
        print("inside data layer")

    def get_employees(self):
        #print(os.getcwd())
        retList = []
        with open('data/employees.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                emp = Employee(row["name"], row["age"], row["role"],row["address"])
                retList.append(emp)
        return retList
    
    def get_vehicles(self):
        retList = []
        with open('data/vehicles.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                vehicle = Vehicle(row["manufacturer"], row["model"], row["vehicle_type"], row["status"], row["man_year"], row["color"], row["licence_type"], row["location"])
                retList.append(vehicle)
        return retList


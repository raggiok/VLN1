# import csv
# from data.dataAPI import dataAPI
from models.Vehicle import Vehicle
from models.Employee import Employee
from data.datafunc import Data

# car = Vehicle("1", "manufacturer", "model", "vehicle_type", "status", "man_year", "color", "license_type", "location")



test = Data()


# test.write_data(car, "vehicle")

car2 = Vehicle("27", "blabla", "model", "vehicle_type", "OK", "man_year", "color", "license_type", "location")

# test.edit_data(car2, "vehicle")

employee = Employee("2", "Raggi", "22", "admin", "Heimilisgata 5", "112", "Reykjavik", "Iceland")

test.get_data("vehicle")
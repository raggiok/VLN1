import csv
from data.dataAPI import dataAPI
from models.Vehicle import Vehicle


logic = dataAPI()



car = Vehicle()


logic.delete_vehicle(car)
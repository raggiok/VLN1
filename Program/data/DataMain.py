import csv
import os
from models.Employee import Employee

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
    


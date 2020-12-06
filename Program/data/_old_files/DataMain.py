import csv
import os
from models.Employee import Employee
from models.contracts import Contract

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
    
    def get_contracts(self):
        contract_list = []
        with open('data/contracts.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contract = Contract(row["customer"], row["vin"], row["start_date"],row["end_date"],row["country"],row["contract_id"])
                contract_list.append(contract)
        return contract_list

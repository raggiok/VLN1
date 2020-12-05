import csv
import os
from models.contracts import Contract

class ContractData:
    def __init__(self):
        print("yolo")

    def get_contracts(self):
        contract_list = []
        with open('data/contracts.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contract = Contract(row['customer'], row["vin"], row["start_date"],row["end_date"],row["country"],row["contract_id"])
                contract_list.append(contract)
        return contract_list

    def add_contract(self, customer, vin, start_date, end_date, country, contract_id):
        with open('data/contracts.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['customer', 'vin', 'start_date', 'end_date', 'country', 'contract_id']
            writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
            writer.writerow({'customer': customer, 'vin': vin, 'start_date': start_date, 'end_date': end_date, 'country': country, 'contract_id': contract_id})

    def del_contract(self, new_id):
        temporary_list = []
        confirmation = False
        with open('data/contracts.csv', 'r', encoding="utf-8") as cvsfile:
            for row in csv.DictReader(cvsfile):
                temporary_list.append(row)
            with open('data/contracts.csv', 'w', newline='', encoding="utf-8") as writecvsfile:
                fieldnames = ['customer', 'vin', 'start_date', 'end_date', 'country', 'contract_id'] 
                writer = csv.DictWriter(writecvsfile, delimiter=',', fieldnames=fieldnames)
                writer.writeheader()
                for row in temporary_list:
                    if row['contract_id'] == new_id:
                        confirmation = True
                        continue
                    writer.writerow(row)
            return confirmation
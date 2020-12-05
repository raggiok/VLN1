import csv
import os
from start_dates.contracts import Contract

class ContractData:
    def __init__(self):
        pass

    # This function creates a new unique ID for each contract and stores it in a separate .csv file.
    # It's important that when the program is run for the first time that contract_unique_id.csv and contracts.csv countain an equal amount of values
    def new_contract_id(self):
        '''Returns a new ID for a contract and stores it in a .csv file'''
        temp_list = []
        #Read current ID's in file
        with open('data/unique_id/contract_unique_id.csv', 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                temp_list.append(row)
            counter = len(temp_list) + 1 #add's one
            #Write's a new file and add's the next ID
            with open('data/unique_id/contract_unique_id.csv', 'w', newline='', encoding="utf-8") as newfile:
                fieldnames = ['contract_unique_id']
                writer = csv.DictWriter(newfile, fieldnames=fieldnames,)
                writer.writeheader()
                for row in temp_list:
                    writer.writerow(row)
                writer.writerow({'contract_unique_id': counter})
        return counter

    def add_contract(self, contract):
        with open('data/contracts.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['unique_id','customer', 'vehicle_unique_id', 'start_date', 'end_date', 'country']
            writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
            writer.writerow({'unique_id': contract.unique_id,'customer': contract.customer, 'vehicle_unique_id': contract.vehicle_unique_id, 'start_date': contract.start_date, 'end_date': contract.end_date, 'country': contract.country})

    def edit_contract(self, updated_contract):
        '''Register's changes of a specific contract'''
        #read file and add content to temp file
        contract_list = []
        confirmation = False
        with open('data/contracts.csv', 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contract_list.append(row)
            #write new file with same content and add new row if it has same ID
            with open('data/contracts.csv', 'w', newline='', encoding="utf-8") as newfile:
                fieldnames = ['unique_id', 'customer', 'vehicle_unique_id', 'start_date', 'end_date', 'country']
                writer = csv.DictWriter(newfile, fieldnames=fieldnames,)
                writer.writeheader()
                for row in contract_list:
                    if updated_contract.unique_id == row["unique_id"]:
                        row = {"unique_id": updated_contract.unique_id, "vehicle_unique_id": updated_contract.vehicle_unique_id, "start_date": updated_contract.start_date, "end_date": updated_contract.end_date, "country": updated_contract.country, "state": state}
                        confirmation = True
                    writer.writerow(row)
        return confirmation

    #Delete contract from data put's it into "Inactive state"
    def delete_contract(self, contract): #Data layer receives an instance of Vehicle
        contract_list = []
        confirmation = False
        with open('data/contracts.csv', 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contract_list.append(row)
            with open('data/contracts.csv', 'w', newline='', encoding="utf-8") as writecvsfile:
                fieldnames = ['unique_id', 'manufacturer', 'model', 'vehicle_type', 'status', 'man_year', 'color', 'license_type', 'location', 'state']
                writer = csv.DictWriter(writecvsfile, delimiter=',', fieldnames=fieldnames)
                writer.writeheader()
                for row in contract_list:
                    if row['unique_id'] == contract.unique_id:
                        row = {"unique_id": contract.unique_id, "vehicle_unique_id": contract.vehicle_unique_id, "start_date": contract.start_date, "end_date": contract.end_date, "country": contract.country, "state": state}
                        confirmation = True
                    writer.writerow(row)
        return confirmation #Returns True if successfully deleted, otherwise False

    def get_contracts(self):
        contract_list = []
        with open('data/contracts.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contract = Contract(row['unique_id'], row['customer'], row["vehicle_unique_id"], row["start_date"],row["end_date"],row["country"])
                contract_list.append(contract)
        return contract_list
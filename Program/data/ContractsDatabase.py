import csv
import os
from models.contracts import Contract

class ContractData:
    def __init__(self):
        self.data = "data"

    def get_contracts(self):
        contract_list = []
        with open('data/contracts.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                contract = Contract(row["customer"], row["vin"], row["start_date"],row["end_date"],row["country"],row["contract_id"])
                contract_list.append(contract)
        return contract_list
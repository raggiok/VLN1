import csv
import os
from models.Customer import Customer

class CustomerData:
    def __init__(self):
        print("inside database")

    def get_customer(self):
        retList = []
        with open('data/customer.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customer = Customer(row["name"], row["ssn"], row["address"], row["postnumber"], row["phone"], row["email"], row["land"])
                retList.append(customer)
        return retList

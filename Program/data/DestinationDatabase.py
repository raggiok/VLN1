import csv
import os
from models.Destinations import Destination

class DestinationData:
    
    def __init__(self):
        print("inside data layer")

     #Create New Destination
    def new_destination(self, destination):
        '''Registers the new destination in the database'''
        with open('destinations.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['country', 'airport', 'phone_number', 'opening_hours']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,)
            print(destination)
            writer.writerow({'country': destination.country, 'airport': destination.airport, 'phone_number': destination.phone_number, 'opening_hours': destination.opening_hours})
   
    def edit_destination(self, updated_destination):
        '''Register's changes of a specific vehicle'''
        #read file
        temp_list = []
        with open('data/destinations.csv', 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                temp_list.append(row)
            #write file
            with open('data/destinations.csv', 'w', newline='', encoding="utf-8") as newfile:
                fieldnames = ['country', 'airport', 'phone_number', 'opening_hours']
                writer = csv.DictWriter(newfile, fieldnames=fieldnames,)
                writer.writeheader()
                for row in temp_list:
                    if updated_vehicle.unique_id == row["unique_id"]:
                        writer.writerow({'country': updated_destination.country, 'airport': updated_destination.airport, 'phone_number': updated_destination.phone_number, 'opening_hours': updated_destination.opening_hours})
                    writer.writerow(row)

    def get_destinations(self):
        '''Returns a list of all vehicles in database'''
        retList = []
        with open('destinations.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                destination = Destination(row["country"],row["airport"], row["phone_number"], row["opening_hours"])
                retList.append(destination)
        return retList                
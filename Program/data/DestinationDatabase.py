import csv
import os
from models.Destinations import Destination

class DestinationData:
    
    def __init__(self):
        print("inside data layer")

    def new_destination_id(self):
        '''Returns a new ID for a destination and stores it in a .csv file'''
        temp_list = []
        #Read current ID's in file
        with open('data/unique_id/destination_unique_id.csv', 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                temp_list.append(row)
            counter = len(temp_list) + 1 #add's one
            #Write's a new file and add's the next ID
            with open('data/unique_id/destination_unique_id.csv', 'w', newline='', encoding="utf-8") as newfile:
                fieldnames = ['destination_unique_id']
                writer = csv.DictWriter(newfile, fieldnames=fieldnames,)
                writer.writeheader()
                for row in temp_list:
                    writer.writerow(row)
                writer.writerow({'destination_unique_id': counter})
        return counter

     #Create New Destination
    def create_destination(self, destination):
        '''Registers the new destination in the database'''
        with open('destinations.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['unique_id', 'country', 'city', 'airport', 'phone_number', 'opening_time', 'closing_time', 'state']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,)
            writer.writerow({'unique_id': destination.unique_id, 'country': destination.country,'city': destination.city, 'airport': destination.airport, 'phone_number': destination.phone_number, 'opening_time': destination.opening_time, 'closing_time': destination.closing_time, 'state': destination.state})
   
    def edit_destination(self, updated_destination):
        '''Register's changes of a specific vehicle'''
        #read file
        temp_list = []
        confirmation = False
        with open('data/destinations.csv', 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                temp_list.append(row)
            #write file
            with open('data/destinations.csv', 'w', newline='', encoding="utf-8") as newfile:
                fieldnames = ['country', 'airport', 'phone_number', 'opening_time']
                writer = csv.DictWriter(newfile, fieldnames=fieldnames,)
                writer.writeheader()
                for row in temp_list:
                    if updated_destination.unique_id == row["unique_id"]:
                        writer.writerow({'country': updated_destination.country, 'airport': updated_destination.airport, 'phone_number': updated_destination.phone_number, 'opening_time': updated_destination.opening_time})
                        confirmation = True
                    writer.writerow(row)
        return confirmation

    def get_destinations(self):
        '''Returns a list of all vehicles in database'''
        retList = []
        with open('data/destinations.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                destination = Destination(row["unique_id"],row["country"],row["airport"], row["phone_number"], row["opening_time"],row['closing_time'], row['state'] )
                retList.append(destination)
        return retList                
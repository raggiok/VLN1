import csv
from models.Vehicle import Vehicle

class VehicleData:
    def __init__(self):
        pass

    # This function creates a new unique ID for each vehicle and stores it in a separate .csv file.
    # It's important that when the program is run for the first time that vehicle_unique_id.csv and vehicles.csv countain an equal amount of values
    def new_vehicle_id(self):
        '''Returns a new ID for a vehicle and stores it in a .csv file'''
        temp_list = []
        #Read current ID's in file
        with open('data/unique_id/vehicle_unique_id.csv', 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                temp_list.append(row)
            counter = len(temp_list) + 1 #add's one
            #Write's a new file and add's the next ID
            with open('data/unique_id/vehicle_unique_id.csv', 'w', newline='', encoding="utf-8") as newfile:
                fieldnames = ['vehicle_unique_id']
                writer = csv.DictWriter(newfile, fieldnames=fieldnames,)
                writer.writeheader()
                for row in temp_list:
                    writer.writerow(row)
                writer.writerow({'vehicle_unique_id': counter})
        return counter

    #Create New Vehicle
    def new_vehicle(self, vehicle):
        '''Registers the new vehicle in the database'''
        with open('data/vehicles.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['unique_id', 'manufacturer', 'model', 'vehicle_type', 'status', 'man_year', 'color', 'license_type', 'location','state']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,)
            writer.writerow({'unique_id': vehicle.unique_id, 'manufacturer': vehicle.manufacturer, 'model': vehicle.model, 'vehicle_type': vehicle.vehicle_type, 'status': vehicle.status, 'man_year': vehicle.man_year, 'color': vehicle.color, 'license_type': vehicle.license_type, 'location': vehicle.location, 'state': vehicle.state})
        #we need to return True if all elements of vehicle were stored accurately in database else false
        #Add a function that goes through each parameter and checks if it's the same as what was delivered


    def edit_vehicle(self, updated_vehicle):
        '''Register's changes of a specific vehicle'''
        #read file and add content to temp file
        temporary_list = []
        confirmation = False
        with open('data/vehicles.csv', 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                temporary_list.append(row)
            #write new file with same content and add new row if it has same ID
            with open('data/vehicles.csv', 'w', newline='', encoding="utf-8") as newfile:
                fieldnames = ['unique_id', 'manufacturer', 'model', 'vehicle_type', 'status', 'man_year', 'color', 'license_type', 'location', 'state']
                writer = csv.DictWriter(newfile, fieldnames=fieldnames,)
                writer.writeheader()
                for row in temporary_list:
                    if updated_vehicle.unique_id == row["unique_id"]:
                        row = {"unique_id": updated_vehicle.unique_id, "manufacturer": updated_vehicle.manufacturer, "model": updated_vehicle.model, "vehicle_type": updated_vehicle.vehicle_type, "status": updated_vehicle.status, "man_year": updated_vehicle.man_year, "color": updated_vehicle.color, "license_type": updated_vehicle.license_type, "location": updated_vehicle.location, "state": state}
                        confirmation = True
                    writer.writerow(row)
        return confirmation

    #Delete Vehicle from data
    def delete_vehicle(self, vehicle): #Data layer receives an instance of Vehicle
        temporary_list = []
        confirmation = False
        with open('data/vehicles.csv', 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                temporary_list.append(row)
            with open('data/vehicles.csv', 'w', newline='', encoding="utf-8") as writecvsfile:
                fieldnames = ['unique_id', 'manufacturer', 'model', 'vehicle_type', 'status', 'man_year', 'color', 'license_type', 'location','state']
                writer = csv.DictWriter(writecvsfile, delimiter=',', fieldnames=fieldnames)
                writer.writeheader()
                for row in temporary_list:
                    if row['unique_id'] == vehicle.unique_id:
                        row = {"unique_id": vehicle.unique_id, "manufacturer": vehicle.manufacturer, "model": vehicle.model, "vehicle_type": vehicle.vehicle_type, "status": vehicle.status, "man_year": vehicle.man_year, "color": vehicle.color, "license_type": vehicle.license_type, "location": vehicle.location, "state": "Inactive"}
                        confirmation = True
                    writer.writerow(row)
        return confirmation #Returns True if successfully deleted, otherwise False

    def get_vehicles(self):
        '''Returns a list of all vehicles in database'''
        retList = []
        with open('data/vehicles.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                vehicle = Vehicle(row["unique_id"],row["manufacturer"], row["model"], row["vehicle_type"], row["status"], row["man_year"], row["color"], row["license_type"], row["location"])
                retList.append(vehicle)
        return retList
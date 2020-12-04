import csv
from models.Vehicle import Vehicle

class VehicleData:
    def __init__(self):
        print("inside data layer")

    #Create New Vehicle
    def new_vehicle(self, vehicle):
        '''Registers the new vehicle in the database'''
        with open('data/vehicles.csv', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['unique_id', 'manufacturer', 'model', 'vehicle_type', 'status', 'man_year', 'color', 'license_type', 'location']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,)
            writer.writerow({'unique_id': vehicle.unique_id, 'manufacturer': vehicle.manufacturer, 'model': vehicle.model, 'vehicle_type': vehicle.vehicle_type, 'status': vehicle.status, 'man_year': vehicle.man_year, 'color': vehicle.color, 'license_type': vehicle.license_type, 'location': vehicle.location})

    def edit_vehicle(self, updated_vehicle):
        '''Register's changes of a specific vehicle'''
        #read file
        temp_list = []
        with open('data/vehicles.csv', 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                temp_list.append(row)
            #write file
            with open('data/vehicles.csv', 'w', newline='', encoding="utf-8") as newfile:
                fieldnames = ['unique_id', 'manufacturer', 'model', 'vehicle_type', 'status', 'man_year', 'color', 'license_type', 'location']
                writer = csv.DictWriter(newfile, fieldnames=fieldnames,)
                writer.writeheader()
                for row in temp_list:
                    if updated_vehicle.unique_id == row["unique_id"]:
                        row = {"unique_id": updated_vehicle.unique_id, "manufacturer": updated_vehicle.manufacturer, "model": updated_vehicle.model, "vehicle_type": updated_vehicle.vehicle_type, "status": updated_vehicle.status, "man_year": updated_vehicle.man_year, "color": updated_vehicle.color, "license_type": updated_vehicle.license_type, "location": updated_vehicle.location}
                    writer.writerow(row)

    def get_vehicles(self):
        '''Returns a list of all vehicles in database'''
        retList = []
        with open('data/vehicles.csv', newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                vehicle = Vehicle(row["unique_id"],row["manufacturer"], row["model"], row["vehicle_type"], row["status"], row["man_year"], row["color"], row["license_type"], row["location"])
                retList.append(vehicle)
        return retList
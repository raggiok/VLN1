from data.dataAPI import dataAPI
from models.Vehicle import Vehicle

class VehicleLogic():
    def __init__(self):
        self.data = dataAPI()

    def create_vehicle(self,manufacturer,model,vehicle_type,status,manufacturing_year,color,license_requirement,location):
        '''Registers a vehicle in vehicles.csv and returns True if successful and False if it't not registered'''
        vehicle = Vehicle(self.data.new_vehicle_id(),manufacturer, model, vehicle_type, status, manufacturing_year, color, license_requirement,location)
        return self.data.create_vehicle(vehicle)

    def edit_vehicle(self, vehicle_instance):
        '''Edits a vehicle in the database'''
        return self.data.edit_vehicle(vehicle_instance)

    #Returns a list of vehicle types
    def vehicle_types(self):
        '''Returns a list of vehicle types'''
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.vehicle_type not in retList:
                retList.append(vehicle.vehicle_type)
        return retList

    #Returns all information about all vehicles
    def all_vehicles(self):
        '''Returns all information about all vehicles'''
        return self.data.get_vehicles()

    #Returns the total number of listed vehicles in Database
    def vehicle_amount_registered(self):
        '''Returns the total number of listed vehicles in Data'''
        return len(self.data.get_vehicles())

    # Return unique ID for vehicle from data
    def add_unique_ID(self):
        '''Returns the next number in line for vehicles in databse'''
        return self.data.new_vehicle_id()
          

    def search_vehicle_by_ID(self, vehicle_ID):
        '''Returns a single vehicle with corresponding ID'''
        ret_list = []
        vehicles = self.data.get_vehicles()
        for vehicle in vehicles:
            if vehicle.unique_id == vehicle_ID:
                ret_list.append(vehicle)
        return self.no_match_found(ret_list)

    #Searches for vehicle by Type
    def search_vehicle_by_type(self, vehicle_type):
        '''Returns a list of vehicles based on the type selected'''
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.vehicle_type == vehicle_type:
                retList.append(vehicle)
        return self.no_match_found(retList)

    def delete_vehicle(self, ID_number):
        if self.search_vehicle_by_ID(ID_number)[0] == ID_number:
            self.data.delete_vehicle(self.search_vehicle_by_ID(ID_number)[0])
        else:
            return "No match found."

    def no_match_found(self, result_list):
        if result_list:
            return result_list
        else:
            result_list.append("No match found.")
            return result_list
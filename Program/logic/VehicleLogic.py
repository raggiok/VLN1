from data.dataAPI import dataAPI
from models.Vehicle import Vehicle

class VehicleLogic():
    def __init__(self):
        self.data = dataAPI()

    def create_vehicle(self,manufacturer,model,vehicle_type,status,manufacturing_year,color,license_type,location):
        '''Registers a vehicle in vehicles.csv and returns True if successful and False if it't not registered'''
        vehicle = Vehicle(self.data.new_vehicle_id(),manufacturer, model, vehicle_type, status, manufacturing_year, color, license_type,location)
        return self.data.create_vehicle(vehicle)

    def edit_vehicle(self, vehicle_instance):
        '''Edits a vehicle in the database'''
        return self.data.edit_vehicle(vehicle_instance)

    
    ##### part of search function###
    def available_model(self):
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.model not in retList:
                retList.append(vehicle.model)
        return retList

    def available_manufacturers(self):
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.manufacturer not in retList:
                retList.append(vehicle.manufacturer)
        return retList

    def available_vehicle_type(self):
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.vehicle_type not in retList:
                retList.append(vehicle.vehicle_type)
        return retList
      
    def available_model(self):
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.model not in retList:
                retList.append(vehicle.model)
        return retList

    def available_status(self):
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.status not in retList:
                retList.append(vehicle.status)
        return retList

    def available_manufacturing_year(self):
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.manufacturing_year not in retList:
                retList.append(vehicle.manufacturing_year)
        return retList     

    def available_color(self):
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.color not in retList:
                retList.append(vehicle.color)
        return retList

    def available_license_type(self):
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.license_type not in retList:
                retList.append(vehicle.license_type)
        return retList

    def available_location(self):
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.location not in retList:
                retList.append(vehicle.location)
        return retList

       #Searches for vehicle by Type
    def search_vehicle_by_manufacturer(self, manufacturer):
        '''Returns a list of vehicles based on the type selected'''
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.manufacturer == manufacturer:
                retList.append(vehicle)
        return self.no_match_found(retList)

    def search_vehicle_by_model(self, model):
        '''Returns a list of vehicles based on the type selected'''
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.model == model:
                retList.append(vehicle)
        return self.no_match_found(retList)

    def search_vehicle_by_vehicle_type(self, vehicle_type):
        '''Returns a list of vehicles based on the type selected'''
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.vehicle_type == vehicle_type:
                retList.append(vehicle)
        return self.no_match_found(retList)

    def search_vehicle_by_status(self, status):
        '''Returns a list of vehicles based on the type selected'''
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.status == status:
                retList.append(vehicle)
        return self.no_match_found(retList)

    def search_vehicle_by_manufacturing_year(self, manufacturing_year):
        '''Returns a list of vehicles based on the type selected'''
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.manufacturing_year == manufacturing_year:
                retList.append(vehicle)
        return self.no_match_found(retList)

    def search_vehicle_by_license_type(self, license_type):
        '''Returns a list of vehicles based on the type selected'''
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.license_type == license_type:
                retList.append(vehicle)
        return self.no_match_found(retList)

    def search_vehicle_by_location(self, location):
        '''Returns a list of vehicles based on the type selected'''
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.location == location:
                retList.append(vehicle)
        return self.no_match_found(retList)

    def search_vehicle_by_ID(self, ID):
        retList = []
        search_list = self.data.get_vehicles()
        for vehicle in search_list:
            if vehicle.unique_id == ID:
                retList.append(vehicle)
        return self.no_match_found(retList)
        

    ### maintainance functions ###
        def vehicle_check_in(self, vehicle_ID):
            vehicle = self

        def vehicle_check_out(self, vehicle_ID):
            
















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

    def delete_vehicle(self, ID_number):
        search = self.search_vehicle_by_ID(ID_number)
        if search[0] != "No match found.":
            self.data.delete_vehicle(search[0])
        else:
            return search

    def no_match_found(self, result_list):
        if result_list:
            return result_list
        else:
            result_list.append("No match found.")
            return result_list
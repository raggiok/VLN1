from data.VehicleDatabase import VehicleData

class VehicleLogic():
    def __init__(self):
        self.data = VehicleData()

    def create_vehicle(self, vehicle_instance):
        '''Creates a vehicle in the database'''
        return self.data.new_vehicle(vehicle_instance)

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

    #Add an unique_ID to vehicle
    def add_unique_ID(self):
        '''Returns the next number in line for vehicles in databse'''
        total_vehicle_count = self.vehicle_amount_registered()
        total_vehicle_count += 1
        return total_vehicle_count

    def search_vehicle_by_ID(self, vehicle_ID):
        '''Returns a single vehicle with corresponding ID'''
        vehicles = self.data.get_vehicles()
        for vehicle in vehicles:
            if vehicle.unique_id == vehicle_ID:
                return vehicle

    #Searches for vehicle by Type
    def search_vehicle_by_type(self, vehicle_type):
        '''Returns a list of vehicles based on the type selected'''
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.vehicle_type == vehicle_type:
                retList.append(vehicle)
        return retList
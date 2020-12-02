from data.VehicleDatabase import VehicleData

class VehicleLogic():
    def __init__(self):
        self.data = VehicleData()

    def create_vehicle(self, vehicle_list):
        return self.data.new_vehicle(vehicle_list[0], vehicle_list[1], vehicle_list[2],vehicle_list[3], vehicle_list[4], vehicle_list[5], vehicle_list[6], vehicle_list[7], vehicle_list[8])

    def vehicle_types(self):
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.vehicle_type not in retList:
                retList.append(vehicle.vehicle_type)
        return retList

    def all_vehicles(self):
        return self.data.get_vehicles()

    def search_vehicle_by_type(self, vehicle_type):
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.vehicle_type == vehicle_type:
                retList.append(vehicle)
        return retList
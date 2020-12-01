from data.VehicleDatabase import VehicleData

class VehicleLogic():
    def __init__(self):
        self.data = VehicleData()

    def all_vehicles(self):
        return self.data.get_vehicles()

    def vehicle_by_type(self, vehicle_type):
        vehicle = self.data.get_vehicles()
        retList = []
        for vehicle in vehicle:
            if vehicle.vehicle_type == vehicle_type:
                retList.append(vehicle)
        return retList
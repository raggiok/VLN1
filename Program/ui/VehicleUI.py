from logic.VehicleLogic import VehicleLogic

class VehicleUI:
    def __init__(self):
        self.logic = VehicleLogic()
        self.ui_print()
        self.ui_print_type()


    def ui_print(self):
        results  = self.logic.all_vehicles()
        print("\nAll vehicles:")
        print("{} {:>12} {:>20} {:>20} {:>20} {:>20} {:>20} {:>20}".format("Manufacturer", "Model", "Type", "Status", "Manufactured Year", "Color", "Licence Requirement", "Location"))
        print("-"*150)
        
        for vehicle in results:
            print(vehicle)

    
    def ui_print_type(self):
        vehicle_type = input("Please enter vehicle type: ")
        results  = self.logic.vehicle_by_type(vehicle_type)
        print("\nAll vehicles by type " + vehicle_type + ": ")
        for vehicle in results:
            print(vehicle)
        
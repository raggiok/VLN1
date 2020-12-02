from ui.UIMain import UIMain
from logic.VehicleLogic import VehicleLogic

class VehicleUI:
    def __init__(self):
        self.logic = VehicleLogic()
        self.vehicle_menu()
        # self.ui_print_type()

    #Prints UI for new vehicle
    def ui_new_vehicle(self):
        vehicleFieldnames = ["Unique_id","Manufacturer","Model","Vehicle_type","Status","Man_year","Color","Licence_type","Location"] #can we automate this list to fetch the header?
        inputList = []
        print("\nPress 'q' and hit 'enter' to cancel at any time.")
        print("\nPlease enter the following details to create a new vehicle:" )
        user_input = ""
        for field in vehicleFieldnames:
            if user_input == "q":
                return self.vehicle_menu()
            user_input = input(f"Enter {field}: ")
            inputList.append(user_input)
        return inputList

    #Prints the vehicle types
    def ui_print_types(self):
        print("\nVehicle types available:")
        vehicles = self.logic.vehicle_types()
        for vehicle in vehicles:
            print("\t" + vehicle)
        print()

    #Print Vehicle Header
    def ui_vehicle_header(self):
        print("{} {:>12} {:>20} {:>20} {:>20} {:>20} {:>20} {:>20}".format("Manufacturer", "Model", "Type", "Status", "Manufactured Year", "Color", "Licence Requirement", "Location"))

    #Prints all vehicles
    def ui_all_vehicles(self):
        results  = self.logic.all_vehicles()
        print("\nAll vehicles:")
        self.ui_vehicle_header()
        print("-"*150)
        for vehicle in results:
            print(vehicle)
    
    #Prints all the vehicles of the same type
    def ui_print_type(self):
        self.ui_print_types()
        vehicle_type = input("Please enter vehicle type: ")
        results  = self.logic.search_vehicle_by_type(vehicle_type)
        print("\nAll vehicles by type " + vehicle_type + ": ")
        self.ui_vehicle_header()
        print("-"*150)
        for vehicle in results:
            print(vehicle)
        print("-"*150)
        print()

    #Prints the search menu for vehicles
    def ui_search_menu(self):
        print("\n" + "-"*20 + "Vehicle Search" + "-"*20)
        print("\nPlease enter search option:")
        print("1. By Type")
        print("2. By Availability")
        print("3. By Manufactuerer")
        print("4. By Model")
        print("5. Other")
        print("\n" + "-"*50)
        selection = input("\n>> Select option: ")
        return selection


    #Prints the Vehicle Main Menu
    def vehicle_menu(self):
        while True:
            print("-"*20 + "Vehicle Menu" + "-"*20)
            print("\nSelect an option...\n1. Create new vehicle \n2. Search vehicles \n3. Check availability \n4. Return vehicle \n5. View all vehicles \n6. Main Menu\n")
            print("-"*50)
            command = input(">> Select option: ")
            command = command.lower()
            if command == "1":
                new_vehicle = self.ui_new_vehicle()
                self.logic.create_vehicle(new_vehicle)
            elif command == "2":
                selection = self.ui_search_menu()
                if selection == "1":
                    self.ui_print_type()
                elif selection == "2":
                    pass
                elif selection == "3":
                    pass
                elif selection == "4":
                    pass
                elif selection == "5":
                    pass                
            elif command == "3":
                results  = self.logic.all_vehicles()
                print("\nAll vehicles:")
                for vehicle in results:
                    print(vehicle)
            elif command == "4":
                pass
            elif command == "5":
                self.ui_all_vehicles()
            elif command == "6":
                return UIMain()
            else:
                print("Invalid command, try again")
    

        
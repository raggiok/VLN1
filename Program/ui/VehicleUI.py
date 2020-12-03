from ui.UIMain import UIMain
from logic.VehicleLogic import VehicleLogic
from models.Vehicle import Vehicle

class VehicleUI:
    def __init__(self):
        self.logic = VehicleLogic()
        self.vehicle_menu()
        # self.ui_print_type()

    #Prints UI for new vehicle
    def ui_new_vehicle(self):
        vehicleFieldnames = ["Manufacturer","Model","Vehicle type","Status","Manufacturing year","Color","License Requirement","Location"]
        inputList = []
        print("\nPress 'q' and hit 'enter' to cancel at any time.")
        print("\nPlease enter the following details to create a new vehicle:" )
        user_input = ""
        for field in vehicleFieldnames:
            if user_input == "q":
                return self.vehicle_menu()
            user_input = input(f"Enter {field}: ")
            inputList.append(user_input)
        vehicle = Vehicle(self.logic.add_unique_ID(), *inputList)
        return vehicle

    #Request new value from user
    def value_input(self):
        return input("Enter new value: ")

    #Creates the Edit menu layout and returns the Vehicle Instance after edit
    def ui_edit_vehicle(self):
        vehicle = self.ui_single_vehicle_ID() #prints specific vehicle
        selection = ""
        while selection != "9":
            self.ui_print_edit_menu() #ask user what he would like to edit
            selection = self.ui_edit_input()
            if selection == "1":
                vehicle.manufacturer = self.value_input()
            elif selection == "2":
                vehicle.model = self.value_input()
            elif selection == "3":
                vehicle.vehicle_type = self.value_input()
            elif selection == "4":
                vehicle.status = self.value_input()
            elif selection == "5":
                vehicle.man_year = self.value_input()
            elif selection == "6":
                vehicle.color = self.value_input()
            elif selection == "7":
                vehicle.license_type = self.value_input()
            elif selection == "8":
                vehicle.location = self.value_input()
            elif selection == "9":
                print(vehicle)
                return vehicle

    #Get input for edit menu
    def ui_edit_input(self):
        selection = input("\n>> Select option: ")
        return selection
    
    #Prints the Vehicle Edit menu options
    def ui_print_edit_menu(self):
        '''Prints options for Edit menu and accepts input'''
        self.ui_menu_header("Edit vehicle")
        print("\nSelect field to edit:")
        print("1. Manufacturer")
        print("2. Model")
        print("3. Vehicle type")
        print("4. Status")
        print("5. Manufacturing year")
        print("6. Color")
        print("7. License Requirement")
        print("8. Location")
        print("9. Exit")
        self.ui_menu_footer()

    #Print Vehicle Table Header
    def ui_vehicle_table_header(self):
        print(f"{'Unique ID':<20}{'Manufacturer':<20}{'Model':<20}{'Vehicle type':<20}{'Status':<20}{'Manufac. year':<20}{'Color':<20}{'License Req.':<20}{'Location':<20}")
        print("-"*200)
    
    #Print Vehicle Table Footer
    def ui_vehicle_table_footer(self):
        print("-"*200)
        print()

    #Prints all vehicles
    def ui_all_vehicles(self):
        results  = self.logic.all_vehicles()
        print("\nAll vehicles:")
        self.ui_vehicle_table_header()
        for vehicle in results:
            print(vehicle)
        self.ui_vehicle_table_footer()
    
    #Prints vehicle with unique ID
    def ui_single_vehicle_ID(self):
        '''Prints a single vehicle with a unique ID'''
        vehicle_ID = input(">> Please enter vehicle ID: ")
        vehicle  = self.logic.search_vehicle_by_ID(vehicle_ID)
        print("\nVehicle by ID: " + vehicle_ID)
        self.ui_vehicle_table_header()
        print(vehicle) 
        self.ui_vehicle_table_footer()
        return vehicle
    
    #Prints the vehicle type categories
    def ui_print_types(self):
        '''Prints all vehicle type categories'''
        print("\nVehicle types available:")
        vehicles = self.logic.vehicle_types()
        for vehicle in vehicles:
            print("\t" + vehicle)
        print()

    #Prints all the vehicles of the same type
    def ui_print_type(self):
        self.ui_print_types()
        vehicle_type = input(">> Please enter vehicle type: ")
        results  = self.logic.search_vehicle_by_type(vehicle_type)
        print("\nAll vehicles by type " + vehicle_type + ": ")
        self.ui_vehicle_table_header()
        for vehicle in results:
            print(vehicle)
        self.ui_vehicle_table_footer()

    #Menu header
    def ui_menu_header(self, menu_name):
        print("\n" + "-"*20 + f"{menu_name}" + "-"*20)

    #Menu footer
    def ui_menu_footer(self):
        print("\n" + "-"*50)

    #Prints the search menu for vehicles
    def ui_search_menu(self):
        self.ui_menu_header("Vehicle Search")
        print("\nPlease select a search option:")
        print("1. Type")
        print("2. Availability")
        print("3. Manufactuerer")
        print("4. Model")
        print("5. Other")
        print("6. Exit")
        self.ui_menu_footer
        selection = input("\n>> Select option: ")
        return selection


    #Prints the Vehicle Main Menu
    def vehicle_menu(self):
        while True:
            self.ui_menu_header("Vehicle Menu")
            print("\nSelect an option...\n1. Create new vehicle \n2. Search vehicles \n3. Check availability \n4. Return vehicle \n5. View all vehicles \n6. Edit vehicle \n7. Delete vehicle \n8. Main Menu")
            self.ui_menu_footer()
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
                elif selection == "6":
                    return VehicleUI()
            elif command == "3":
                self.ui_all_vehicles()
            elif command == "4":
                pass
            elif command == "5":
                self.ui_all_vehicles()
            elif command == "6":
                new_vehicle = self.ui_edit_vehicle()
                self.logic.edit_vehicle(new_vehicle)
            elif command == "7":
                pass    
            elif command == "8":
                return UIMain()
            else:
                print("Invalid command, try again")
    

        
from ui.UIMain import UIMain
from logic.logicAPI import LogicAPI
from models.Vehicle import Vehicle


class VehicleUI:
    def __init__(self):
        self.logic = LogicAPI()
        self.vehicle_menu()
        # self.ui_print_type()

    #Prints UI for new vehicle
    def ui_new_vehicle(self):
        vehicleFieldnames = ["Manufacturer","Model","Vehicle type","Status","Manufacturing year","Color","License Requirement","Location", "Rate"]
        inputList = []
        print("\nPress 'q' and hit 'enter' to cancel at any time.")
        print("\nPlease enter the following details to create a new vehicle:" )
        user_input = ""
        for field in vehicleFieldnames:
            if user_input.lower() == "q":
                return self.vehicle_menu()
            user_input = input(f"Enter {field}: ")
            inputList.append(user_input)
        return inputList

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
                vehicle.rate = self.value_input()
            elif selection == "q":
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
        print("9. Rate")
        print("q. Exit")
        self.ui_menu_footer()
        

    #Print Vehicle Table Header
    def ui_vehicle_table_header(self):
        print(f"{'Unique ID':<20}{'Manufacturer':<20}{'Model':<20}{'Vehicle type':<20}{'Status':<20}{'Manufac. year':<20}{'Color':<20}{'License Req.':<20}{'Location':<20}{'Rate':<20}")
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
        vehicles  = self.logic.search_vehicle_by_ID(vehicle_ID)
        print("\nVehicle by ID: " + vehicle_ID)
        self.ui_vehicle_table_header()
        for vehicle in vehicles:
            print(vehicle) 
        self.ui_vehicle_table_footer()
        return vehicle

####################################################Search Menus##########################################################################  
    

    def ui_manufacturer_available_print(self):
        print("\nAvailable Options:")
        vehicles = self.logic.available_manufacturers()
        for vehicle in vehicles:
            print("\t" + vehicle)
        print()

    def ui_model_available_print(self):
        print("\nAvailable Options:")
        vehicles = self.logic.available_model()
        for vehicle in vehicles:
            print("\t" + vehicle)
        print()

    def ui_vehicle_type_available_print(self):
        print("\nAvailable Options:")
        vehicles = self.ui_vehicle_type_available_print()
        for vehicle in vehicles:
            print("\t" + vehicle)
        print()

    def ui_status_available_print(self):
        print("\nAvailable Options:")
        vehicles = self.logic.available_status()
        for vehicle in vehicles:
            print("\t" + vehicle)
        print()

    def ui_manufacturing_year_available_print(self):
        print("\nAvailable Options:")
        vehicles = self.logic.available_manufacturing_year()
        for vehicle in vehicles:
            print("\t" + vehicle)
        print()

    def ui_color_available_print(self):
        print("\nAvailable Options:")
        vehicles = self.logic.available_color()
        for vehicle in vehicles:
            print("\t" + vehicle)
        print()

    def ui_license_type_available_print(self):
        print("\nAvailable Options:")
        vehicles = self.logic.available_license_type()
        for vehicle in vehicles:
            print("\t" + vehicle)
        print()

    def ui_location_available_print(self):
        print("\nAvailable Options:")
        vehicles = self.logic.available_location()
        for vehicle in vehicles:
            print("\t" + vehicle)
        print()


    
    def ui_print_manufacturer(self):
        self.ui_manufacturer_available_print()
        manufacturer = input(">> Please enter vehicle manufacturer: ")
        results  = self.logic.search_vehicle_by_manufacturer(manufacturer)
        print("\nAll vehicles by manufacturer " + manufacturer + ": ")
        self.ui_vehicle_table_header()
        for vehicle in results:
            print(vehicle)
        self.ui_vehicle_table_footer()
    
    def ui_print_model(self):
        self.ui_model_available_print()
        model = input(">> Please enter vehicle model: ")
        results  = self.logic.search_vehicle_by_model(model)
        print("\nAll vehicles by model " + model + ": ")
        self.ui_vehicle_table_header()
        for vehicle in results:
            print(vehicle)
        self.ui_vehicle_table_footer()

    def ui_print_vehicle_type(self):
        self.ui_vehicle_type_available_print()
        vehicle_type = input(">> Please enter vehicle type: ")
        results  = self.logic.search_vehicle_by_vehicle_type(vehicle_type)
        print("\nAll vehicles by type " + vehicle_type + ": ")
        self.ui_vehicle_table_header()
        for vehicle in results:
            print(vehicle)
        self.ui_vehicle_table_footer()

    def ui_print_status(self):
        self.ui_status_available_print()
        status = input(">> Please enter vehicle status: ")
        results  = self.logic.search_vehicle_by_status(status)
        print("\nAll vehicles by type " + status + ": ")
        self.ui_vehicle_table_header()
        for vehicle in results:
            print(vehicle)
        self.ui_vehicle_table_footer()

    def ui_print_manufacturing_year(self):
        self.ui_manufacturer_available_print()
        manufacturing_year = input(">> Please enter vehicle manufacturing year: ")
        results  = self.logic.search_vehicle_by_type(manufacturing_year)
        print("\nAll vehicles by manufacturing year " + manufacturing_year + ": ")
        self.ui_vehicle_table_header()
        for vehicle in results:
            print(vehicle)
        self.ui_vehicle_table_footer()
    
    def ui_print_color(self):
        self.ui_color_available_print()
        color = input(">> Please enter vehicle color: ")
        results  = self.logic.search_vehicle_by_color(color)
        print("\nAll vehicles by color " + color + ": ")
        self.ui_vehicle_table_header()
        for vehicle in results:
            print(vehicle)
        self.ui_vehicle_table_footer()

    def ui_print_license_type(self):
        self.ui_license_type_available_print()
        license_type = input(">> Please enter vehicle license requirement: ")
        results  = self.logic.search_vehicle_by_license_type(license_type)
        print("\nAll vehicles by type " + license_type + ": ")
        self.ui_vehicle_table_header()
        for vehicle in results:
            print(vehicle)
        self.ui_vehicle_table_footer()

    def ui_print_location(self):
        self.ui_location_available_print()
        location = input(">> Please enter vehicle location: ")
        results  = self.logic.search_vehicle_by_location(location)
        print("\nAll vehicles by type " + location + ": ")
        self.ui_vehicle_table_header()
        for vehicle in results:
            print(vehicle)
        self.ui_vehicle_table_footer()

#########################################################################################################################


    #Prints the search menu for vehicles
    def ui_search_menu(self):
        self.ui_menu_header("Vehicle Search")
        print("\nPlease select a search option:")
        self.UI_numbered_menu(["Manufacturer","Model","Vehicle type","Status","Manufacturing year","Color","License Requirement","Location","Exit"])
        self.ui_menu_footer
        selection = input("\n>> Select option: ")
        return selection

    #Prints any UI menu in order
    def UI_numbered_menu(self, a_list):
        '''Takes a list as parameter and prints all the items of a list in an order from 1. list[0], 2. list[1] and so on'''
        for i in range(0,(len(a_list))):
            print(f"{i+1}. {a_list[i]}")

    #Prints the Vehicle Main Menu
    def vehicle_menu(self):
        while True:
            self.ui_menu_header("Vehicle Menu")
            print("\nSelect an option...\n1. Create new vehicle \n2. Search vehicles \n3. Check availability \n4. Return/check out vehicle. \n5. View all vehicles \n6. Edit vehicle \n7. Delete vehicle \n8. Main Menu")
            self.ui_menu_footer()
            command = input(">> Select option: ")
            command = command.lower()
            if command == "1":
                new_vehicle = self.ui_new_vehicle()
                self.logic.create_vehicle(*new_vehicle)
            elif command == "2":
                selection = self.ui_search_menu()   
                if selection == "1":
                    self.ui_print_manufacturer()
                elif selection == "2":
                    self.ui_print_model()
                elif selection == "3":
                    self.ui_print_vehicle_type()
                elif selection == "4":
                    self
                elif selection == "5":
                    self.ui_print_manufacturing_year()
                elif selection == "6":
                    self.ui_print_color()
                elif selection == "7":
                    self.ui_print_license_type()
                elif selection == "8":
                    self.ui_print_location()
                elif selection == "9":   
                    self.vehicle_menu()
            elif command == "3":
                self.ui_all_vehicles()
            elif command == "4":
                self.ui_checkin_menu()
            elif command == "5":
                self.ui_all_vehicles()
            elif command == "6":
                new_vehicle = self.ui_edit_vehicle()
                self.logic.edit_vehicle(new_vehicle)
            elif command == "7":
                vehicle_id = input(">> Enter vehicle ID to delete: ")
                vehicle = self.logic.delete_vehicle(vehicle_id)
                for result in vehicle:
                    print(result)  
            elif command == "8":
               return UIMain()
            else:
                print("Invalid command, try again")
    
    def ui_checkin_menu(self):
        self.ui_menu_header('Check-in Menu')
        print("Select an option...\n1.Check out vehicle.\n2.Check in vehicle.\n3.Return.")
        self.ui_menu_footer()
        choice = input(">> Select option: ")
        if choice == '3':
            return
        elif choice == '1':
            vehicle = input("Enter vehicle ID: ")
            print(self.logic.vehicle_check_out(vehicle))
        elif choice == '2':
            vehicle = input("Enter vehicle ID: ")
            print(self.logic.vehicle_check_in(vehicle))
        elif choice == '3':
            return
    #Menu header
    def ui_menu_header(self, menu_name):
        print("\n" + "-"*20 + f"{menu_name}" + "-"*20)

    #Menu footer
    def ui_menu_footer(self):
        print("\n" + "-"*50)  
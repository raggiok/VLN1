from ui.UIMain import UIMain
from logic.logicAPI import LogicAPI
from models.Destinations import Destination

class destinationUI:
    def __init__(self):
        self.logicAPI = LogicAPI()
        self.destination_menu()
        # self.ui_print_type()

    #Prints UI for new destination
    def ui_new_destination(self):
        destinationFieldnames = ["country","airport","phone_number","opening_time","closing_time","main_contact","state"] 
        inputList = []
        print("\nPress 'q' and hit 'enter' to cancel at any time.")
        print("\nPlease enter the following details to create a new destination:" )
        user_input = ""
        user_input = ""
        for field in destinationFieldnames:
            if user_input.lower() == "q":
                return self.destination_menu()
            user_input = input(f"Enter {field}: ")
            inputList.append(user_input)
        return inputList

    #Request new value from user
    def value_input(self):
        return input("Enter new value: ")

    #Creates the Edit menu layout and returns the destination Instance after edit
    def ui_edit_destination(self):
        destination = self.ui_single_destination_ID() #prints specific destination
        selection = ""
        while selection != "9":
            self.ui_print_edit_menu() #ask user what he would like to edit
            selection = self.ui_edit_input()
            if selection == "1":
                destination.country = self.value_input()
            elif selection == "2":
                destination.airport = self.value_input()
            elif selection == "3":
                destination.phone_number = self.value_input()
            elif selection == "4":
                destination.opening_time = self.value_input()
            elif selection == "5":
                destination.closing_time = self.value_input()
            elif selection == "6":
                destination.main_contact = self.value_input()
            elif selection == "7":
                destination.state = self.value_input()
            elif selection == "8":
                return destination

    #Get input for edit menu
    def ui_edit_input(self):
        selection = input("\n>> Select option: ")
        return selection
    
    #Prints the destination Edit menu options
    def ui_print_edit_menu(self):
        '''Prints options for Edit menu and accepts input'''
        self.ui_menu_header("Edit destination")
        print("\nSelect field to edit:")
        print("1. Country")
        print("2. Airport")
        print("3. Phone Number")
        print("4. Opening Time")
        print("5. Closing Time")
        print("6. Main Contact")
        print("7. State")
        print("8. Exit")
        self.ui_menu_footer()

    #Print Destination Table Header
    def ui_destination_table_header(self):
        print(f"{'Country':<20}{'Airport':<20}{'Phone Number':<20}{'Opening Time':<20}{'Closing Time':<20}{'Main Contact':<20}{'State':<20}")
        print("-"*200)

    #Print destination Table Footer
    def ui_destination_table_footer(self):
        print("-"*200)
        print()

    #Prints all destinations
    def ui_all_destinations(self):
        results  = self.logicAPI.all_destinations()
        print("\nAll destinations:")
        self.ui_destination_table_header()
        for destination in results:
            print(destination)
        self.ui_destination_table_footer()
    
    #Prints destination with unique ID
    def ui_single_destination_ID(self):
        '''Prints a single destination with a unique ID'''
        destination_ID = input(">> Please enter destination ID: ")
        destination  = self.logicAPI.search_destination_by_ID(destination_ID)
        print("\ndestination by ID: " + destination_ID)
        self.ui_destination_table_header()
        print(destination) 
        self.ui_destination_table_footer()
        return destination
    
    #Prints the destination type categories
    def ui_print_types(self):
        '''Prints all destination type categories'''
        print("\nAvailable Options:")
        destinations = self.logicAPI.destination_types()
        for destination in destinations:
            print("\t" + destination)
        print()

    #Prints all the destinations of the same county
    def search_destination_by_country(self):
        self.ui_print_types()
        destination_type = input(">> Please enter destination type: ")
        results  = self.logicAPI.search_destination_by_type(destination_type)
        print("\nAll destinations by type " + destination_type + ": ")
        self.ui_destination_table_header()
        for destination in results:
            print(destination)
        self.ui_destination_table_footer()

    def search_destination_by_airport():
        pass    

        
    def ui_print_type(self):
        #self.ui_print_types()
        country = input(">> Please enter destination type: ")
        results  = self.logicAPI.destination_types()
        print("\nAll destination by type " + country + ": ")
        self.ui_destination_table_header()
        for destination in results:
            print(destination)
        self.ui_destination_table_footer()
    #Menu header
    def ui_menu_header(self, menu_name):
        print("\n" + "-"*20 + f"{menu_name}" + "-"*20)

    #Menu footer
    def ui_menu_footer(self):
        print("\n" + "-"*50)

    #Prints the search menu for destinations
    def ui_search_menu(self):
        self.ui_menu_header("Destination Search")
        print("\nPlease select a search option:")
        self.UI_numbered_menu(["Country", "Airport", "Phone Number", "Opening Time","Closing Time","Main Contact","State", "Exit"])
        self.ui_menu_footer
        selection = input("\n>> Select option: ")
        return selection

    #Prints any UI menu in order
    def UI_numbered_menu(self, a_list):
        '''Takes a list as parameter and prints all the items of a list in an order from 1. list[0], 2. list[1] and so on'''
        for i in range(0,(len(a_list))):
            print(f"{i+1}. {a_list[i]}")

    #Prints the destination Main Menu
    def destination_menu(self):
        while True:
            self.ui_menu_header("Destination Menu")
            print("\nSelect an option...\n1. Create new destination \n2. Search destinations \n3. View all destinations \n4. Edit destination \n5. Delete destination \n6. Main Menu")
            self.ui_menu_footer()
            command = input(">> Select option: ")
            command = command.lower()
            if command == "1":
                new_destination = self.ui_new_destination()
                self.logicAPI.create_destination(*new_destination)
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
                    return destinationUI()
            elif command == "3":
                self.ui_all_destinations()
            elif command == "4":
                pass
            elif command == "5":
                self.ui_all_destinations()
            elif command == "6":
                new_destination = self.ui_edit_destination()
                self.logicAPI.edit_destination(new_destination)
            elif command == "7":
                pass    
            elif command == "8":
                return UIMain()
            else:
                print("Invalid command, try again")
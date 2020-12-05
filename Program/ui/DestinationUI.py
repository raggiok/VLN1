from ui.UIMain import UIMain
from logic.DestinationLogic import DestinationLogic
from models.Destinations import Destination


class DestinationUI:
    def __init__(self):
        self.logic = DestinationLogic()
        self.destination_menu()
        # self.ui_print_type()

    #Prints UI for new destination
    def ui_new_destination(self):

        destinationFieldnames = ["country","airport","phone_number","opening_hours"] 
        inputList = []
        print("\nPress 'q' and hit 'enter' to cancel at any time.")
        print("\nPlease enter the following details to create a new destination:" )
        user_input = ""

        for field in destinationFieldnames:
            if user_input == "q":
                return self.destination_menu()
            user_input = input(f"Enter {field}: ")
            inputList.append(user_input)
        return inputList
        #Get input for edit menu
    def ui_edit_input(self):
        selection = input("\n>> Select option: ")
        return selection
    
    #Prints the Destination Edit menu options
    def ui_print_edit_menu(self):
        '''Prints options for Edit menu and accepts input'''
        self.ui_menu_header("Edit Destination")
        print("\nSelect field to edit:")
        print("1. Country")
        print("2. Airport")
        print("3. Phone Number")
        print("4. Opening Hours")
        print("5. Exit")
        self.ui_menu_footer()

    #Print Destination Table Header
    def ui_destination_table_header(self):
        print(f"{'Country':<20}{'Airport':<20}{'Phone Number':<20}{'Opening Hours':<20}")
        print("-"*200)
    
    #Print Destination Table Footer
    def ui_destination_table_footer(self):
        print("-"*200)
        print()

    #Prints all destinations
    def ui_all_destinations(self):
        results  = self.logic.all_destinations()
        print("\nAll destinations:")
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
        self.UI_numbered_menu(["Country", "Airport", "Phone Number", "Opening Hours", "Exit"])
        self.ui_menu_footer
        selection = input("\n>> Select option: ")
        return selection

    #Prints any UI menu in order
    def UI_numbered_menu(self, a_list):
        '''Takes a list as parameter and prints all the items of a list in an order from 1. list[0], 2. list[1] and so on'''
        for i in range(0,(len(a_list))):
            print(f"{i+1}. {a_list[i]}")    

    #Prints the Destination Main Menu
    def destination_menu(self):
        while True:
            self.ui_menu_header("Destination Menu")
            print("\nSelect an option...\n1. Create new destination \n2. Search destinations \n3. View all destinations \n4. Edit destination \n5. Delete destination \n6. Main Menu")
            self.ui_menu_footer()
            command = input(">> Select option: ")
            command = command.lower()
            if command == "1":
                new_destination = self.ui_new_destination()
                self.logic.create_destination(new_destination)
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
                    return DestinationUI()
            elif command == "3":
                self.ui_all_destinations()
            elif command == "4":
                pass
            elif command == "5":
                self.ui_all_destinations()
            elif command == "6":
                new_destination = self.ui_edit_destination()
                self.logic.edit_destination(new_destination)
            elif command == "7":
                pass    
            elif command == "8":
                return UIMain()
            else:
                print("Invalid command, try again")    
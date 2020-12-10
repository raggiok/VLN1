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
        destinationFieldnames = ["country","city","airport","phone_number","opening_time","closing_time","main_contact"] 
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
        self.ui_all_destinations()
        destination = self.ui_single_destination_ID() #prints specific destination
        selection = ""
    
        while selection != "9":
            self.ui_print_edit_menu() #ask user what he would like to edit
            selection = self.ui_edit_input()
            if selection == "1":
                destination.country = self.value_input()
            elif selection == "2":
                destination.city = self.value_input()    
            elif selection == "3":
                destination.airport = self.value_input()
            elif selection == "4":
                destination.phone_number = self.value_input()
            elif selection == "5":
                destination.opening_time = self.value_input()
            elif selection == "6":
                destination.closing_time = self.value_input()
            elif selection == "7":
                destination.main_contact = self.value_input()
            elif selection == "8":
                destination.state = self.value_input()
            elif selection == "9":
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
        print("2. City")
        print("3. Airport")
        print("4. Phone Number")
        print("5. Opening Time")
        print("6. Closing Time")
        print("7. Main Contact")
        print("8. State")
        print("9. Exit")
        self.ui_menu_footer()

    #Print Destination Table Header
    def ui_destination_table_header(self):
        print(f"{'Unique ID':<20}{'Country':<20}{'City':<20}{'Airport':<20}{'Phone Number':<20}{'Opening Time':<20}{'Closing Time':<20}{'Main Contact':<20}")
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
        destination  = self.logicAPI.search_destinations_by_id(destination_ID)
        print("\ndestination by ID: " + destination_ID)
        self.ui_destination_table_header()
        for destination in destination:
            print(destination) 
        self.ui_destination_table_footer()
        return destination



    ### search function ###
    

    def ui_country_available_print(self):
        '''Prints all destination type categories'''
        print("\nAvailable Options:")
        destinations = self.logicAPI.available_country()
        for destination in destinations:
            print("\t" + destination)
        print()

    def ui_city_available_print(self):
        '''Prints all destination type categories'''
        print("\nAvailable Options:")
        destinations = self.logicAPI.available_city()
        for destination in destinations:
            print("\t" + destination)
        print()

    def ui_airport_available_print(self):
        '''Prints all destination type categories'''
        print("\nAvailable Options:")
        destinations = self.logicAPI.available_airport()
        for destination in destinations:
            print("\t" + destination)
        print()

    def ui_phone_number_available_print(self):
        '''Prints all destination type categories'''
        print("\nAvailable Options:")
        destinations = self.logicAPI.available_phone_number()
        for destination in destinations:
            print("\t" + destination)
        print()

    def ui_opening_time_available_print(self):
        '''Prints all destination type categories'''
        print("\nAvailable Options:")
        destinations = self.logicAPI.available_opening_time()
        for destination in destinations:
            print("\t" + destination)
        print()

    def ui_closing_time_available_print(self):
        '''Prints all destination type categories'''
        print("\nAvailable Options:")
        destinations = self.logicAPI.available_closing_time()
        for destination in destinations:
            print("\t" + destination)
        print()    

    def ui_main_contact_available_print(self):
        '''Prints all destination type categories'''
        print("\nAvailable Options:")
        destinations = self.logicAPI.available_main_contact()
        for destination in destinations:
            print("\t" + destination)
        print()             

        
    def ui_print_country(self):
        self.ui_country_available_print()
        country = input(">> Please enter destination Country: ")
        results  = self.logicAPI.search_destination_by_country(country)
        print("\nSearch results for " + country + ": ")
        self.ui_destination_table_header()
        for destination in results:
            print(destination)
        self.ui_destination_table_footer()


    def ui_print_city(self):
        self.ui_city_available_print()
        city = input(">> Please enter destination City: ")
        results  = self.logicAPI.search_destination_by_city(city)
        print("\nSearch results for " + city + ": ")
        self.ui_destination_table_header()
        for destination in results:
            print(destination)
        self.ui_destination_table_footer()

    def ui_print_airport(self):
        self.ui_airport_available_print()
        airport = input(">> Please enter destination Airport: ")
        results  = self.logicAPI.search_destination_by_city(airport)
        print("\nSearch results for " + airport + ": ")
        self.ui_destination_table_header()
        for destination in results:
            print(destination)
        self.ui_destination_table_footer()

    def ui_print_phone_number(self):
        self.ui_phone_number_available_print()
        phone_number = input(">> Please enter destination Phone number: ")
        results  = self.logicAPI.search_destination_by_phone_number(phone_number)
        print("\nSearch results for " + phone_number + ": ")
        self.ui_destination_table_header()
        for destination in results:
            print(destination)
        self.ui_destination_table_footer()


    def ui_print_opening_time(self):
        self.ui_opening_time_available_print()
        opening_time = input(">> Please enter destination Opening time: ")
        results  = self.logicAPI.search_destination_by_opening_time(opening_time)
        print("\nSearch results for " + opening_time + ": ")
        self.ui_destination_table_header()
        for destination in results:
            print(destination)
        self.ui_destination_table_footer()    

    def ui_print_closing_time(self):
        self.ui_closing_time_available_print()
        closing_time = input(">> Please enter destination Closing time: ")
        results  = self.logicAPI.search_destination_by_opening_time(closing_time)
        print("\nSearch results for " + closing_time + ": ")
        self.ui_destination_table_header()
        for destination in results:
            print(destination)
        self.ui_destination_table_footer() 

    def ui_print_main_contact(self):
        self.ui_main_contact_available_print()
        main_contact = input(">> Please enter destination Main contact: ")
        results  = self.logicAPI.search_destination_by_main_contact(main_contact)
        print("\nSearch results for " + main_contact + ": ")
        self.ui_destination_table_header()
        for destination in results:
            print(destination)
        self.ui_destination_table_footer() 

    ### search function ###

   

    #Prints the search menu for destinations
    def ui_search_menu(self):
        self.ui_menu_header("Destination Search")
        print("\nPlease select a search option:")
        self.UI_numbered_menu(["Country","City", "Airport", "Phone Number", "Opening Time","Closing Time","Main Contact", "Exit"])
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
                    self.ui_print_country()
                elif selection == "2":
                    self.ui_print_city()
                elif selection == "3":
                    self.ui_print_airport()
                elif selection == "4":
                    self.ui_print_phone_number()
                elif selection == "5":
                    self.ui_print_opening_time()
                elif selection == "6":
                    self.ui_print_closing_time()
                elif selection == "7":
                    self.ui_print_main_contact()
                elif selection == "8":
                    self.ui_destination_menu()    
            elif command == "3":
                self.ui_all_destinations()
            elif command == "4":
                new_destination = self.ui_edit_destination()
                self.logicAPI.edit_destination(new_destination)
            elif command == "5":
                self.ui_all_destinations()
                destination_id = input(">> Enter destination ID to delete: ")
                destination = self.logicAPI.delete_destination(destination_id)
                for result in destination:
                    print(result) 
            elif command == "6":
                return UIMain()
            else:
                print("Invalid command, try again")


        #Menu header
    def ui_menu_header(self, menu_name):
        print(" _   _       _   _            _      _ _                  ")
        print("| \ | |     | \ | |     /\   (_)    | (_)                 ")
        print("|  \| | __ _|  \| |    /  \   _ _ __| |_ _ __   ___  ___  ")
        print("| . ` |/ _` | . ` |   / /\ \ | | '__| | | '_ \ / _ \/ __| ")
        print("| |\  | (_| | |\  |  / ____ \| | |  | | | | | |  __/\__ \ ")
        print("|_| \_|\__,_|_| \_| /_/    \_\_|_|  |_|_|_| |_|\___||___/ ")
        print("-"*20 + f"{menu_name}" + "-"*20)

    #Menu footer
    def ui_menu_footer(self):
        print("-"*50)
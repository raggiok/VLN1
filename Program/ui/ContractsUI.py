from logic.logicAPI import LogicAPI
from ui.UIMain import UIMain
from models.contracts import Contract
import datetime


class ContractUI:

    def __init__(self):
        self.logic = LogicAPI()
        self.contract_main_menu()

    ### GENERAL FUNCTIONS ###

    #Prints any UI menu in numbered list
    def ui_numbered_menu(self, a_list):
        '''Takes a list as parameter and prints all the items of a list in an order from 1. list[0], 2. list[1] and so on'''
        for i in range(0,(len(a_list))):
            print(f"{i+1}. {a_list[i]}")

    #Menu header
    def ui_menu_header(self, menu_name):
        print("\n" + "-"*20 + f"{menu_name}" + "-"*20)

    #Menu footer
    def ui_menu_footer(self):
        print("\n" + "-"*53)

    def print_select_option(self):
        return input(">> Select option: ").lower()

    def print_table_header(self):
        print()
        print(f'{"Contract ID":<20}{"Customer Name":<20}{"Customer SSN":<20}{"Vehicle ID":<20}{"Contract Duration":<29}{"Country":<20}{"Employee":<20}{"Total price":<20}{"Creation Date":<20}{"Check-out Date":<20}{"Check-in Date":<20}{"Check-in Location":<20}')
        print("="*250)

    #Print Contract Table Footer
    def print_table_footer(self):
        print("-"*250)
        print()

    def validate(self,date_text):
        try:
            datetime.datetime.strptime(date_text, '%d.%m.%y')
            return True
        except ValueError:
            print("\nIncorrect input, make sure the format is DD.MM.YY\n")
            return False

    #Prints UI for new contract
    def new_contract(self):
        contractFieldnames = ["Customer name", "Customer SSN","Vehicle ID", "Start date of rental period (dd.mm.yy)","End date of rental period (dd.mm.yy)","Country","Employee name","Total price"] # + "Contract Creation Date"
        inputList = []
        print("\nPress 'q' and hit 'enter' to cancel at any time.")
        print("\nPlease enter the following details to create a new contract:" )
        user_input = ""
        for field in contractFieldnames:
            user_input = input(f"Enter {field}: ")
            if user_input.lower() == "q":
                return self.contract_main_menu()
            #Checks start date format
            if contractFieldnames.index(field) == 3:
                date_check = False
                while user_input != "q":
                    date_check = self.validate(user_input)
                    if date_check == False:
                        user_input = input(f"Enter {field}: ")
                    else:
                        start_date = datetime.datetime.strptime(user_input, '%d.%m.%y')
                        yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
                        if start_date <= yesterday:
                            print("Dates before today are invalid")
                            user_input = input(f"Enter {field}: ")
                        else:
                            break
            #Checks end date format
            elif contractFieldnames.index(field) == 4:
                date_check = False
                while user_input != "q":
                    date_check = self.validate(user_input)
                    if date_check == False:
                        user_input = input(f"Enter {field}: ")
                    else:
                        end_date = datetime.datetime.strptime(user_input, '%d.%m.%y')
                        if start_date > end_date:
                            print("Dates before start date are invalid.")
                            user_input = input(f"Enter {field}: ")
                        else:
                            break            
            inputList.append(user_input)
        #Add Contract creation date "Contract Creation Date"
        contract_creation_date = datetime.datetime.today()
        contract_creation_date = contract_creation_date.strftime('%d.%m.%y')
        inputList.append(contract_creation_date)
        return inputList


    ### CONTRACT MAIN MENU ###
    def contract_main_menu(self):
        while True:
            self.ui_menu_header("Contract Menu")
            print("\nPlease select a an option:")
            self.ui_numbered_menu(["Create contract", "Search contracts", "View all contracts", "Edit contract", "Cancel contract", "Delete contract", "Main menu"])
            self.ui_menu_footer()
            command = self.print_select_option()
            if command == "1":  #1. Create contract
                contract_param = self.new_contract()
                print(self.logic.create_new_contract(contract_param))
            elif command == "2": # 2. Search contracts
                self.contract_search_menu()
            elif command == "3": # 3. View all contracts
                self.print_table_header()
                for item in self.logic.all_contracts():
                    print(item)
                self.print_table_footer()
            elif command == "4": # 4. Edit contracts
                self.ui_all_contracts()
                edited_contract = self.ui_edit_contract()
                self.print_table_header()
                print(edited_contract)
                self.print_table_footer()
            elif command == "5": # 5. Cancel contract
                self.ui_all_contracts()
                edited_contract = self.ui_edit_contract()
                self.print_table_header()
                print(edited_contract)
                self.print_table_footer()
            elif command == "6": # 6. Delete contract
                contract_id = input(">> Enter contract ID to delete: ")
                result_list = self.logic.delete_contract(contract_id)
                for item in result_list:
                    print(item)
            elif command == "7":
                return UIMain() 
            else:
                print("Invalid command, try again")


    ### CONTRACT SEARCH MENU ###

    def contract_search_menu(self):
        while True:
            self.ui_menu_header("Contract Search")
            print("\nPlease select search option:")
            self.ui_numbered_menu(["Search by Contract ID", "Search by Customer name", "Search by Vehicle ID", "Main menu"])
            self.ui_menu_footer()
            command = self.print_select_option()
            if command == "1":
                contract_id = input(">> Enter Contract ID: ")
                a_list = self.logic.search_contracts_by_id(contract_id)
                self.print_table_header()
                for item in a_list:
                    print(item)
            elif command == "2":
                vehicle_id = input(">> Enter Customer name: ")
                a_list = self.logic.search_contracts_by_customer(vehicle_id)
                self.print_table_header()
                for item in a_list:
                    print(item)
            elif command == "3":
                vehicle_id = input(">> Enter vehicle ID: ")
                a_list = self.logic.search_contract_by_vin(vehicle_id)
                self.print_table_header()
                for item in a_list:
                    print(item)
            elif command == "4":
                return ContractUI() 
            else:
                print("Invalid command, try again")
 
    #Creates the Edit menu layout and returns the Contract Instance after edit
    def ui_edit_contract(self):
        contracts = self.ui_single_contract_ID() #returns a list of contracts, in this case only one contract
        selection = ""
        while selection != "8":
            self.ui_print_edit_menu() #ask user what he would like to edit
            selection = self.ui_edit_input()
            if selection == "1":
                for contract in contracts:
                    contract.customer = self.value_input()
            elif selection == "2":
                for contract in contracts:
                    contract.vehicle_unique_id = self.value_input()
            elif selection == "3":
                for contract in contracts:
                    contract.start_date = self.value_input()
            elif selection == "4":
                for contract in contracts:
                    contract.end_date = self.value_input()
            elif selection == "5":
                for contract in contracts:
                    contract.country = self.value_input()
            elif selection == "6":
                for contract in contracts:
                    contract.employee = self.value_input()
            elif selection == "7":
                for contract in contracts:
                    contract.total_price = self.value_input()
            elif selection == "8":
                return contract

    #Get input for edit menu
    def ui_edit_input(self):
        selection = input("\n>> Select option: ")
        return selection

    #Prints the Vehicle Edit menu options
    def ui_print_edit_menu(self):
        '''Prints options for Edit menu and accepts input'''
        self.ui_menu_header("Edit vehicle")
        print("\nSelect field to edit:")
        print("1. Customer name")
        print("2. Vehicle ID")
        print("3. Start date")
        print("4. End date")
        print("5. Country")
        print("6. Employee name")
        print("7. Total price")
        print("8. Exit")
        self.ui_menu_footer()

    #Prints contract with unique ID
    def ui_single_contract_ID(self):
        '''Prints a single vehicle with a unique ID'''
        contract_ID = input(">> Enter contract ID: ")
        contract  = self.logic.search_contracts_by_id(contract_ID)
        print("\Contract by ID: " + contract_ID)
        self.print_table_header()
        for single_contract in contract:
            print(single_contract) 
        self.print_table_footer()
        return contract

    #Request new value from user
    def value_input(self):
        return input("Enter new value: ")

    #Prints all contracts
    def ui_all_contracts(self):
        contracts  = self.logic.all_contracts()
        print("\nAll Contracts:")
        self.print_table_header()
        for contract in contracts:
            print(contract)
        self.print_table_footer()
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
        print(f'{"Contract ID":<20}{"Customer Name":<20}{"Vehicle ID":<20}{"Contract Duration":<29}{"Country":<20}{"Employee":<20}{"Total price":<20}{"Contract Creation Date":<20}')
        print("="*171)

    def validate(self,date_text):
        try:
            datetime.datetime.strptime(date_text, '%d.%m.%y')
            return True
        except ValueError:
            print("\nIncorrect input, make sure the format is DD.MM.YY\n")
            return False

    #Prints UI for new contract
    def new_contract(self):
        contractFieldnames = ["Customer name","Vehicle ID", "Start date of rental period (dd.mm.yy)","End date of rental period (dd.mm.yy)","Country","Employee Name","Total price"] # + "Contract Creation Date"
        inputList = []
        print("\nPress 'q' and hit 'enter' to cancel at any time.")
        print("\nPlease enter the following details to create a new contract:" )
        user_input = ""
        for field in contractFieldnames:
            user_input = input(f"Enter {field}: ")
            if user_input.lower() == "q":
                return self.contract_main_menu()
            #Checks start date format
            if contractFieldnames.index(field) == 2:
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
            elif contractFieldnames.index(field) == 3:
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
            self.ui_numbered_menu(["Create contract", "Search contracts", "View all contracts", "Edit contract", "Delete contract", "Main menu"])
            self.ui_menu_footer()
            command = self.print_select_option()
            if command == "1":
                contract_param = self.new_contract()
                self.logic.create_new_contract(contract_param)
            elif command == "2":
                self.contract_search_menu()
            elif command == "3":
                self.print_table_header()
                for item in self.logic.all_contracts():
                    print(item)
            elif command == "4":
                pass
            elif command == "5":
                contract_id = input(">> Enter contract ID to delete: ")
                self.logic.delete_contract(contract_id)
            elif command == "6":
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

#unique_id, customer, vehicle_unique_id, start_date, end_date, country, employee, total_price, contract_creation_date
 
    #Creates the Edit menu layout and returns the Contract Instance after edit
    def ui_edit_contract(self):
        contract = self.ui_single_contract_ID() #prints specific contract
        selection = ""
        while selection != "9":
            self.ui_print_edit_menu() #ask user what he would like to edit
            selection = self.ui_edit_input()
            if selection == "1":
                vehicle.customer = self.value_input()
            elif selection == "2":
                vehicle.vehicle_unique_id = self.value_input()
            elif selection == "3":
                vehicle.start_date = self.value_input()
            elif selection == "4":
                vehicle.end_date = self.value_input()
            elif selection == "5":
                vehicle.country = self.value_input()
            elif selection == "6":
                vehicle.employee = self.value_input()
            elif selection == "7":
                vehicle.total_price = self.value_input()
            elif selection == "8":
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
        print("8. Exit")
        self.ui_menu_footer()

    #Prints vehicle with unique ID
    def ui_single_contract_ID(self):
        '''Prints a single vehicle with a unique ID'''
        vehicle_ID = input(">> Enter vehicle ID: ")
        vehicle  = self.logic.search_vehicle_by_ID(vehicle_ID)
        print("\nVehicle by ID: " + vehicle_ID)
        self.ui_vehicle_table_header()
        print(vehicle) 
        self.ui_vehicle_table_footer()
        return vehicle

    #Request new value from user
    def value_input(self):
        return input("Enter new value: ")


#  def all_contracts(self):
#         return self.contract.all_contracts()

#     def search_contracts_by_name(self, name):
#         return self.contract.search_contracts_by_name(name)

#     def create_new_contract(self, a_list):
#         self.contract.create_contract(a_list)

#     def search_contracts_by_customer(self, string):
#         return self.contract.search_contracts_by_customer(string)
    
#     def search_contract_by_vin(self, string):
#         return self.contract.search_contracts_by_vin(string)
    
#     def search_contracts_by_id(self, string):
#         return self.contract.search_contracts_by_id(string)

#     def delete_contract(self, string):
#         return self.contract.delete_contract(string)








#     def contract_ui_loop(self):
#         while True:
#             print("""\n---------------Contracts---------------\n
# \t1. Create new contract.\n\t2. Search contracts.\n\t3. Print all contracts.\n\t4. View contract.\n\t5. Edit contract.\n\t6. Delete contract.\n\t7. Main menu.""")
#             choice = input("\nEnter option: ")
#             if choice == "5":
#                 break
#             elif choice == "1":
#                 self.create_new_contract()
#             elif choice == "2":
#                 self.search_menu()
#             elif choice == "3":
#                 self.print_all_contracts()
#             elif choice == "4":
#                 self.view_contract_by_id()
#             elif choice == "5":
#                 pass
#             elif choice == "6":
#                 self.delete_contract()
                
#     def create_new_contract(self):
#         answer_list = []
#         question_list = ["Enter customers name: ", "Enter VIN number: ", "Enter start date(dd.mm.yy): ", "Enter end date(dd.mm.yy):", "Enter country: "]
#         print("Enter 'q' to cancel at any time")
#         for element in question_list:
#             answer = input(element)
#             if answer.lower() == 'q':
#                 break
#             answer_list.append(answer)
#         if len(answer_list) == 5:
#             self.logic.create_new_contract(answer_list)
#         else:
#             return

#     def search_contracts(self):
#         choice = input("")

#     def search_menu(self):                           #Gera snyrtilegra / Bæta vid no result
#         while True:
#             print("Search by: \n1.Customer name.\n2.VIN number\nType 'q' to return to main menu.")
#             choice = input("Enter option: ")
#             if choice.lower == 'q':
#                 return
#             elif choice == '1':
#                 name = input("Enter name to search for: ")
#                 result_list = self.logic.search_contracts_by_customer(name)
#                 if result_list:
#                     for result in result_list:
#                         print(result)
#             elif choice == '2':
#                 vin = input("Enter VIN to search for: ")
#                 result_list = self.logic.search_contracts_by_vin(vin)
#                 if result_list:
#                     for result in result_list:
#                         print(result)
    
#     def print_all_contracts(self):
#         for contract in (self.logic.all_contracts()):
#             print(contract)

#     def view_contract_by_id(self):
#         contract_id = input("Enter contract identification number: ")
#         contract = self.logic.search_contracts_by_id(contract_id)
#         if contract:
#             print(contract)
#         else:
#             print("Contract not found.")

#     def delete_contract(self):
#         contract_id = str(input("Enter the ID number of the contract you want to delete :"))
#         confirmation = self.logic.delete_contract(contract_id)
#         if confirmation == True:
#             print("Contract successfully deleted.")
#         else:
#             print("Contract not found.")

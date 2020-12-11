import os
from ui.VehicleUI import VehicleUI
from ui.CustomerUI import CustomerUI
from ui.ContractsUI import ContractUI
from ui.DestinationUI import destinationUI
from ui.EmployeeUI import EmployeeUI
from ui.InvoiceUI import InvoiceUI
from ui.ReportsUI import ReportUI
from logic.logicAPI import LogicAPI

class UIMain:
    promt_login = True

    def __init__(self):
        self.login()
        
        #Menu header
    def ui_menu_header(self, menu_name):
        print(" _   _       _   _            _      _ _                  ")
        print("| \ | |     | \ | |     /\   (_)    | (_)                 ")
        print("|  \| | __ _|  \| |    /  \   _ _ __| |_ _ __   ___  ___  ")
        print("| . ` |/ _` | . ` |   / /\ \ | | '__| | | '_ \ / _ \/ __| ")
        print("| |\  | (_| | |\  |  / ____ \| | |  | | | | | |  __/\__ \ ")
        print("|_| \_|\__,_|_| \_| /_/    \_\_|_|  |_|_|_| |_|\___||___/ ")
        print()
        print("-"*20 + f"{menu_name}" + "-"*20)

    #Menu footer
    def ui_menu_footer(self):
        print("-"*50)


    def login(self):
        self.ui_menu_header("Please Login")
        while self.promt_login == True:
            print('\nPress "q" to exit')
            print()
            # employee_id = input(">> Employee ID: ")
            # if employee_id == "q":
            #     break
            # password = input(">> Password: ")
            # employee_role = self.logic.check_password(employee_id, password)
            employee_role = "ADMIN"
            if employee_role == None:
                print("\n*** INVALID PASSWORD AND/OR USERNAME ***\n")
            else:
                if employee_role == "OFFICE":
                    self.office_ui_loop()
                elif employee_role == "AIRPORT":
                    self.airport_ui_loop()
                elif employee_role == "ADMIN":
                    self.admin_ui_loop()


    def admin_ui_loop(self):
        while True:
            self.ui_menu_header("Main Menu")
<<<<<<< HEAD
            print("\nSelect an option...\n1. Vehicles \n2. Customers \n3. Contracts \n4. Reports \n5. Destinations \n6. Employees \n7. Invoices \nq. Quit program\n")
=======
            print("\nSelect an option...\n1. Vehicles \n2. Customers \n3. Contracts \n4. Reports \n5. Destinations \n6. Employees \n7. Invoices \nq. to quit program\n")
>>>>>>> 5130f7688c176517a3963aebf75957d9ba69d240
            self.ui_menu_footer()
            command = input("Input your command: ")
            command = command.lower()
            if command == "1":
                self.vehicle = VehicleUI()
            elif command == "2":
                self.customer = CustomerUI()
            elif command == "3":
                self.contracts = ContractUI()
            elif command == "4":
                self.report = ReportUI()
            elif command == "5":
                self.destination = destinationUI()
            elif command == "6":            
                self.employee = EmployeeUI()
            elif command == '7':
                self.invoice = InvoiceUI()
            elif command == "q":
                self.promt_login = False
                return
            else:
                print("Invalid command, try again")
    
    def airport_ui_loop(self):
        while True:
            self.ui_menu_header("Main Menu")
            print("\nSelect an option...\n1. Vehicles \n2. Customers \nq. Quit program\n")
            self.ui_menu_footer()
            command = input("Input your command: ")
            command = command.lower()
            if command == "1":
                self.vehicle = VehicleUI()
            elif command == "2":
                self.customer = CustomerUI()
            elif command == "q":
                self.promt_login = False
                return
            else:
                print("Invalid command, try again")

    def office_ui_loop(self):
        while True:
            self.ui_menu_header("Main Menu")
            print("\nSelect an option...\n1. Contracts \n2. Reports \nq. Quit program\n")
            self.ui_menu_footer()
            command = input("Input your command: ")
            command = command.lower()
            if command == "1":
                self.contracts = ContractUI()
            elif command == "2":
                self.report = ReportUI()
            elif command == "q":
                self.promt_login = False
                return
            else:
                print("Invalid command, try again")


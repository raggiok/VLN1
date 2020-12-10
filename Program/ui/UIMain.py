import os
from ui.VehicleUI import VehicleUI
from ui.CustomerUI import CustomerUI
from ui.ContractsUI import ContractUI
from ui.DestinationUI import destinationUI
from ui.EmployeeUI import EmployeeUI

class UIMain:
    
    def __init__(self):
        self.ui_loop()
    

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

    def ui_loop(self):
        while True:
            self.ui_menu_header("Main Menu")
            print("\nSelect an option...\n1. Vehicles \n2. Customers \n3. Contracts \n4. Reports \n5. Destinations \n6. Employees \nq. to quit program\n")
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
                pass # Vantar reports
            elif command == "5":
                self.destination = destinationUI()
            elif command == "6":            
                self.employee = EmployeeUI()
            elif command == "q":
                break
            else:
                print("Invalid command, try again")


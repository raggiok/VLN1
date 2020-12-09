from logic.logicAPI import LogicAPI

class UIMain:
    def __init__(self):
        print("inside ui")
        self.logicAPI = LogicAPI()
        self.ui_loop()

    def ui_loop(self):
        while True:
            print("-"*20 + "Main Menu" + "-"*20)
            print("\nSelect an option...\n1 - Vehicles \n2 - Customers \n3 - Contracts \n4 - Reports \n5 - Destinations \n6 - Employees \nq - to quit program\n")
            print("-"*50)
            command = input("Input your command: ")
            command = command.lower()
            if command == "1":
                from ui.VehicleUI import VehicleUI
                VehicleUI.vehicle_menu(self)
            elif command == "2":
                CustomerUI.customer_menu()
            elif command == "3":
                self.ContractsUI.contracts_menu()
            elif command == "4":
                pass
            elif command == "5":
                self.destinationUI.destination_menu()
            elif command == "6":            
                pass
            elif command == "q":
                return False
            else:
                print("Invalid command, try again")

        #Menu header
    def ui_menu_header(self, menu_name):
        print("\n" + "-"*20 + f"{menu_name}" + "-"*20)

    #Menu footer
    def ui_menu_footer(self):
        print("\n" + "-"*50)
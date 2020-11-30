from logic.LogicMain import LogicMain

class UIMain:
    def __init__(self):
        print("inside ui")
        self.logic = LogicMain()
        self.ui_loop()

    def ui_loop(self):
        while True:
            print("\nSelect an option...\n1 - Print all employees \n2 - Get employees by role \nq - to quit program")
            command = input("Input your command: ")
            command = command.lower()
            if command == "1":
                results  = self.logic.all_employees()
                print("\nAll employees:")
                for employee in results:
                    print(employee)
            elif command == "2":
                role_str = input("Type role name: ")
                results = self.logic.employee_by_role(role_str)
                print("\nAll employees with role " + role_str + ": ")
                for employee in results:
                    print(employee)
            elif command == "q":
                return False
            else:
                print("Invalid command, try again")
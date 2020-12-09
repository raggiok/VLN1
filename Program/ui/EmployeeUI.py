from ui.UIMain import UIMain
from logic.logicAPI import LogicAPI
from models.Employee import Employee

class EmployeeUI:
    def __init__(self):
        self.logicAPI = LogicAPI()
        self.employee_menu()

    #unique_id,name,ssn,role,address,zip_code,city,country,home_phone,mobile_phone,email,state
    #create new employee
    def ui_new_employee(self):
        employeeFieldnames = ["name","ssn","role","address","zip_code", "city", "country","home_phone","mobile_phone","email"]
        inputList = []
        print("\nPress 'q' and hit 'enter' to cancel at any time.")
        print("\nPlease enter the following details to create a new employee:" )
        user_input = ""
        for field in employeeFieldnames:
            if user_input.lower() == "q":
                return self.employee_menu()
            user_input = input(f"Enter {field}: ")
            inputList.append(user_input)
        return inputList

    #Request new value from user
    def value_input(self):
        return input("Enter new value: ")

    #Creates the Edit menu layout and returns the employee Instance after edit
    def ui_edit_employee(self):
        employee = self.ui_employee_ID() #prints specific destination
        selection = ""
        while selection != "11":
            self.ui_print_edit_menu() #ask user what he would like to edit
            selection = self.ui_edit_input()
            if selection == "1":
                employee.name = self.value_input()
            elif selection == "2":
                employee.ssn = self.value_input()
            elif selection == "3":
                employee.role = self.value_input()
            elif selection == "4":
                employee.address = self.value_input()
            elif selection == "5":
                employee.zip_code = self.value_input()
            elif selection == "6":
                employee.city = self.value_input()
            elif selection == "7":
                employee.country = self.value_input()
            elif selection == "8":
                employee.home_phone = self.value_input()
            elif selection == "9":
                employee.mobile_phone = self.value_input()
            elif selection == "10":
                employee.email = self.value_input()
            elif selection == "11":
                return employee

    #Get input for edit menu
    def ui_edit_input(self):
        selection = input("\n>> Select option: ")
        return selection
    
    #unique_id	name	ssn	role	address	zip_code	city	country	home_phone	mobile_phone	email	state
    #Prints the employee Edit menu options
    def ui_print_edit_menu(self):
        '''Prints options for Edit menu and accepts input'''
        self.ui_menu_header("Edit employee")
        print("\nSelect field to edit:")
        print("1. Name")
        print("2. SSN")
        print("3. Role")
        print("4. Address")
        print("5. Zip_code")
        print("6. City")
        print("7. Country")
        print("8. Home_phone")
        print("9. Mobile_phone")
        print("10. Email")
        print("11. Exit")
        self.ui_menu_footer()

    def ui_delete_employee(self):
        employee = self.ui_employee_ID()
        choose = ""
        while choose != "3":
            self.ui_print_delete_menu()
            choose = self.ui_delete_input()
            if choose == "1":
                pass
            elif choose == "2":
                pass
            elif choose == "3":
                return employee
    
    #print delete input
    def ui_delete_input(self):
        choose = input("\n>> Select option: ")
        return choose

    #print delete menu
    def ui_print_delete_menu(self):
        '''Prints options for delete menu and accepts input'''
        self.ui_menu_header("Delete employee")
        print("\nSelect option to delete:")
        print("1. Yes")
        print("2. No")
        print("3. Exit")
        self.ui_menu_footer()

    #Print Employee Table Header
    def ui_employee_table_header(self):
        print(f"{'Unique_id':<20}{'Name':<20}{'SSN':<20}{'Role':<20}{'Address':<20}{'Zip_code':<20}{'City':<20}{'Country':<20}{'Home_phone':<20}{'Mobile_phone':<20}{'Email':<20}")
        print("-"*200)

    #Print employee Table Footer
    def ui_employee_table_footer(self):
        print("-"*200)
        print()

    #Prints all employee
    def ui_all_employee(self):
        results  = self.logicAPI.get_employees()
        print("\nAll employee:")
        self.ui_employee_table_header()
        for employee in results:
            print(employee)
        self.ui_employee_table_footer()
    
    #Prints employee with unique ID
    def ui_employee_ID(self):
        '''Prints a single employee with a unique ID'''
        employee_ID = input(">> Please enter employee ID: ")
        employee  = self.logicAPI.search_employee_by_ID(employee_ID)
        print("\nemployee by ID: " + employee_ID)
        self.ui_employee_table_header()
        print(employee) 
        self.ui_employee_table_footer()
        return employee

    #Prints employee name
    #def ui_employee_name(self):
    #    '''Prints a single employee name'''
    #    employee_name = input(">> Please enter employee name: ")
    #    employee  = self.logicAPI.search_employee_by_name(employee_name)
    #    print("\nemployee by name: " + employee_name)
    #    self.ui_employee_table_header()
    #    print(employee) 
    #    self.ui_employee_table_footer()
    #    return employee
    
    #Prints employee role
    def ui_employee_role(self):
        '''Prints a single employee role'''
        ui_employee_role = input(">> Please enter employee role: ")
        employee  = self.logicAPI.search_employee_by_role(employee_role)
        print("\nemployee by role: " + employee_role)
        self.ui_employee_table_header()
        print(employee) 
        self.ui_employee_table_footer()
        return employee

    #Menu header
    def ui_menu_header(self, menu_name):
        print("\n" + "-"*20 + f"{menu_name}" + "-"*20)

    #Menu footer
    def ui_menu_footer(self):
        print("\n" + "-"*50)


    #Prints the search menu for employee
    def ui_search_menu(self):
        self.ui_menu_header("Employee Search")
        print("\nPlease select a search option:")
        #self.UI_numbered_menu(["Name", "SSN", "Role", "Exit"])
        self.UI_numbered_menu([ "SSN", "Role", "Exit"])
        self.ui_menu_footer
        selection = input("\n>> Select option: ")
        #if selection == "1":
        #   emp_name = input(">> Please enter employee name: ")
        #    a_list = self.logic.customer_by_name(cust_name)
        #    self.ui_customer_table_header()
        #    for item in a_list:
        #       print(item)
        if selection == "1":
            emp_id = input(">> Please enter employee ID: ")
            a_list = self.logicAPI.search_employees_by_id(emp_id)
            self.ui_employee_table_header()
            for item in a_list:
                print(item)
        elif selection == "2":
            emp_role = input(">> Please enter employee role: ")
            a_list = self.logicAPI.search_employees_by_role(emp_role)
            self.ui_employee_table_header()
            for item in a_list:
                print(item)
        elif selection == "3":
            return EmployeeUI()
        else:
            print("Invalid command, try again")

    #Prints any UI menu in order
    def UI_numbered_menu(self, a_list):
        '''Takes a list as parameter and prints all the items of a list in an order from 1. list[0], 2. list[1] and so on'''
        for i in range(0,(len(a_list))):
            print(f"{i+1}. {a_list[i]}")

    #UNFINISHED
    #Prints the employee Main Menu
    def employee_menu(self):
        while True:
            self.ui_menu_header("Employee Menu")
            print("\nSelect an option...\n1. Create new employee \n2. Search employees  \n3. View all employees \n4. Edit employee \n5. Delete employee \n6. Main Menu")
            self.ui_menu_footer()
            command = input(">> Select option: ")
            command = command.lower()
            if command == "1":
                new_employee = self.ui_new_employee()
                self.logicAPI.create_employee(new_employee)
            elif command == "2":
                selection = self.ui_search_menu()
            elif command == "3":
                self.ui_all_employee()
            elif command == "4":
                new_employee = self.ui_edit_employee()
                self.logicAPI.update_employee(new_employee)
            elif command == "5":
                pass
            elif command == "6":
                return UIMain()
            else:
                print("Invalid command, try again") 

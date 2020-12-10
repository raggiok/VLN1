from logic.logicAPI import LogicAPI
from models.Employee import Employee

class EmployeeUI:
    def __init__(self):
        self.logicAPI = LogicAPI()
        self.employee_menu()

    #unique_id,name,ssn,role,address,zip_code,city,country,home_phone,mobile_phone,email,state
    #create new employee
    def ui_new_employee(self):
        employeeFieldnames = ["Name", "Social security number", "Role", "Address", "Zip Code", "City", "Country", "Home phone", "Mobile phone", "Email"]
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
        employee = self.ui_single_employee_unique() #prints specific employee
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
    
    #Prints customer with unique ID
    def ui_single_employee_unique(self):
        '''Prints a single customer with a unique ID'''
        employee_unique = input(">> Please enter employee ID: ")
        employees = self.logicAPI.search_employee_by_unique(employee_unique)
        print("\ncustomer by ID: " + employee_unique)
        self.ui_employee_table_header()
        for employee in employees:
            print(employee) 
        self.ui_employee_table_footer()
        return employee

    #name	ssn	role	address	zip_code	city	country	home_phone	mobile_phone	email	state
    ###availability option search ###
    def ui_name_available_print(self):
        '''Prints all employee name'''
        print("\nAvailable Options:")
        employees = self.logicAPI.available_name()
        for employee in employees:
            print("\t" + employee)
        print()

    def ui_ssn_available_print(self):
        '''Prints all customer SSN'''
        print("\nAvailable Options:")
        employees = self.logicAPI.available_ssn()
        for employee in employees:
            print("\t" + employee)
        print()
    
    def ui_role_available_print(self):
        '''Prints all employee role'''
        print("\nAvailable Options:")
        employees = self.logicAPI.available_role()
        for employee in employees:
            print("\t" + employee)
        print()

    def ui_address_available_print(self):
        '''Prints all employee address'''
        print("\nAvailable Options:")
        employees = self.logicAPI.available_address()
        for employee in employees:
            print("\t" + employee)
        print()

    def ui_zip_code_available_print(self):
        '''Prints all employee zip_code'''
        print("\nAvailable Options:")
        employees = self.logicAPI.available_zip_code()
        for employee in employees:
            print("\t" + employee)
        print()
    
    def ui_city_available_print(self):
        '''Prints all employee city'''
        print("\nAvailable Options:")
        employees = self.logicAPI.available_city()
        for employee in employees:
            print("\t" + employee)
        print()
    
    def ui_country_available_print(self):
        '''Prints all employee country'''
        print("\nAvailable Options:")
        employees = self.logicAPI.available_country()
        for employee in employees:
            print("\t" + employee)
        print()

    #name	ssn	role	address	zip_code	city	country	
    #Print the availability data
    def ui_print_country(self):
        self.ui_country_available_print()
        country = input(">> Please enter employee Country: ")
        results  = self.logicAPI.search_employees_by_country(country)
        print("\nSearch results for " + country + ": ")
        self.ui_employee_table_header()
        for employee in results:
            print(employee)
        self.ui_employee_table_footer()

    def ui_print_city(self):
        self.ui_city_available_print()
        city = input(">> Please enter employee City: ")
        results  = self.logicAPI.search_employees_by_city(city)
        print("\nSearch results for " + city + ": ")
        self.ui_employee_table_header()
        for employee in results:
            print(employee)
        self.ui_employee_table_footer()

    def ui_print_zip_code(self):
        self.ui_zip_code_available_print()
        zip_code = input(">> Please enter employee zip_code: ")
        results  = self.logicAPI.search_employees_by_zip_code(zip_code)
        print("\nSearch results for " + zip_code + ": ")
        self.ui_employee_table_header()
        for employee in results:
            print(employee)
        self.ui_employee_table_footer()

    def ui_print_address(self):
        self.ui_address_available_print()
        address = input(">> Please enter employee address: ")
        results  = self.logicAPI.search_employees_by_address(address)
        print("\nSearch results for " + address + ": ")
        self.ui_employee_table_header()
        for employee in results:
            print(employee)
        self.ui_employee_table_footer()

    def ui_print_role(self):
        self.ui_role_available_print()
        role = input(">> Please enter employee role: ")
        results  = self.logicAPI.search_employees_by_role(role)
        print("\nSearch results for " + role + ": ")
        self.ui_employee_table_header()
        for employee in results:
            print(employee)
        self.ui_employee_table_footer()

    def ui_print_ssn(self):
        self.ui_ssn_available_print()
        ssn = input(">> Please enter employee ssn: ")
        results  = self.logicAPI.search_employees_by_id(ssn)
        print("\nSearch results for " + ssn + ": ")
        self.ui_employee_table_header()
        for employee in results:
            print(employee)
        self.ui_employee_table_footer() 

    def ui_print_name(self):
        self.ui_name_available_print()
        name = input(">> Please enter employee name: ")
        results  = self.logicAPI.search_employees_by_name(name)
        print("\nSearch results for " + name + ": ")
        self.ui_employee_table_header()
        for employee in results:
            print(employee)
        self.ui_employee_table_footer()

    #Menu header
    def ui_menu_header(self, menu_name):
        print("\n" + "-"*20 + f"{menu_name}" + "-"*20)

    #Menu footer
    def ui_menu_footer(self):
        print("\n" + "-"*50)

    #name	ssn	role	address	zip_code	city	country
    #Prints the search menu for employee
    def ui_search_menu(self):
        self.ui_menu_header("Employee Search")
        print("\nPlease select a search option:")
        self.UI_numbered_menu(["Name", "Social Security Number", "Role", "Address", "Zip Code", "City", "Country", "Exit"])
        #self.UI_numbered_menu([ "ID", "Role", "Exit"])
        self.ui_menu_footer()
        selection = input("\n>> Select option: ").lower()
        return selection

    #Prints any UI menu in order
    def UI_numbered_menu(self, a_list):
        '''Takes a list as parameter and prints all the items of a list in an order from 1. list[0], 2. list[1] and so on'''
        for i in range(0,(len(a_list))):
            print(f"{i+1}. {a_list[i]}")

    #name	ssn	role	address	zip_code	city	country
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
                if selection == "1":
                    self.ui_print_name()
                elif selection == "2":
                    self.ui_print_ssn()
                elif selection == "3":
                    self.ui_print_role()
                elif selection == "4":
                    self.ui_print_address()
                elif selection == "5":
                    self.ui_print_zip_code()
                elif selection == "6":
                    self.ui_print_city()
                elif selection == "7":
                    self.ui_print_country()
                elif selection == "8":
                    self.ui_employee_menu()    
            elif command == "3":
                self.ui_all_employee()
            elif command == "4":
                new_employee = self.ui_edit_employee()
                self.logicAPI.update_employee(new_employee)
            elif command == "5":
                self.ui_all_employee()
                employee_id = input(">> Enter employee ID to delete: ")
                employee = self.logicAPI.delete_employee(employee_id)
                for result in employee:
                    print(result)
            elif command == "6":
                return
            else:
                print("Invalid command, try again") 

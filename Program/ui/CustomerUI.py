from logic.logicAPI import LogicAPI
from models.Customers import Customer

class CustomerUI:
    def __init__(self):
        self.logicAPI = LogicAPI()
        self.customer_menu()

    #unique_id,name,ssn,address,zip_code,city,country,phone,email,state
    #create new customer
    def ui_new_customer(self):
        customerFieldnames = ["name","ssn","address","zip_code","city","country","phone","email"]
        inputList = []
        print("\nPress 'q' and hit 'enter' to cancel at any time.")
        print("\nPlease enter the following details to create a new customer:" )
        user_input = ""
        for field in customerFieldnames:
            if user_input.lower() == "q":
                return self.customer_menu()
            user_input = input(f"Enter {field}: ")
            inputList.append(user_input)
        return inputList

     #choose the number to edit 
    def value_input(self):
        return input("Enter new value: ")

    
    #unique_id,name,ssn,address,zip_code,city,country,phone,email,state
    #Creates the Edit menu layout and returns the customer Instance after edit
    def ui_edit_customer(self):
        customer = self.ui_single_customer_unique() #prints specific customer
        selection = ""
        while selection != "9":
            self.ui_print_edit_menu() 
            selection = self.ui_edit_input()
            if selection == "1":
                customer.name = self.value_input()
            elif selection == "2":
                customer.ssn = self.value_input()
            elif selection == "3":
                customer.address = self.value_input()
            elif selection == "4":
                customer.zip_code = self.value_input()
            elif selection == "5":
                customer.city = self.value_input()
            elif selection == "6":
                customer.country = self.value_input()
            elif selection == "7":
                customer.phone = self.value_input()
            elif selection =="8":
                customer.email = self.value_input()
            elif selection == "9":
                return customer
            

    #Get input for edit menu
    def ui_edit_input(self):
        selection = input("\n>> Select option: ")
        return selection
    
    #unique_id,name,ssn,address,zip_code,city,country,phone,email,state
    #Prints the Customer Edit menu options
    def ui_print_edit_menu(self):
        '''Prints options for Edit menu and accepts input'''
        self.ui_menu_header("Edit customer")
        print("\nSelect field to edit:")
        print("1. Name")
        print("2. Social Security No.")
        print("3. Address")
        print("4. Zip code")
        print("5. City")
        print("6. Country")
        print("7. Phone")
        print("8. Email")
        print("9. Exit")
        self.ui_menu_footer()

    #name,ssn,address,zip_code,city,country,phone,email,state
    #Print Customer Table Header
    def ui_customer_table_header(self):
        print(f"{'Customer ID':<20}{'Name':<20}{'SSN':<20}{'Address':<20}{'Zip code':<20}{'City':<20}{'Country':<20}{'Phone':<20}{'Email':<20}")
        print("-"*200)
    
    #Print Customer Table Footer
    def ui_customer_table_footer(self):
        print("-"*200)
        print()

    #Print all customer
    def ui_all_customer(self):
        results  = self.logicAPI.all_customer()
        print("\nAll customers:")
        self.ui_customer_table_header()
        for customer in results:
            print(customer)
        self.ui_customer_table_footer()

    #Prints customer with unique ID
    def ui_single_customer_unique(self):
        '''Prints a single customer with a unique ID'''
        customer_unique = input(">> Please enter customer ID: ")
        customers = self.logicAPI.search_customer_by_unique(customer_unique)
        print("\ncustomer by ID: " + customer_unique)
        self.ui_customer_table_header()
        for customer in customers:
            print(customer) 
        self.ui_customer_table_footer()
        return customer

    #name,ssn,address,zip_code,city,country
    ###availability option search ###
    def ui_name_available_print(self):
        '''Prints all customer name'''
        print("\nAvailable Options:")
        customers = self.logicAPI.available_customer_name()
        for customer in customers:
            print("\t" + customer)
        print()

    def ui_ssn_available_print(self):
        '''Prints all customer SSN'''
        print("\nAvailable Options:")
        customers = self.logicAPI.available_customer_ssn()
        for customer in customers:
            print("\t" + customer)
        print()

    def ui_address_available_print(self):
        '''Prints all customer address'''
        print("\nAvailable Options:")
        customers = self.logicAPI.available_customer_address()
        for customer in customers:
            print("\t" + customer)
        print()

    def ui_zip_code_available_print(self):
        '''Prints all customer zip_code'''
        print("\nAvailable Options:")
        customers = self.logicAPI.available_customer_zip_code()
        for customer in customers:
            print("\t" + customer)
        print()
    
    def ui_city_available_print(self):
        '''Prints all customer city'''
        print("\nAvailable Options:")
        customers = self.logicAPI.available_customer_city()
        for customer in customers:
            print("\t" + customer)
        print()
    
    def ui_country_available_print(self):
        '''Prints all customer country'''
        print("\nAvailable Options:")
        customers = self.logicAPI.available_customer_country()
        for customer in customers:
            print("\t" + customer)
        print()

    #name,ssn,address,zip_code,city,country
    #Print the availability data
    def ui_print_country(self):
        self.ui_country_available_print()
        country = input(">> Please enter customer Country: ")
        results  = self.logicAPI.search_customers_by_country(country)
        print("\nSearch results for " + country + ": ")
        self.ui_customer_table_header()
        for customer in results:
            print(customer)
        self.ui_customer_table_footer()

    def ui_print_city(self):
        self.ui_city_available_print()
        city = input(">> Please enter customer City: ")
        results  = self.logicAPI.search_customers_by_city(city)
        print("\nSearch results for " + city + ": ")
        self.ui_customer_table_header()
        for customer in results:
            print(customer)
        self.ui_customer_table_footer()

    def ui_print_zip_code(self):
        self.ui_zip_code_available_print()
        zip_code = input(">> Please enter customer zip_code: ")
        results  = self.logicAPI.search_customers_by_zip_code(zip_code)
        print("\nSearch results for " + zip_code + ": ")
        self.ui_customer_table_header()
        for customer in results:
            print(customer)
        self.ui_customer_table_footer()

    def ui_print_address(self):
        self.ui_address_available_print()
        address = input(">> Please enter customer address: ")
        results  = self.logicAPI.search_customers_by_address(address)
        print("\nSearch results for " + address + ": ")
        self.ui_customer_table_header()
        for customer in results:
            print(customer)
        self.ui_customer_table_footer()

    def ui_print_ssn(self):
        self.ui_ssn_available_print()
        ssn = input(">> Please enter customer ssn: ")
        results  = self.logicAPI.search_customers_by_id(ssn)
        print("\nSearch results for " + ssn + ": ")
        self.ui_customer_table_header()
        for customer in results:
            print(customer)
        self.ui_customer_table_footer() 

    def ui_print_name(self):
        self.ui_name_available_print()
        name = input(">> Please enter customer name: ")
        results  = self.logicAPI.search_customers_by_name(name)
        print("\nSearch results for " + name + ": ")
        self.ui_customer_table_header()
        for customer in results:
            print(customer)
        self.ui_customer_table_footer()

    #Menu header
    def ui_menu_header(self, menu_name):
        print("\n" + "-"*20 + f"{menu_name}" + "-"*20)

    #Menu footer
    def ui_menu_footer(self):
        print("\n" + "-"*50)
    

    #Print search menu 
    def ui_search_menu(self):
        self.ui_menu_header("Customer Search") 
        print("\nPlease enter search option:")
        self.UI_numbered_menu(["Name", "Social Security No.", "Address", "Zip Code", "City",  "Country", "Exit"])
        self.ui_menu_footer()
        selection = input("\n>> Select option: ").lower()
        return selection


    #Prints any UI menu in order
    def UI_numbered_menu(self,a_list):
        '''Takes a list as parameter and prints all the items of a list in an order from 1. list[0], 2. list[1] and so on'''
        for i in range(0,(len(a_list))):
            print(f"{i+1}. {a_list[i]}") 

    #name	ssn	address	zip_code	city	country
    #Print customer main menu
    def customer_menu(self):
        while True:
            self.ui_menu_header("Customer Menu")
            print("\nSelect an option...\n1. Create new customer \n2. Search customer \n3. View all customers \n4. Edit customer \n5. Delete customer \n6. Main menu ")   
            self.ui_menu_footer()      
            command = input(">> Select option: ").lower()
            command = command.lower()
            if command == "1":
                new_customer = self.ui_new_customer()
                self.logicAPI.create_customer(new_customer)
            elif command == "2":
                selection = self.ui_search_menu()
                if selection == "1":
                    self.ui_print_name()
                elif selection == "2":
                    self.ui_print_ssn()
                elif selection == "3":
                    self.ui_print_address()
                elif selection == "4":
                    self.ui_print_zip_code()
                elif selection == "5":
                    self.ui_print_city()
                elif selection == "6":
                    self.ui_print_country()
                elif selection == "7":
                    self.customer_menu()
            elif command == "3":
                self.ui_all_customer()
            elif command == "4": 
                new_customer = self.ui_edit_customer()
                self.logicAPI.update_customer(new_customer)
            elif command == "5":
                customer_id = input(">> Enter customer ID to delete: ")
                customer = self.logicAPI.delete_customer(customer_id)
                for result in customer:
                    print(result)
            elif command == "6":
                return
            else:
                print("Invalid command, try again")




   

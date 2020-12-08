from ui.UIMain import UIMain
from logic.logicAPI import LogicAPI
from models.Customers import Customers

class CustomerUI:
    def __init__(self):
        self.logicAPI = LogicAPI()
        self.customer_menu()

    #unique_id,name,ssn,address,zip_code,city,country,phone,email,state
    #create new customer
    def ui_new_customer(self):
        customerFieldnames = ["unique_id","name","ssn","address","zip_code","city","country","phone","email"]
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

    #Menu header
    def ui_menu_header(self, menu_name):
        print("\n" + "-"*20 + f"{menu_name}" + "-"*20)

    #Menu footer
    def ui_menu_footer(self):
        print("\n" + "-"*50)
    

    #Prints any UI menu in order
    def UI_numbered_menu(self,a_list):
        '''Takes a list as parameter and prints all the items of a list in an order from 1. list[0], 2. list[1] and so on'''
        for i in range(0,(len(a_list))):
            print(f"{i+1}. {a_list[i]}")  

    #Print search menu 
    def ui_search_menu(self):
        self.ui_menu_header("Customer Search") 
        print("\nPlease enter search option:")
        self.UI_numbered_menu(["Name", "SSN", "Country", "Exit"])
        self.ui_menu_footer()
        selection = input("\n>> Select option: ").lower()
        if selection == "1":
            cust_name = input(">> Please enter customer name: ")
            a_list = self.logic.customer_by_name(cust_name)
            self.ui_customer_table_header()
            for item in a_list:
                print(item)
        elif selection == "2":
            cust_id = input(">> Please enter customer ID: ")
            a_list = self.logic.customer_by_ssn(cust_id)
            self.ui_customer_table_header()
            for item in a_list:
                print(item)
        elif selection == "3":
            cust_country = input(">> Please enter customer country: ")
            a_list = self.logic.customer_by_area(cust_country)
            self.ui_customer_table_header()
            for item in a_list:
                print(item)
        elif selection == "4":
            return CustomerUI()
        else:
            print("Invalid command, try again")


    #UNFINISHED
    #Print customer main menu
    def customer_menu(self):
        while True:
            self.ui_menu_header("Customer Menu")
            print("\nSelect an option...\n1. Create new customer \n2. Search customer \n3. View all customers \n4. Edit customer information \n5. Delete customer information \n6. Main menu\n ")   
            self.ui_menu_footer()      
            command = input(">> Select option: ")
            command = command.lower()
            if command == "1":
                new_customer = self.ui_new_customer()
                self.logic.create_customer(*new_customer)
            elif command == "2":
                choice = self.ui_search_menu()
            elif command == "3":
                return self.ui_all_customer()
            elif command == "4": 
                new_customer = self.ui_edit_customer()
                self.logicAPI.edit_customer(new_customer)
            elif command == "5":
                new_customer = self.ui_delete_customer()
                self.logicAPI.delete_customer(new_customer)
            elif command == "6":
                return UIMain() 
            else:
                print("Invalid command, try again")

    ##unique_id,name,ssn,address,zip_code,city,country,phone,email,state
    #Print Customer Table Header
    def ui_customer_table_header(self):
        print(f"{'Name':<20}{'SSN':<20}{'Address':<20}{'Zip_code':<20}{'City':<20}{'Country':<20}{'Phone':<20}{'Email':<20}")
        print("-"*200)
    
    #Print Customer Table Footer
    def ui_customer_table_footer(self):
        print("-"*200)
        print()

    #Print all customer
    def ui_all_customer(self):
        for customer in self.logicAPI.all_customer():
            print("\n All customers:")
            self.ui_customer_table_header()
            for customer in result:
                print(customer)
            self.ui_customer_table_footer()

    #Print customer by ID
    def ui_by_id(self):
        "allowing search by ID only"
        customer_ID = input(">> Please enter SSN: ")
        customer = self.logicAPI.customer_by_ssn(customer_ID)
        print("\nCustomer by SSN: " + customer_ID)
        self.ui.ui_customer_table_header
        print(customer)
        self.ui_customer_table_footer
        return customer

    #Print customer by name
    def ui_by_name(self):
        "allowing search by name only"
        customer_name = input(">> Please enter name of customer: ")
        customer = self.logicAPI.customer_by_name(customer_name)
        print("\nCustomer by name: " + customer_name)
        self.ui.ui_customer_table_header
        print(customer)
        self.ui_customer_table_footer
        return customer    
    
    #Print customer by area
    def ui_by_area(self):
        "allowing search by area only"
        customer_area = input(">> Please enter area of customer: ")
        customer = self.logicAPI.customer_by_area(customer_area)
        print("\nCustomer by area: " + customer_area)
        self.ui.ui_customer_table_header
        print(customer)
        self.ui_customer_table_footer
        return customer   

     #choose the number to edit 
    def value_input(self):
        return input("Enter new value: ")

    
    #unique_id,name,ssn,address,zip_code,city,country,phone,email,state
    #Creates the Edit menu layout and returns the customer Instance after edit
    def ui_edit_customer(self):
        customer = self.ui_by_ID() #prints specific customer
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
        print("2. SSN")
        print("3. Address")
        print("4. Zip_code")
        print("5. City")
        print("6. Country")
        print("7. Phone")
        print("8. Email")
        print("9. Exit")
        self.ui_menu_footer()

    def ui_delete_customer(self):
        customer = self.ui_by_id()
        choose = ""
        while choose != "3":
            self.ui_print_delete_menu()
            choose = self.ui_delete_input()
            if choose == "1":
                pass
            elif choose == "2":
                pass
            elif choose == "3":
                return customer
    
    #print delete input
    def ui_delete_input(self):
        choose = input("\n>> Select option: ")
        return choose

    #print delete menu
    def ui_print_delete_menu(self):
         '''Prints options for delete menu and accepts input'''
         self.ui_menu_header("Delete customer")
         print("\nSelect option to delete:")
         print("1. Yes")
         print("2. No")
         print("3. Exit")
         self.ui_menu_footer()

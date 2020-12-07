from ui.UIMain import UIMain
from logic.CustomerLogic import CustomerLogic
from models.Customer import Customer

class CustomerUI:
    def __init__(self):
        self.logic = CustomerLogic()
        self.customer_menu()

    #create new customer
    def ui_new_customer(self):
        customerFieldnames = ["name","ssn","address","postnumber","phone","email","land"]
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
        self.ui_menu_footer
        selection = input("\n>> Select option: ")
        return selection

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
                self.logic.create_customer(new_customer)
            elif command == "2":
                choice = self.ui_search_menu()
                if choice == "1":
                    return self.logic.customer_by_name()
                    edit_delete = self.ui_edit_delete_menu() 
                elif choice == "2":
                    return self.logic.customer_by_ssn()
                elif choice == "3":
                    return self.logic.customer_by_area()
                elif choice == "4":
                    return CustomerUI()
            elif command == "3":
                return self.ui_all_customer()
            elif command == "4": #Edit
                pass
            elif command == "5":

            elif command == "6":
                return UIMain() 
            else:
                print("Invalid command, try again")

    #name,ssn,address,postnumber,phone,email,land 
    #Print Customer Table Header
    def ui_customer_table_header(self):
        print(f"{'Name':<20}{'SSN':<20}{'Address':<20}{'Post Number':<20}{'Phone':<20}{'Email':<20}{'Color':<20}{'Country':<20}")
        print("-"*200)
    
    #Print Customer Table Footer
    def ui_customer_table_footer(self):
        print("-"*200)
        print()

    #Print all customer
    def ui_all_customer(self):
        for customer in self.logic.all_customer():
            print("\n All customers:")
            self.ui_customer_table_header()
            for customer in result:
                print(customer)
            self.ui_customer_table_footer()

    #Print customer by ID
    def ui_by_id(self):
        "allowing search by ID only"
        customer_ID = input(">> Please enter SSN: ")
        customer = self.customer.customer_by_ssn(customer_ID)
        print("\nCustomer by SSN: " + customer_ID)
        self.ui.ui_customer_table_header
        print(customer)
        self.ui_customer_table_footer
        return customer

    #Print customer by name
    def ui_by_name(self):
        "allowing search by name only"
        customer_name = input(">> Please enter name of customer: ")
        customer = self.customer.customer_by_name(customer_name)
        print("\nCustomer by name: " + customer_name)
        self.ui.ui_customer_table_header
        print(customer)
        self.ui_customer_table_footer
        return customer    
    
    #Print customer by area
    def ui_by_area(self):
        "allowing search by area only"
        customer_area = input(">> Please enter area of customer: ")
        customer = self.customer.customer_by_area(customer_area)
        print("\nCustomer by area: " + customer_area)
        self.ui.ui_customer_table_header
        print(customer)
        self.ui_customer_table_footer
        return customer   

     #choose the number to edit 
    def value_input(self):
        return input("Enter new value: ")

    #UNFINISHED
    #Creates the Edit menu layout and returns the customer Instance after edit
    def ui_edit_customer(self):
        customer = self.ui_by_ID() #prints specific customer
        selection = ""
        while selection != "9":
            self.ui_print_edit_menu() 
            selection = self.ui_edit_input()
            if selection == "1":
                vehicle.manufacturer = self.value_input()
            elif selection == "2":
                vehicle.model = self.value_input()
            elif selection == "3":
                vehicle.vehicle_type = self.value_input()
            elif selection == "4":
                vehicle.status = self.value_input()
            elif selection == "5":
                vehicle.man_year = self.value_input()
            elif selection == "6":
                vehicle.color = self.value_input()
            elif selection == "7":
                vehicle.license_type = self.value_input()
            elif selection == "8":
                vehicle.location = self.value_input()
            elif selection == "9":
                customer.location
            elif selection == "10":
                return customer

    #Get input for edit menu
    def ui_edit_input(self):
        selection = input("\n>> Select option: ")
        return selection
    
    #UNFINISHED
    #Prints the Customer Edit menu options
    def ui_print_edit_menu(self):
        '''Prints options for Edit menu and accepts input'''
        self.ui_menu_header("Edit customer")
        print("\nSelect field to edit:")
        print("1. Name")
        print("2. SSN")
        print("3. Phone Number")
        print("4. Mobile Number")
        print("5. E-mail Address")
        print("6. Address")
        print("7. Country")
        print("8. Credit Card Number")
        print("9. Status")
        print("10. Exit")
        self.ui_menu_footer()

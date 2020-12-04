from ui.UIMain import UIMain
from logic.CustomerLogic import CustomerLogic

class CustomerUI:
    def __init__(self):
        print ("Ui cal")
        self.logic = CustomerLogic()
        self.customer_menu()

    #create new customer
    def ui_new_customer(self):
        customerheader = ["name","ssn","address","postnumber","phone","email","land"]
        answer = []
        print("\nPress 'q' and hit 'enter' to cancel at any time.")
        print("\nPlease enter the following details to create a new customer:" )
        user_answer = ""
        for header in customerheader:
            if user_answer.lower() == "q":
                return self.customer_menu()
            user_answer = input(f"Enter {header}: ")
            answer.append(user_answer)
        return answer
    
    #Print all customer
    def ui_all_customer(self):
        for customer in self.logic.all_customer():
            print(customer)

    #Print search menu 
    def ui_search_menu(self):
        print("-"*20 + "Customer" + "-"*20) 
        print("\nPlease enter search option:")
        print("1. Name")
        print("2. SSN")
        print("3. Country")
        print("4. Exit")
        print("-"*50) 
        choice = input("\n>> Select option: ")
        return choice

    def ui_edit_delete_menu(self):
        print("1. Edit")
        print("2. Delete")
        print("3. Return")
        option = input("\n>> Select option: ")
        return option
         

    #Print customer main menu
    def customer_menu(self):
        while True:
            print("-"*20 + "Customer" + "-"*20)
            print("\nSelect an option...\n1. Create new customer \n2. Search customer \n3. View all customers \n4. Main menu\n ")   
            print("-"*50)      
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
            elif command == "4":
                return UIMain() 
            else:
                print("Invalid command, try again")

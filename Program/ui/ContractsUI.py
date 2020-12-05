from logic.ContractsLogic import ContractLogic
from models.contracts import Contract

class ContractUI:
    def __init__(self):
        self.logic = ContractLogic()
        self.contract_ui_loop()

    def contract_ui_loop(self):
        while True:
            print("""\n---------------Contracts---------------\n
\t1. Create new contract.\n\t2. Search contracts.\n\t3. Print all contracts.\n\t4. View contract.\n\t5. Edit contract.\n\t6. Delete contract.\n\t7. Main menu.""")
            choice = input("\nEnter option: ")
            if choice == "5":
                break
            elif choice == "1":
                self.create_new_contract()
            elif choice == "2":
                self.search_menu()
            elif choice == "3":
                self.print_all_contracts()
            elif choice == "4":
                self.view_contract_by_id()
            elif choice == "5":
                pass
            elif choice == "6":
                self.delete_contract()
                
    def create_new_contract(self):
        answer_list = []
        question_list = ["Enter customers name: ", "Enter VIN number: ", "Enter start date(dd.mm.yy): ", "Enter end date(dd.mm.yy):", "Enter country: "]
        print("Enter 'q' to cancel at any time")
        for element in question_list:
            answer = input(element)
            if answer.lower() == 'q':
                break
            answer_list.append(answer)
        if len(answer_list) == 5:
            self.logic.create_new_contract(answer_list)
        else:
            return

    def search_contracts(self):
        choice = input("")

    def search_menu(self):                           #Gera snyrtilegra / Bæta vid no result
        while True:
            print("Search by: \n1.Customer name.\n2.VIN number\nType 'q' to return to main menu.")
            choice = input("Enter option: ")
            if choice.lower == 'q':
                return
            elif choice == '1':
                name = input("Enter name to search for: ")
                result_list = self.logic.search_contracts_by_customer(name)
                if result_list:
                    for result in result_list:
                        print(result)
            elif choice == '2':
                vin = input("Enter VIN to search for: ")
                result_list = self.logic.search_contracts_by_vin(vin)
                if result_list:
                    for result in result_list:
                        print(result)
    
    def print_all_contracts(self):
        for contract in (self.logic.all_contracts()):
            print(contract)

    def view_contract_by_id(self):
        contract_id = input("Enter contract identification number: ")
        contract = self.logic.search_contracts_by_id(contract_id)
        if contract:
            print(contract)
        else:
            print("Contract not found.")

    def delete_contract(self):
        contract_id = str(input("Enter the ID number of the contract you want to delete :"))
        confirmation = self.logic.delete_contract(contract_id)
        if confirmation == True:
            print("Contract successfully deleted.")
        else:
            print("Contract not found.")

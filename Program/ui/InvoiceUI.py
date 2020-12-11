from csv import unix_dialect
from logic.logicAPI import LogicAPI
from models.Invoice import Invoice
from ui.ContractsUI import ContractUI

class InvoiceUI:

    def __init__(self):
        self.logic = LogicAPI()
        self.invoice_menu()

    #Menu header
    def ui_menu_header(self, menu_name):
        print("\n" + "-"*20 + f"{menu_name}" + "-"*20)

    #Menu footer
    def ui_menu_footer(self):
        print("\n" + "-"*53)

    def print_select_option(self):
        return input(">> Select option: ").lower()
    
    def print_table_header(self):
        print()
        print(f'{"Invoice ID":<20}{"Contract ID":<20}{"Customer SSN":<20}{"Vehicle ID":<20}{"Rate(€)":<20}{"Days total":<20}{"Total price(€)":<20}{"Late fee(€)":<20}{"State":<20}')
        print("="*180)

    #Print Contract Table Footer
    def print_table_footer(self):
        print("-"*180)
        print()

    def invoice_menu(self):
        while True:
            self.ui_menu_header("Invoice Menu")
            self.ui_numbered_menu(["Print invoice list", "Search for invoice by unique ID", "Send invoice", "Mark invoice as payed", "Main menu"])
            self.ui_menu_footer()
            choice = self.print_select_option()
            if choice == '1':
                self.print_table_header()
                for i in self.logic.get_all_invoices():
                    print(i)
                self.print_table_footer()
            elif choice == '2':
                id_invoice = input(">> Enter invoice ID: ")
                self.print_table_header()
                for i in self.logic.search_invoices(id_invoice):
                    print(i)
            elif choice == '3':
                invoice_ID = input(">> Enter contract ID: ")
                print(self.logic.create_invoice(invoice_ID))
            elif choice == '4':
                id_invoice = input(">> Enter invoice ID: ")
                print(self.logic.set_invoice_to_payed(id_invoice))
            elif choice == '5':
                return
            else:
                print('Invalid command, try again.')


    #Prints any UI menu in numbered list
    def ui_numbered_menu(self, a_list):
        '''Takes a list as parameter and prints all the items of a list in an order from 1. list[0], 2. list[1] and so on'''
        for i in range(0,(len(a_list))):
            print(f"{i+1}. {a_list[i]}")
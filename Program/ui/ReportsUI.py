from logic.logicAPI import LogicAPI
from ui.GeneralUI import GeneralUI
from models.contracts import Contract

class ReportUI:

    def __init__(self):
        self.general = GeneralUI()
        self.logic = LogicAPI()
        self.report_main_menu()

    def ui_menu_header(self, menu_name):
        print("\n" + "-"*20 + f"{menu_name}" + "-"*20)

    def ui_menu_footer(self):
        print("\n" + "-"*50)

    #Prints any UI menu in numbered list
    def ui_numbered_menu(self, a_list):
        '''Takes a list as parameter and prints all the items of a list in an order from 1. list[0], 2. list[1] and so on'''
        for i in range(0,(len(a_list))):
            print(f"{i+1}. {a_list[i]}")

    def print_select_option(self):
        return input(">> Select option: ").lower()
    
    def contract_table_header(self):
        print()
        print(f'{"Contract ID":<20}{"Customer Name":<20}{"Customer SSN":<20}{"Vehicle ID":<20}{"Contract Duration":<31}{"Country":<20}{"Employee":<20}{"Total price":<20}{"Creation Date":<20}{"Check-out Date":<20}{"Check-in Date":<20}{"Check-in Location":<20}{"State":<20}')
        print("="*260)
    
    def print_table_footer(self):
        print("-"*60)
        print()

    def revenue_table_header(self):
        print()
        print(f'{"Date":<20}{"Location":<20}{"Revenue(€)":<20}')
        print("="*60)

    #Print Vehicle Table Header
    def utility_table_header(self):
        print(f"{'Location':<40}{'Vehicle Type':<40}{'Days rented in a year (%)':<50}")
        print("-"*100)
    
    def utility_table_footer(self):
        print("-"*100)
    
    ### CONTRACT MAIN MENU ###
    def report_main_menu(self):
        while True:
            self.ui_menu_header("Reports")
            print("\nPlease select a an option:")
            self.ui_numbered_menu(["Revenues", "Vehicle Usability", "Main Menu"])
            self.ui_menu_footer()
            command = self.print_select_option()
            if command == "1":
                start_date = input(">> Input start date in format dd.mm.yy: ")
                end_date = input(">> Input end date in format dd.mm.yy: ")
                self.revenue_statistics(start_date, end_date)
            elif command == "2": # 2. Vehicle usability
                result_dict = self.logic.result_list()
                self.utility_table_header()
                for key,val in result_dict.items():
                    print(f"{key}")
                    for k,v in val.items():
                        print(f"{'':<40}{k:<40}{v:<50.2f}")
                    print("-"*100)
                self.utility_table_footer()
            elif command == "3":
                return
            else:
                print("Invalid command, try again")

    def revenue_statistics(self, start_date, end_date):
        search_list = self.logic.revenue_by_date(start_date, end_date)
        if search_list == 'No revenue to show during that time period.':
            print(f'\n***** {search_list} *****')
            return
        else:
            self.revenue_table_header()
            for result in search_list:
                print(f'{result.checkout_date:<20}{result.country:<20}{result.total_price:<20}')
            self.print_table_footer()

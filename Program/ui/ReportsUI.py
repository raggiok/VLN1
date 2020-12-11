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
        print("-"*260)
        print()

    def revenue_table_header(self):
        print()
        print(f'{"Date":<20}{"Location":<20}{"Revenue(€)":<20}')
        print("="*60)

    #Print Vehicle Table Header
    def vehicle_table_header(self):
        print(f"{'Unique ID':<20}{'Manufacturer':<20}{'Model':<20}{'Vehicle type':<20}{'Status':<20}{'Manufac. year':<20}{'Color':<20}{'License Req.':<20}{'Location':<20}{'Rate':<20}")
        print("-"*200)

    ### CONTRACT MAIN MENU ###
    def report_main_menu(self):
        while True:
            self.ui_menu_header("Reports")
            print("\nPlease select a an option:")
            self.ui_numbered_menu(["Revenues", "Vehicle Usability", "Invoices", "Main Menu"])
            self.ui_menu_footer()
            command = self.print_select_option()
            if command == "1":
                start_date = input(">> Input start date in format dd.mm.yy: ")
                end_date = input(">> Input end date in format dd.mm.yy: ")
                self.revenue_statistics(start_date, end_date)
            elif command == "2": # 2. Vehicle usability
                self.logic.utilization_report()
                
                # self.vehicle_table_header()
                # for item in self.logic.all_vehicles():
                #     print(item)
                # self.ui_menu_footer()
                #Sækja contract, lesa út destination
                #lesa út úr contract fjölda daga í notkun
                # deila með 354 og sýna %

            elif command == "3": # 3. Invoices
                pass
            elif command == "4":
                return
            else:
                print("Invalid command, try again")

    #Review revenue during time period

    #Overview of vehicle in a specific destination, categorized by type



    #     contractFieldnames = ["Customer name","Vehicle ID", "Start date of rental period (dd.mm.yy)","End date of rental period (dd.mm.yy)","Country","Employee Name","Total price"] # + "Contract Creation Date"




    # def print_report_menu(self):
    #     self.ui_menu_header('Report Menu')
    #     print("""\nSelect an option...\n1. Print statistics by destination.\n2. Print revenue statistics.\n3. Print billing overview.""")
    #     self.ui_menu_footer()

    # def print_report_menu(self):
    #     self.general.ui_menu_header('Report Menu')
    #     print("""\nSelect an option...\n1. Print statistics by destination.\n2. Print revenue statistics.\n3. Print billing overview.""")
    #     self.ui_menu_footer()

    # def destination_statistics(self):
    #     self.general.ui_menu_header('Destination Statistics')
    #     print("""Select an option...\n1. Revenue statistics.\n2. Vehicle statistics.""")
    #     self.ui_menu_footer()

    # def revenue_statistics(self):
    #     self.general.ui_menu_header('Revenue Statistics')
    #     print("""Select an option...\n1. Revenue by month.\n2. Revenue by date.""")
    #     self.ui_menu_footer()

    # def billing_overview(self):
    #     self.general.ui_menu_header('Billing Overview')
    #     start_date = input("From date (dd.mm.yy): ")
    #     end_date = input("End date (dd.mm.yy): ")



    # def destination_statistics(self):
    #     self.ui_menu_header('Destination Statistics')
    #     print("""Select an option...\n1. Revenue statistics.\n2. Vehicle statistics.""")
    #     self.ui_menu_footer()

    def revenue_statistics(self, start_date, end_date):
        search_list = self.logic.revenue_by_date(start_date, end_date)
        if search_list == 'No revenue to show during that time period.':
            print(f'\n***** {search_list} *****')
            return
        else:
            print(self.revenue_table_header)
            for result in search_list:
                print(f'{result.checkout_date:<20}{result.country:<20}{result.total_price:<20}')
            print(self.print_table_footer)

    # def billing_overview(self):
    #     self.ui_menu_header('Billing Overview')
    #     start_date = input("From date (dd.mm.yy): ")
    #     end_date = input("End date (dd.mm.yy): ")
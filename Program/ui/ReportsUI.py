from logic.logicAPI import LogicAPI

class ReportUI:

    def __init__(self):
        self.logic = LogicAPI()
        self.report = self.print_report_menu()


    #Review revenue during time period

    #Overview of vehicle in a specific destination, categorized by type






    def print_report_menu(self):
        self.ui_menu_header('Report Menu')
        print("""\nSelect an option...\n1. Print statistics by destination.\n2. Print revenue statistics.\n3. Print billing overview.""")
        self.ui_menu_footer()

    def destination_statistics(self):
        self.ui_menu_header('Destination Statistics')
        print("""Select an option...\n1. Revenue statistics.\n2. Vehicle statistics.""")
        self.ui_menu_footer()

    def revenue_statistics(self):
        self.ui_menu_header('Revenue Statistics')
        print("""Select an option...\n1. Revenue by month.\n2. Revenue by date.""")
        self.ui_menu_footer()

    def billing_overview(self):
        self.ui_menu_header('Billing Overview')
        start_date = input("From date (dd.mm.yy): ")
        end_date = input("End date (dd.mm.yy): ")

    def ui_menu_header(self, menu_name):
        print("\n" + "-"*20 + f"{menu_name}" + "-"*20)

    def ui_menu_footer(self):
        print("\n" + "-"*50)


        contractFieldnames = ["Customer name","Vehicle ID", "Start date of rental period (dd.mm.yy)","End date of rental period (dd.mm.yy)","Country","Employee Name","Total price"] # + "Contract Creation Date"


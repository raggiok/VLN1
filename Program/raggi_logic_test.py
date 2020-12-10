from models.contracts import Contract
from models.Customers import Customer
from models.Destinations import Destination
from models.Employee import Employee
from models.Vehicle import Vehicle
from models.Invoice import Invoice
from models.rates import Rate
from data.dataAPI import dataAPI
from logic.logicAPI import LogicAPI

import datetime
x = datetime.datetime.today()
current_time = x.strftime('%d-%b %Y')

test = dataAPI()
logic = LogicAPI()
#unique_id, customer, vehicle_unique_id, start_date, end_date, country, employee, total_price, contract_creation_date, state

contract = Contract('5', 'customer', 'customer_ssn', 'vehicle_unique_id', 'start_date', 'end_date', 'country', 'employee', 'total_price', 'contract_creation_date', 'checkout_date', 'checkin_date', 'checkin_location', 'state')
# customer = Customer("4", "John Smith", "150588-2459", "Heimilisgata 1", "TEST", "Reykjavik", "Iceland", "551-4489", "John@email.com")
# destination = Destination("2", "Iceland", "TEST", "Keflavik Airport", "558-5498", "10:00", "15:00", "Contact")
employee = Employee("", "Jon Jonsson", "150589-2129", "City staff", "TEST 50", "105", "Reykjavik", "Iceland", "551-4469", "889-2121", "test@test.is")
# car = Vehicle("40", "Benz", "Model-s", "Sportscar", "OK", "2020", "Panther Black", "Drivers License", "TEST")
# def validate(date_text):
#         try:
#             datetime.datetime.strptime(date_text, '%d.%m.%y')
#         except ValueError:
#             print("Incorrect data format, should be DD.MM.YY")

#test.create_employee(employee)
unique_id = "6"
password = "6168"

test = logic.check_password(unique_id, password)
for i in test:
    print(i)

#test.create_employee(employee)

# for item in test.get_contracts():
#     print(item)

# for item in test.get_customers():
#     print(item)

# for item in test.get_destinations():
#     print(item)

# for item in test.get_employees():
#     print(item)

# for item in test.get_vehicles():
#     print(item)

# invoice = Invoice("1","Customer no. 50", "Vehicle 25", "15", "20")

# test.create_invoice(invoice)

# rate = Rate('2','B','60')

# test.create_rate(rate)


# def print_main_menu(self,staff_role):
#     staff_role = check_staff_role()
#     if staff_role == 'admin':
#         self.print_admin_menu()
#     elif staff_role == 'city_staff':
#         self.print_city_menu()
#     elif staff_role == "office_staff":
#         self.print_office_menu()

# def check_staff_role(self):
#     staff_role = #fall sem kallar í logic og fær til baka staff role
#     return staff_role

# def print_admin_menu(list_of_menu_items):
#     for item in list_of_menu_items:
#         print(item)

# def print_city_menu(list_of_menu_items):
#     for item in list_of_menu_items:
#         if item == "Admin" or item == "Office":
#             continue
#         else:
#             print(item)

# def print_office_menu(list_of_menu_items):
#     for item in list_of_menu_items:
#         if item == "Admin" or item == "City":
#             continue
#         else:
#             print(item)


# print("Menu")
# print("1. Vehicle")
# print("2. Contract")
# print("3. Employee")
# user_input = input(">> Enter choice: ")

# def sub_menu():
#     print("1. Create")
#     print("2. Edit")
#     print("3. Delete")
#     user_input = input(">> Enter choice: ")
#     return user_input


# def create_instance(user_input):
#     if user_input == "1":
#         usr_input = sub_menu()
#         check_instance_type(usr_input)

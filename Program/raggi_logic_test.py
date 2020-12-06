from models.Contracts import Contract
from models.Customers import Customer
from models.Destinations import Destination
from models.Employee import Employee
from models.Vehicle import Vehicle
from data.dataAPI import dataAPI

import datetime
x = datetime.datetime.today()
current_time = x.strftime('%d-%b %Y')

test = dataAPI()
#unique_id, customer, vehicle_unique_id, start_date, end_date, country, employee, total_price, contract_creation_date, state

contract = Contract("3", "Bobby", "25", "01.01.2020", "11.02.2025", "Iceland", "Jon Jonsson", "9.999", f"{current_time}")
# customer = Customer("4", "John Smith", "150588-2459", "Heimilisgata 1", "TEST", "Reykjavik", "Iceland", "551-4489", "John@email.com")
# destination = Destination("2", "Iceland", "TEST", "Keflavik Airport", "558-5498", "10:00", "15:00", "Contact")
# employee = Employee("5", "Jon Jonsson", "150589-2129", "City staff", "TEST 50", "105", "Reykjavik", "Iceland", "551-4469", "889-2121", "test@test.is")
# car = Vehicle("40", "Benz", "Model-s", "Sportscar", "OK", "2020", "Panther Black", "Drivers License", "TEST")


test.create_contract(contract)

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



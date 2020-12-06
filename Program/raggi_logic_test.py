from models.Contracts import Contract
from models.Customers import Customer
from models.Destinations import Destination
from models.Employee import Employee
from models.Vehicle import Vehicle
from data.dataAPI import dataAPI

# car = Vehicle("1", "manufacturer", "model", "vehicle_type", "status", "man_year", "color", "license_type", "location")



test = dataAPI()


contract = Contract("3", "TEST", "25", "01.01.2020", "11.02.2025", "Iceland", "Jon Jonsson", "10.000.000")
customer = Customer("4", "John Smith", "150588-2459", "Heimilisgata 1", "TEST", "Reykjavik", "Iceland", "551-4489", "John@email.com")
destination = Destination("2", "Iceland", "TEST", "Keflavik Airport", "558-5498", "10:00", "15:00")
employee = Employee("5", "Jon Jonsson", "25", "City staff", "TEST 50", "105", "Reykjavik", "Iceland")
car = Vehicle("40", "Benz", "Model-s", "Sportscar", "OK", "2020", "Panther Black", "Drivers License", "TEST")



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
#Logic Wrapper
from logic.ContractsLogic import ContractLogic
from logic.VehicleLogic import VehicleLogic
from logic.CustomerLogic import CustomerLogic
from logic.DestinationLogic import DestinationLogic
from logic.EmployeeLogic import EmployeeLogic

class LogicAPI:

    def __init__(self):
        self.contract = ContractLogic()
        self.vehicle = VehicleLogic()
        self.customer = CustomerLogic()
        self.destination = DestinationLogic()
        self.employee = EmployeeLogic()

        ### Vehicles ###
    def create_vehicle(self,manufacturer,model,vehicle_type,status,manufacturing_year,color,license_type,location,rate):
        return self.vehicle.create_vehicle(manufacturer,model,vehicle_type,status,manufacturing_year,color,license_type,location,rate)

    def edit_vehicle(self, vehicle):
        return self.vehicle.edit_vehicle(vehicle)

    def all_vehicles(self):
        return self.vehicle.all_vehicles()

    def vehicle_amount_registered(self):
        return self.vehicle.vehicle_amount_registered()

    def add_unique_ID(self):
        self.vehicle.add_unique_ID()

    def search_vehicle_by_ID(self, vehicle_ID):
        return self.vehicle.search_vehicle_by_ID(vehicle_ID)

    def search_vehicle_by_manufacturer(self, manufacturer):
        return self.vehicle.search_vehicle_by_manufacturer(manufacturer)

    def search_vehicle_by_model(self, model):
        return self.vehicle.search_vehicle_by_model(model)

    def search_vehicle_by_vehicle_type(self, vehicle_type):
        return self.vehicle.search_vehicle_by_vehicle_type(vehicle_type)

    def search_vehicle_by_status(self, status):
        return self.vehicle.search_vehicle_by_status(status)

    def search_vehicle_by_manufacturing_year(self, manufacturing_year):
        return self.vehicle.search_vehicle_by_manufacturing_year(manufacturing_year)

    def search_vehicle_by_color(self, color):
        return self.vehicle.search_vehicle_by_color(color)   

    def search_vehicle_by_license_type(self, license_type):
        return self.vehicle.search_vehicle_by_license_type(license_type)

    def search_vehicle_by_location(self, location):
        return self.vehicle.search_vehicle_by_location(location)

    def available_model(self):
        return self.vehicle.available_model()

    def available_manufacturers(self):
        return self.vehicle.available_manufacturers()

    def available_vehicle_type(self):
        return self.vehicle.available_vehicle_type()

    def available_status(self):
        return self.vehicle.available_status()

    def available_manufacturing_year(self):
        return self.vehicle.available_manufacturing_year()

    def available_color(self):
        return self.vehicle.available_color()

    def available_license_type(self):
        return self.vehicle.available_license_type()

    def available_location(self):
        return self.vehicle.available_location()




    def delete_vehicle(self, vehicle_ID):
        return self.vehicle.delete_vehicle(vehicle_ID)

        ### Contracts ###
    def all_contracts(self):
        return self.contract.all_contracts()

    def search_contracts_by_name(self, name):
        return self.contract.search_contracts_by_name(name)

    def create_new_contract(self, a_list):
        return self.contract.create_contract(a_list)

    def search_contracts_by_customer(self, string):
        return self.contract.search_contracts_by_customer(string)
    
    def search_contract_by_vin(self, string):
        return self.contract.search_contracts_by_vin(string)
    
    def search_contracts_by_id(self, string):
        return self.contract.search_contracts_by_id(string)

    def delete_contract(self, string):
        return self.contract.delete_contract(string)

    
        ### Customers ###
    def create_customer(self, customer_list):
        return self.customer.create_customer(customer_list)

    def all_customer(self):
        return self.customer.all_customer()

    def customer_by_name(self, name):
        return self.customer.customer_by_name(name)

    def customer_by_ssn(self, ssn):
        return self.customer.customer_by_ssn(ssn)

    def customer_by_area(self,country):
        return self.customer.customer_by_area(country)

    def delete_customer(self, ssn):
        return self.customer.delete_customer(ssn)

    def update_customer(self, edited_instance):
        self.customer.edit_customer(edited_instance)

       
        ### Destinations ###
    def create_destination(self, country, city, airport, phone_number, opening_time, closing_time, main_contact):
        return self.destination.create_destination(country, city, airport, phone_number, opening_time, closing_time, main_contact)

    def edit_destination(self, a_list):
        return self.destination.edit_destination(a_list)

    def all_destinations(self):
        return self.destination.all_destinations()

    def delete_destination(self,destination_id):
        return self.destination.delete_destination(destination_id)
      
      
       ##Search functions##
    def search_destinations_by_id(self,unique_id):
        return self.destination.search_destinations_by_id(unique_id)

    def search_destination_by_country(self,country):
        return self.destination.search_destinations_by_country(country)

    def search_destination_by_city(self,city):
        return self.destination.search_destinations_by_cities(city)    

    def search_destination_by_airport(self,airport):
        return self.destination.search_destinations_by_airport(airport)

    def search_destination_by_phone_number(self,phone_number):
        return self.destination.search_destinations_by_phone_number(phone_number)    

    def search_destination_by_opening_time(self,opening_time):
        return self.destination.search_destinations_by_opening_time(opening_time)

    def search_destination_by_closing_time(self,closing_time):
        return self.destination.search_destinations_by_closing_time(closing_time)

    def search_destination_by_main_contact(self,main_contact):
        return self.destination.search_destinations_by_main_contact(main_contact)

    def available_country(self):
        return self.destination.available_countries()

    def available_city(self):
        return self.destination.available_cities()

    def available_airport(self):
        return self.destination.available_airports()

    def available_phone_number(self):
        return self.destination.available_phone_numbers()

    def available_opening_time(self):
        return self.destination.available_opening_times()
            
    def available_closing_time(self):
        return self.destination.available_closing_times()    
         
    def available_main_contact(self):
        return self.destination.available_main_contacts()    
        
        
        
        
        
        ### Employee ###

    def create_employee(self, a_list):
        self.employee.create_employee(a_list)

    def get_employees(self):
        return self.employee.get_employees()

    def search_employees_by_role(self, string):
        return self.employee.search_by_role(string)

    def search_employees_by_id(self, id_number):
        return self.employee.search_by_id(id_number)

    def delete_employee(self, id_number):
        return self.employee.delete_employee(id_number)

    def update_employee(self, updated_object):
        self.employee.update_employee(updated_object)
#Logic Wrapper
from logic.ContractsLogic import ContractLogic
from logic.VehicleLogic import VehicleLogic
from logic.CustomerLogic import CustomerLogic
from logic.DestinationLogic import DestinationLogic
from logic.EmployeeLogic import EmployeeLogic
from logic.ReportLogic import ReportLogic

class LogicAPI:

    def __init__(self):
        self.contract = ContractLogic()
        self.vehicle = VehicleLogic()
        self.customer = CustomerLogic()
        self.destination = DestinationLogic()
        self.employee = EmployeeLogic()
        self.report = ReportLogic()

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

    def vehicle_check_out(self, contract_id):
        return self.contract.vehicle_check_out(contract_id)

    def vehicle_check_in(self, contract_id):
        return self.contract.vehicle_check_in(contract_id)


    def delete_vehicle(self, vehicle_ID):
        return self.vehicle.delete_vehicle(vehicle_ID)

        ### Contracts ###
    def all_contracts(self):
        return self.contract.all_contracts()

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

    def edit_contract(self, contract_instance):
        return self.contract.update_contract(contract_instance)
    
### Customers ###
    def create_customer(self, customer_list):
        return self.customer.create_customer(customer_list)

    def all_customer(self):
        return self.customer.all_customer()

    def delete_customer(self, unique_id):
        return self.customer.delete_customer(unique_id)

    def update_customer(self, edited_instance):
        self.customer.edit_customer(edited_instance)

      #search function
    def search_customer_by_unique(self,unique_id):
        return self.customer.search_customer_by_id(unique_id)
    
    def search_customers_by_name(self, name):
        return self.customer.search_by_name(name)

    def search_customers_by_id(self, ssn):
        return self.customer.search_by_id(ssn)

    def search_customers_by_address(self, address):
        return self.customer.search_by_address(address)
       
    def search_customers_by_zip_code(self, zip_code):
        return self.customer.search_by_zip_code(zip_code)

    def search_customers_by_city(self, city):
        return self.customer.search_by_city(city)

    def search_customers_by_country(self, country):
        return self.customer.search_by_country(country)

    #name	ssn	role	address	zip_code	city	country
    def available_customer_name(self):
        return self.customer.available_the_name()
    
    def available_customer_ssn(self):
        return self.customer.available_the_ssn()

    def available_customer_address(self):
        return self.customer.available_the_address()

    def available_customer_zip_code(self):
        return self.customer.available_the_zip_code()
    
    def available_customer_city(self):
        return self.customer.available_the_city()

    def available_customer_country(self):
        return self.customer.available_the_country()
        
    

       
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

    def delete_employee(self, id_number):
        return self.employee.delete_employee(id_number)

    def update_employee(self, updated_object):
        self.employee.update_employee(updated_object)

    #search function
    def search_employee_by_unique(self,unique_id):
        return self.employee.search_employee_by_id(unique_id)
    
    def search_employees_by_name(self, name):
        return self.employee.search_by_name(name)

    def search_employees_by_role(self, role):
        return self.employee.search_by_role(role)

    def search_employees_by_id(self, ssn):
        return self.employee.search_by_id(ssn)

    def search_employees_by_address(self, address):
        return self.employee.search_by_address(address)
       
    def search_employees_by_zip_code(self, zip_code):
        return self.employee.search_by_zip_code(zip_code)

    def search_employees_by_city(self, city):
        return self.employee.search_by_city(city)

    def search_employees_by_country(self, country):
        return self.employee.search_by_country(country)

    #name	ssn	role	address	zip_code	city	country
    def available_name(self):
        return self.employee.available_the_name()
    
    def available_ssn(self):
        return self.employee.available_the_ssn()
    
    def available_role(self):
        return self.employee.available_the_role()

    def available_address(self):
        return self.employee.available_the_address()

    def available_zip_code(self):
        return self.employee.available_the_zip_code()
    
    def emp_available_city(self):
        return self.employee.available_the_city()

    def emp_available_country(self):
        return self.employee.available_the_country()


    def generate_password(self):
            return self.employee.autogenerate_password()

    def check_password(self,user_id, password):
        return self.employee.check_employee_password(user_id, password)

    ###Invoice###

    def create_invoice(self, contract_id):
        return self.contract.create_invoice(contract_id)
    
    def search_invoices(self, invoice_id):
        return self.contract.search_invoices(invoice_id)

    def get_all_invoices(self):
        return self.contract.get_all_invoices()
    
    def set_invoice_to_paid(self, invoice_id):
        return self.contract.set_invoice_to_paid(invoice_id)


    ### REPORTS ###

    def get_utitlity_report(self):
        return self.report.merge_report()

    def contracts_to_list(self):
        return self.report.contracts_to_list()
    
    def vehicle_id_and_types(self):
        return self.report.vehicle_id_and_types()

    def calcuate_days_per_vehicle(self,vehicle_list):
        return self.report.calcuate_days_per_vehicle(vehicle_list)

    def merge_report(self):
        return self.report.merge_report()

    def utilization_report(self):
        return self.report.utilization_report()
        
    def add_vehicle_type(self):
        return self.report.add_vehicle_type()
    
    def revenue_by_date(self, start_date, end_date):
        return self.report.revenue_by_date(start_date, end_date)
    
    def result_list(self):
        return self.report.result_list()

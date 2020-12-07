#Logic Wrapper
from logic.ContractsLogic import ContractLogic
from logic.VehicleLogic import VehicleLogic
from logic.CustomerLogic import CustomerLogic
from logic.DestinationLogic import DestinationLogic

class LogicAPI:

    def __init__(self):
        self.contract = ContractLogic()
        self.vehicle = VehicleLogic()
        self.customer = CustomerLogic()
        self.destination = DestinationLogic()

        ### Vehicles ###
    def create_vehicle(self,manufacturer,model,vehicle_type,status,manufacturing_year,color,license_requirement,location):
        return self.vehicle.create_vehicle(self,manufacturer,model,vehicle_type,status,manufacturing_year,color,license_requirement,location)

    def edit_vehicle(self, vehicle):
        return self.vehicle.edit_vehicle(vehicle)

    def vehicle_types(self):
        return self.vehicle.vehicle_types()

    def all_vehicles(self):
        return self.vehicle.all_vehicles()

    def vehicle_amount_registered(self):
        return self.vehicle.vehicle_amount_registered()

    def add_unique_ID(self):
        self.vehicle.add_unique_ID()

    def search_vehicle_by_ID(self, vehicle_ID):
        return self.vehicle.search_vehicle_by_ID(vehicle_ID)

    def search_vehicle_by_type(self, vehicle_type):
        return self.vehicle.search_vehicle_by_type(vehicle_type)


        ### Contracts ###
    def all_contracts(self):
        return self.contract.all_contracts()

    def search_contracts_by_name(self, name):
        return self.contract.search_contracts_by_name(name)

    def create_new_contract(self, a_list):
        self.contract.create_contract(a_list)

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
        return self.customer.customer_by_name(ssn)

    def customer_by_ssn(self, ssn):
        return self.customer.customer_by_ssn(ssn)

    def customer_by_area(self,country):
        return self.customer(country)

    def delete_customer(self, ssn):
        return self.customer.delete_customer

    def update_customer(self, edited_instance):
        self.customer.edit_customer()

        ### Destinations ###
    def create_destination(self, a_list):
        return self.destination.create_destination(a_list)

    def edit_destination(self, a_list):
        return self.destination.edit_destination(a_list)
    
    def destination_types(self):
        return self.destination.destination_types()

    def all_destinations(self):
        return self.destination.all_destinations()
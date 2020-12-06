# A Wrapper for all the DATA functionality
from data.datafunc import Data

class dataAPI():

    def __init__(self):
        self.data = Data()


    ### CONTRACTS ###
    def new_contract_id(self):
        return self.data.new_id(instance_type="contract")

    def create_contract(self, instance):
        return self.data.write_data(instance, instance_type="contract")

    def update_contract(self, instance):
        return self.data.edit_data(instance, instance_type="contract")

    def delete_contract(self, instance):
        return self.data.delete_data(instance, instance_type="contract")

    def get_contracts(self):
        '''Returns a list of all instances of Contracts in .csv file'''
        return self.data.get_data(instance_type="contract")

    ### CUSTOMER ###
    def new_customer_id(self):
        return self.data.new_id(instance_type="customer")

    def create_customer(self, instance):
        return self.data.write_data(instance, instance_type="customer")

    def update_customer(self, instance):
        return self.data.edit_data(instance, instance_type="customer")

    def delete_customer(self, instance):
        return self.data.delete_data(instance, instance_type="customer")

    def get_customers(self):
        return self.data.get_data(instance_type="customer")

    ### DESTINATIONS ###
    def new_destination_id(self):
        return self.data.new_id(instance_type="destination")

    def create_destination(self, instance):
        return self.data.write_data(instance, instance_type="destination")

    def update_destination(self, instance):
        return self.data.edit_data(instance, instance_type="destination")

    def delete_destination(self, instance):
        return self.data.delete_data(instance, instance_type="destination")

    def get_destinations(self):
        return self.data.get_data(instance_type="destination")


    ### EMPLOYEES ###
    def new_employee_id(self):
        return self.data.new_id(instance_type="employee")

    def create_employee(self, instance):
        return self.data.write_data(instance, instance_type="employee")

    def update_employee(self, instance):
        return self.data.edit_data(instance, instance_type="employee")

    def delete_employee(self, instance):
        return self.data.delete_data(instance, instance_type="employee")

    def get_employees(self):
        return self.data.get_data(instance_type="employee")
    

    ### VEHICLES ###
    def new_vehicle_id(self):
        return self.data.new_id(instance_type="vehicle")

    def create_vehicle(self, instance):
        return self.data.write_data(instance, instance_type="vehicle")

    def update_vehicle(self, instance):
        return self.data.edit_data(instance, instance_type="vehicle")
    
    def delete_vehicle(self, instance):
        '''Changes state of Vehicle from "Active" to "Inactive"'''
        return self.data.delete_data(instance, instance_type="vehicle")

    def get_vehicles(self):
        '''Returns a list of all instances of Vehicles in .csv file'''
        return self.data.get_data(instance_type="vehicle")

    
    ### INVOICES ###
    def new_invoices_id(self):
        return self.data.new_id(instance_type="invoice")

    def create_invoice(self, instance):
        return self.data.write_data(instance, instance_type="invoice")

    def update_invoice(self, instance):
        return self.data.edit_data(instance, instance_type="invoice")

    def delete_invoice(self, instance):
        return self.data.delete_data(instance, instance_type="invoice")

    def get_invoices(self):
        return self.data.get_data(instance_type="invoice")

    ### RATES ###
    def new_rate_id(self):
        return self.data.new_id(instance_type="rate")

    def create_rate(self, instance):
        return self.data.write_data(instance, instance_type="rate")

    def update_rate(self, instance):
        return self.data.edit_data(instance, instance_type="rate")

    def delete_rate(self, instance):
        return self.data.delete_data(instance, instance_type="rate")

    def get_rates(self):
        return self.data.get_data(instance_type="rate")
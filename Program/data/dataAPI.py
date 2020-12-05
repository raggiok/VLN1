# A Wrapper for all the DATA functionality

from data.VehicleDatabase import VehicleData
from data.ContractsDatabase import ContractData
#from data.DestinationDatabase import DestinationData
#from data.EmployeeData import EmployeeData

class dataAPI():

    def __init__(self):
        self.vehicle = VehicleData()
        self.contract = ContractData()
        #self.destination = DestinationData()
        #self.employee = EmployeeData()


    ### VEHICLES ###
    def new_vehicle_id(self):
        return self.vehicle.new_vehicle_id()

    def create_vehicle(self, vehicle):
        return self.vehicle.new_vehicle(vehicle)

    def update_vehicle(self, vehicle):
        return self.vehicle.edit_vehicle(vehicle)
    
    def delete_vehicle(self, vehicle):
        '''Changes state of Vehicle from "Active" to "Inactive"'''
        return self.vehicle.delete_vehicle(vehicle)

    def get_vehicles(self):
        '''Returns a list of all instances of Vehicles in .csv file'''
        return self.vehicle.get_vehicles()


    ### CONTRACTS ###
    def new_contract_id(self):
        return self.contract.new_contract_id()

    def create_contract(self, contract):
        return self.contract.add_contract(contract)

    def update_contract(self, contract):
        return self.vehicle.edit_contract(contract)

    def delete_contract(self, contract):
        return self.vehicle.delete_contract(contract)

    def get_contracts(self):
        return self.contract.get_contracts()

    ### DESTINATIONS ###
    def new_destination_id(self, destination):
        pass

    def create_destination(self, destination):
        pass

    def update_destination(self, destination):
        pass

    def delete_destination(self, destination):
        pass

    def get_destinations(self):
        pass


    ### EMPLOYEES ###
    def new_employee_id(self, employee):
        pass

    def create_employee(self, employee):
        pass

    def update_employee(self, employee):
        pass

    def delete_employee(self, employee):
        pass

    def get_employee(self):
        pass
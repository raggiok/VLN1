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
    def create_contract(self):
        pass

    def update_contract(self):
        pass

    def delete_contract(self):
        pass

    def all_contracts(self):
        pass

    ### DESTINATIONS ###
    def create_destination(self):
        pass

    def update_destination(self):
        pass

    def delete_destination(self):
        pass

    def all_destinations(self):
        pass


    ### EMPLOYEES ###
    def create_employee(self):
        pass

    def update_employee(self):
        pass

    def delete_employee(self):
        pass

    def all_employee(self):
        pass

    ### DESTINATIONS ###
    def create_(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def all(self):
        pass


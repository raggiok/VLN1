from data.dataAPI import dataAPI
from models.contracts import Contract


class ContractLogic:

    def __init__(self):
        self.data = dataAPI()

    def all_contracts(self):
        return self.data.get_contracts()

    
    def create_contract(self, a_list):
        new_contract = Contract(self.data.new_contract_id() , *a_list)
        if self.check_availability(new_contract):
            self.data.create_contract(new_contract)
        else:
            return "Vehicle unavailable or inadequate license type."

    def check_availability(self, new_contract):     #Athugar tímaskorður
        for contract in self.all_contracts():
            if contract.vehicle_unique_id == new_contract.vehicle_unique_id:
                if contract.start_date <= new_contract.start_date & contract.end_date >= new_contract.start_date:
                    return False
                elif contract.end_date >= new_contract.end_date & new_contract.end_date >= contract.start_date:
                    return False
                elif contract.start_date >= new_contract.start_date & contract.start_date <= new_contract.end_date:
                    return False
        return True
    
    def check_license(self, new_contract):
        for contract in self.all_contracts():
            if contract.vehicle.license_type not in new_contract.customer.license_type:
                return False
        return True

    def check_country(self, new_contract):
        if new_contract.country != new_contract.vehicle.location:
            return False
        else:
            return True
        

    def search_contracts_by_customer(self, string):
        result_list = []
        for contract in self.all_contracts():
            if contract.get_customer().lower() == string.lower():
                result_list.append(contract)
        return self.no_match_found(result_list)
        
    def search_contracts_by_vin(self, string):
        result_list = []
        for contract in self.all_contracts():
            if contract.get_vin().lower() == string.lower():
                result_list.append(contract)
        return self.no_match_found(result_list)

    def search_contracts_by_id(self, string):
        match = []
        for contract in self.all_contracts():
            if contract.get_unique_id() == string:
                match.append(contract)
        return self.no_match_found(match)

    def no_match_found(self, result_list):
        if result_list:
            return result_list
        else:
            result_list.append("No match found.")
            return result_list

    def delete_contract(self, contract_id):
        result = self.search_contracts_by_id(contract_id)
        if result[0] != "No match found.":
            self.data.delete_contract(result[0])
        else:
            return result

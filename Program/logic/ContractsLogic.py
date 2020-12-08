from data.dataAPI import dataAPI
from models.contracts import Contract


class ContractLogic:

    def __init__(self):
        self.data = dataAPI()

    def all_contracts(self):
        return self.data.get_contracts()

    
    def create_contract(self, a_list):
        new_contract = Contract(self.data.new_contract_id , *a_list)
        self.data.create_contract(new_contract)


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

    def delete_contract(self, string):
        confirmation = self.data.delete_contract(string)
        return confirmation
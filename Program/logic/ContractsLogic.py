from data.ContractsDatabase import ContractData
from models.contracts import Contract
class ContractLogic:

    def __init__(self):
        self.data = ContractData()

    def all_contracts(self):
        return self.data.get_contracts()

    def search_contracts_by_name(self, name):
        ret_string = ""
        temporary_list = []
        for item in self.data.get_contracts():
            temporary_list = item.get_customer().split()
    
    def create_new_contract(self, list):      #Vantar betri útfærslu?
        self.data.add_contract(list[0], list[1], list[2], list[3], list[4], self.add_contract_id())

    def add_contract_id(self):
        return (len(self.all_contracts()) + 1)

    def search_contracts_by_customer(self, string):
        result_list = []
        for contract in self.all_contracts():
            if contract.get_customer().lower() == string.lower():
                result_list.append(contract)
        if result_list:
            return result_list
        
    def search_contracts_by_vin(self, string):
        result_list = []
        for contract in self.all_contracts():
            if contract.get_vin().lower() == string.lower():
                result_list.append(contract)
        if result_list:
            return result_list

    def search_contracts_by_id(self, string):
        for contract in self.all_contracts():
            if contract.get
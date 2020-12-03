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
    
    def create_new_contract(self, string):
        return "d"

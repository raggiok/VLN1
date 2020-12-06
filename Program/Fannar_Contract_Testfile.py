from ui.ContractsUI import ContractUI
from logic.logicAPI import LogicAPI


data = LogicAPI()

for contract in data.all_destinations():
    print(contract)
#logic = ContractLogic()
#data_main = ContractUI()

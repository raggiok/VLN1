from ui.ContractsUI import ContractUI
from logic.logicAPI import LogicAPI
from models.contracts import Contract



for contract in LogicAPI().all_contracts():
    print(contract)
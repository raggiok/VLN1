from ui.ContractsUI import ContractUI
from logic.logicAPI import LogicAPI
from models.contracts import Contract



#LogicAPI().create_customer(["1", '1', '1', '1', '1', '1', '1', '1', '1'])

print(LogicAPI().search_by_id("1"))
for employee in LogicAPI().search_contracts_by_customer("City staff"):
    print(employee)
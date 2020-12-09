from ui.ContractsUI import ContractUI
from datetime import datetime, date
from logic.logicAPI import LogicAPI
t1 = date(year = 18, month = 7, day = 23)
#t2 = date(year = 2018, month = 7, day = 23)


print(LogicAPI().create_new_contract(["John Smith", "16", "13.11.20", "14.11.20","Nuk", "Jón", "1500", "09.12.20"]))


a = 5 > 7

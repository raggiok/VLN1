from ui.ContractsUI import ContractUI
from datetime import datetime, date
from logic.ContractsLogic import ContractLogic
from ui.UIMain import UIMain
t1 = date(year = 18, month = 7, day = 23)
t2 = date(year = 2018, month = 7, day = 23)
t3 = t2 - t1
print(t3.days * 100)


UIMain()
#print(ContractLogic().create_invoice("5"))
#print(LogicAPI().create_new_contract(["John Smith", "16", "15.11.20", "16.11.20","Nuuk", "Jón", "1500", "09.12.20"]))
#
#ContractUI()

a = 5 > 7

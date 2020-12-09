from logic.logicAPI import LogicAPI
from ui.UIMain import UIMain
from models.contracts import Contract



for emp in LogicAPI().all_contracts():
    print(emp)
#print(LogicAPI().search_employees_by_role("lala"))
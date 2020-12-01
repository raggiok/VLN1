from data.DataMain import  DataMain

class LogicMain():
    def __init__(self):
        print("inside logic")
        self.data = DataMain()

    def all_employees(self):
        return self.data.get_employees()


    def employee_by_role(self, role):
        emps = self.data.get_employees()
        retList = []
        for emp in emps:
            if emp.role == role:
                retList.append(emp)
        return retList


    


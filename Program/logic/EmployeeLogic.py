from data.dataAPI import dataAPI
from models.Employee import Employee

class EmployeeLogic:

    def __init__(self):
        self.data = dataAPI()

    def create_employee(self, a_list):
        return Employee(*a_list)

    def get_employees(self):
        return self.data.get_employees()

    def search_by_id(self, string):
        match = ""
        for employee in self.get_employees():
            if employee.unique_id == string:
                match = employee
        return match

    def search_by_role(self, string):
        match = []
        for employee in self.get_employees():
            if employee.role.lower() == string.lower():
                match.append(employee)
        return match

    def delete_employee(self, string):
        if self.search_by_id(string):
            self.data.delete_employee(self.search_by_id(string))
        else:
            return "Employee not found."

    def update_employee(self, updated_employee):
        self.data.update_employee(updated_employee)
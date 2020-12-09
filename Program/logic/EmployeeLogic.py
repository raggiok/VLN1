from data.dataAPI import dataAPI
from models.Employee import Employee

class EmployeeLogic:

    def __init__(self):
        self.data = dataAPI()

    def create_employee(self, a_list):
        employee = Employee("placeholder", *a_list)
        return self.data.create_employee(employee)
        
    def get_employees(self):
        return self.data.get_employees()

    def search_by_id(self, string):
        match = []
        for employee in self.get_employees():
            if employee.unique_id == string:
                match.append(employee)
        return self.no_match_found(match)

    def search_by_role(self, string):
        match = []
        for employee in self.get_employees():
            if employee.role.lower() == string.lower():
                match.append(employee)
        return self.no_match_found(match)

    def delete_employee(self, string):
        temp_list = self.search_by_id(string)
        if temp_list[0] != "No match found.":
            self.data.delete_employee(temp_list[0])
        else:
            return temp_list

    def update_employee(self, updated_employee):
        self.data.update_employee(updated_employee)

    def no_match_found(self, result_list):
        if result_list:
            return result_list
        else:
            result_list.append("No match found.")
            return result_list
from data.dataAPI import dataAPI
from models.Employee import Employee

class EmployeeLogic:

    def __init__(self):
        self.data = dataAPI()

    def create_employee(self, a_list):
        employee = Employee(self.data.new_employee_id, *a_list)
        return self.data.create_employee(employee)
        
    def get_employees(self):
        return self.data.get_employees()

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

    #search function
    #name	ssn	role	address	zip_code	city	country	
###serach function ###
    def available_the_name(self):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.name not in retList:
                retList.append(employee.name)
        return retList     

    def available_the_ssn(self):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.ssn not in retList:
                retList.append(employee.ssn)
        return retList    

    def available_the_role(self):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.role not in retList:
                retList.append(employee.role)
        return retList     

    def available_the_address(self):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.address not in retList:
                retList.append(employee.address)
        return retList 

    def available_the_zip_code(self):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.zip_code not in retList:
                retList.append(employee.zip_code)
        return retList    

    def available_the_city(self):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.city not in retList:
                retList.append(employee.city)
        return retList     

    def available_the_country(self):
        employee = self.data.get_customers()
        retList = []
        for employee in employee:
            if employee.country not in retList:
                retList.append(employee.country)
        return retList 

###
    def search_employee_by_id(self,unique_id):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.unique_id == unique_id:
                retList.append(employee)
        return self.no_match_found(retList)

    def search_by_name(self,name):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.name.lower() == name.lower():
                retList.append(employee)
        return self.no_match_found(retList)

    def search_by_role(self,role):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.role.lower() == role.lower():
                retList.append(employee)
        return self.no_match_found(retList)

    def search_by_id(self,ssn):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.ssn.lower() == ssn.lower():
                retList.append(employee)
        return self.no_match_found(retList)

    def search_by_address(self,address):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.address.lower() == address.lower():
                retList.append(employee)
        return self.no_match_found(retList)

    def search_by_country(self,country):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.country.lower() == country.lower():
                retList.append(employee)
        return self.no_match_found(retList)

    def search_by_city(self,city):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.city.lower() == city.lower():
                retList.append(employee)
        return self.no_match_found(retList)

    def search_by_zip_code(self,zip_code):
        employee = self.data.get_employees()
        retList = []
        for employee in employee:
            if employee.zip_code.lower() == zip_code.lower():
                retList.append(employee)
        return self.no_match_found(retList)

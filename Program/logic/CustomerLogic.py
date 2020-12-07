from data.dataAPI import dataAPI
from models.Customers import Customer

class CustomerLogic:
    def __init__(self):
        self.data = dataAPI()

    def create_customer(self, customer_list):
        customer_instance = Customer(self.data.new_customer_id, *customer_list)
        self.data.create_customer(customer_instance)

    def all_customer(self):
        return self.data.get_customers()

    # search by name 
    def customer_by_name(self,name):
        custs = self.data.get_customers()
        retList = []
        for cust in custs:
            if cust.name.lower() == name.lower():
                retList.append(cust)
        return self.no_match_found(retList)

    #search by ID
    def customer_by_ssn(self,ssn):
        custs = self.data.get_customers()
        retList = []
        for cust in custs:
            if cust.ssn == ssn:
                retList.append(cust)
        return self.no_match_found(retList)

    #search by area/land
    def customer_by_area(self,country):
        custs = self.data.get_customers()
        retList = []
        for cust in custs:
            if cust.country.lower() == country.lower():
                retList.append(cust)
        return self.no_match_found(retList)

    #delete customer information
    def delete_customer(self, ssn):
        deleteList = self.customer_by_ssn(ssn)
        if deleteList:
            self.data.delete_customer(deleteList[0])
        else:
            return "Customer not found."

    #Edit customer
    def edit_customer(self, edited_instance):
        self.data.update_customer()

    def no_match_found(self, result_list):
        if result_list:
            return result_list
        else:
            result_list.append("No match found.")
            return result_list
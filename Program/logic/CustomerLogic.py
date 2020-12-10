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

    #delete customer information
    def delete_customer(self, string):
        temp_list = self.search_customer_by_id(string)
        if temp_list[0] != "*** No match found ***":
            self.data.delete_customer(temp_list[0])
            return ["\n*** Customer successfully deleted ***\n"]
        else:
            return temp_list

    #Edit customer
    def edit_customer(self, edited_instance):
        self.data.update_customer()

    def no_match_found(self, result_list):
        if result_list:
            return result_list
        else:
            result_list.append("No match found.")
            return result_list

    
#name	ssn	role	address	zip_code	city	country	
###serach function ###
    def available_the_name(self):
        customer = self.data.get_customers()
        retList = []
        for customer in customer:
            if customer.name not in retList:
                retList.append(customer.name)
        return retList     

    def available_the_ssn(self):
        customer = self.data.get_customers()
        retList = []
        for customer in customer:
            if customer.ssn not in retList:
                retList.append(customer.ssn)
        return retList    


    def available_the_address(self):
        customer = self.data.get_customers()
        retList = []
        for customer in customer:
            if customer.address not in retList:
                retList.append(customer.address)
        return retList 

    def available_the_zip_code(self):
        customer = self.data.get_customers()
        retList = []
        for customer in customer:
            if customer.zip_code not in retList:
                retList.append(customer.zip_code)
        return retList    

    def available_the_city(self):
        customer = self.data.get_customers()
        retList = []
        for customer in customer:
            if customer.city not in retList:
                retList.append(customer.city)
        return retList     

    def available_the_country(self):
        customer = self.data.get_customers()
        retList = []
        for customer in customer:
            if customer.country not in retList:
                retList.append(customer.country)
        return retList 

    ###
    def search_customer_by_id(self,unique_id):
        customer = self.data.get_customers()
        retList = []
        for customer in customer:
            if customer.unique_id == unique_id:
                retList.append(customer)
        return self.no_match_found(retList)

    def search_by_name(self,name):
        customer = self.data.get_customers()
        retList = []
        for customer in customer:
            if customer.name.lower() == name.lower():
                retList.append(customer)
        return self.no_match_found(retList)

    def search_by_id(self,ssn):
        customer = self.data.get_customers()
        retList = []
        for customer in customer:
            if customer.ssn.lower() == ssn.lower():
                retList.append(customer)
        return self.no_match_found(retList)

    def search_by_address(self,address):
        customer = self.data.get_customers()
        retList = []
        for customer in customer:
            if customer.address.lower() == address.lower():
                retList.append(customer)
        return self.no_match_found(retList)

    def search_by_country(self,country):
        customer = self.data.get_customers()
        retList = []
        for customer in customer:
            if customer.country.lower() == country.lower():
                retList.append(customer)
        return self.no_match_found(retList)

    def search_by_city(self,city):
        customer = self.data.get_customers()
        retList = []
        for customer in customer:
            if customer.city.lower() == city.lower():
                retList.append(customer)
        return self.no_match_found(retList)

    def search_by_zip_code(self,zip_code):
        customer = self.data.get_customers()
        retList = []
        for customer in customer:
            if customer.zip_code.lower() == zip_code.lower():
                retList.append(customer)
        return self.no_match_found(retList)

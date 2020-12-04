from data.CustomerDatabase import CustomerData

class CustomerLogic:
    def __init__(self):
        self.data = CustomerData()

    def create_customer(self, customer_list):
        return self.data.new_customer(customer_list)

    def all_customer(self):
        return self.data.get_customer()

    # search by name 
    def customer_by_name(self,name):
        cust = self.data.get_customer()
        retList = []
        for cust in custs:
            if cust.name == name:
                retList.append(cust)
        return retList

    #search by ID
    def customer_by_ssn(self,ssn):
        cust = self.data.get_customer()
        retList = []
        for cust in custs:
            if cust.ssn == ssn:
                retList.append(cust)
        return retList

    #search by area/land
    def customer_by_area(self,country):
        cust = self.data.get_customer()
        retList = []
        for cust in custs:
            if cust.country == country:
                retList.append(cust)
        return retList

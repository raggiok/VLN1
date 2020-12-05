<<<<<<< HEAD
class Contract:
    def __init__(self, customer, vehicle_vin, start_date, end_date, country, contract_id):
        self.customer = customer
        self.vehicle_vin = vehicle_vin
        self.start_date = start_date
        self.end_date = end_date
        self.country = country
        self.identification_number = str(contract_id)
        
    def change_customer_name(self, new_customer_name):
        self.customer = new_customer_name

    def change_vehicle(self, new_vehicle_vin):
        self.vehicle_vin = new_vehicle_vin

    def change_start_date(self, new_start_date, new_end_date):
        self.start_date = new_start_date
        self.end_date = new_end_date

    def change_country(self, new_country_name):
        self.country = new_country_name

    def get_customer(self):
        return self.customer
    
    def get_vin(self):
        return self.identification_number

    def get_identification_number(self):
        return self.identification_number
        
    def __str__(self):
        contract_string = f'{self.identification_number} {self.customer} {self.vehicle_vin} {self.start_date} {self.end_date} {self.country}'
        return contract_string
=======
class Contract:
    def __init__(self, unique_id, customer, vehicle_unique_id, start_date, end_date, country, employee, total_price, state="Active"):
        self.unique_id = unique_id
        self.customer = customer
        self.vehicle_unique_id = vehicle_unique_id
        self.start_date = start_date
        self.end_date = end_date
        self.country = country
        self.employee = employee
        self.total_price = total_price
        self.state = state
        
    def change_customer_name(self, new_customer_name):
        self.customer = new_customer_name

    def change_vehicle(self, new_vehicle_unique_id):
        self.vehicle_unique_id = new_vehicle_unique_id

    def change_start_date(self, new_start_date, new_end_date):
        self.start_date = new_start_date
        self.end_date = new_end_date

    def change_country(self, new_country_name):
        self.country = new_country_name

    def get_customer(self):
        return self.customer
    
    def get_vin(self):
        return self.unique_id

    def get_unique_id(self):
        return self.unique_id
        
    def __str__(self):
        return f'{self.unique_id:<20}{self.customer:<20}{self.vehicle_unique_id:<20}{self.start_date:<20}{self.end_date:<20}{self.country:<20}{self.employee:<20}{self.total_price:<20}'
>>>>>>> 3a9f20ebd3f51c23da9c3218b53c017ceee9991c

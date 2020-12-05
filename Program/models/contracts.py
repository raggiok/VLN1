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
=======
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
>>>>>>> d34924f5aaaf3e21e1201376dcfcab0c8cdb8067
        return contract_string
class Contract:
    def __init__(self, unique_id, customer, customer_ssn, vehicle_unique_id, start_date, end_date, country, employee, total_price, contract_creation_date, checkout_date="A", checkin_date="B", checkin_location="C", state="ACTIVE"):
        self.unique_id = unique_id
        self.customer = customer
        self.customer_ssn = customer_ssn
        self.vehicle_unique_id = vehicle_unique_id
        self.start_date = start_date
        self.end_date = end_date
        self.country = country
        self.employee = employee
        self.total_price = total_price
        self.contract_creation_date = contract_creation_date
        self.checkout_date = checkout_date
        self.checkin_date = checkin_date
        self.checkin_location = checkin_location
        self.state = state #Available states: ACTIVE DELETED INVOICED CANCELED
        
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
        return self.vehicle_unique_id

    def get_unique_id(self):
        return self.unique_id
        
    def __str__(self):
        return f'{self.unique_id:<20}{self.customer:<20}{self.customer_ssn:<20}{self.vehicle_unique_id:<20}{self.start_date}-{self.end_date:<20}{self.country:<20}{self.employee:<20}{self.total_price:<20}{self.contract_creation_date:<20}{self.checkout_date:<20}{self.checkin_date:<20}{self.checkin_location:<20}{self.state:<20}'

class Customer:
    def __init__(self, unique_id, name, ssn, address, zip_code, city, country, phone, email, state="ACTIVE"):
        self.unique_id = unique_id
        self.name = name
        self.ssn = ssn
        self.address = address
        self.zip_code = zip_code
        self.city = city
        self.country = country
        self.phone = phone
        self.email = email
        self.state = state

    def __str__(self):
        return f"{self.unique_id:<20}{self.name:<20}{self.ssn:<20}{self.address:<20}{self.zip_code:<20}{self.city:<20}{self.country:<20}{self.phone:<20}{self.email:<20}"

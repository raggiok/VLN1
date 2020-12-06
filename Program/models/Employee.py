class Employee:
    def __init__(self, unique_id, name, ssn, role, address, zip_code, city, country, home_phone, mobile_phone, email, state="Active"):
        self.unique_id = unique_id
        self.name = name
        self.ssn = ssn
        self.role = role
        self.address = address
        self.zip_code = zip_code
        self.city = city
        self.country = country
        self.state = state
        self.mobile_phone = mobile_phone
        self.home_phone = home_phone
        self.email = email

    def __str__(self):
        return f"{self.unique_id:<20}{self.name:<20}{self.ssn:<20}{self.role:<20}{self.address:<20}{self.zip_code:<20}{self.city:<20}{self.country:<20}"
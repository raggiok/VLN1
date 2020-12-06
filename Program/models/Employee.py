class Employee:
    def __init__(self, unique_id, name, age, role, address, zip_code, city, country, state="Active"):
        self.unique_id = unique_id
        self.name = name
        self.age = age
        self.role = role
        self.address = address
        self.zip_code = zip_code
        self.city = city
        self.country = country
        self.state = state

    def __str__(self):
        return f"{self.unique_id:<20}{self.name:<20}{self.age:<20}{self.role:<20}{self.address:<20}{self.zip_code:<20}{self.city:<20}{self.country:<20}"
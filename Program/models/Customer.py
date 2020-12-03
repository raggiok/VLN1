class Customer:
    def __init__(self, name, ssn,address, postnumber, phone, email, land):
        self.name = name
        self.ssn = ssn
        self.address = address
        self.postnumber = postnumber
        self.phone = phone
        self.email = email
        self.land = land

    def __str__(self):
        return f"{self.name:<20}{self.ssn:<10}{self.address:<25}{self.postnumber:<10}{self.phone:<15}{self.email:<20}{self.land:<15}"

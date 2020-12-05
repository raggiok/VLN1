class Destination:
    def __init__(self, country, airport, phone_number, opening_hours):
        self.country = country
        self.airport = airport
        self.phone_number = phone_number
        self.opening_hours = opening_hours

    def __str__(self):
        return f"{self.country:<20}{self.airport:<20}{self.phone_number:<20}{self.opening_hours:<20}"
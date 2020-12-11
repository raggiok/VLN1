class Destination:
    def __init__(self, unique_id, country, city, airport, phone_number, opening_time, closing_time, main_contact, state="ACTIVE"):
        self.unique_id = unique_id
        self.country = country
        self.city = city
        self.airport = airport
        self.phone_number = phone_number
        self.opening_time = opening_time
        self.closing_time = closing_time
        self.main_contact = main_contact
        self.state = state

    def get_destination(self):
        return self.city

    def __str__(self):
        return f"{self.unique_id:<20}{self.country:<20}{self.city:<20}{self.airport:<20}{self.phone_number:<20}{self.opening_time:<20}{self.closing_time:<20}{self.main_contact:<20}"
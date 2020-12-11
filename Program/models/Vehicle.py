class Vehicle:
    def __init__(self, unique_id, manufacturer, model, vehicle_type, status, man_year, color, license_type, location, rate, state="ACTIVE"):
        self.unique_id = unique_id
        self.manufacturer = manufacturer
        self.model = model
        self.vehicle_type = vehicle_type
        self.status = status
        self.man_year = man_year
        self.color = color
        self.license_type = license_type
        self.location = location
        self.rate = rate
        self.state = state #ACTIVE by default and becomes DELETED if Vehicle is deleted

    def get_id(self):
        return self.unique_id

    def type_of_vehicle(self):
        return self.vehicle_type

    def __str__(self):
        return f"{self.unique_id:<20}{self.manufacturer:<20}{self.model:<20}{self.vehicle_type:<20}{self.status:<20}{self.man_year:<20}{self.color:<20}{self.license_type:<20}{self.location:<20}{self.rate:<20}"
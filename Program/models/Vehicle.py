class Vehicle:
    def __init__(self, manufacturer, model, vehicle_type, status, man_year, color, licence_type, location):
        self.manufacturer = manufacturer
        self.model = model
        self.vehicle_type = vehicle_type
        self.status = status
        self.man_year = man_year
        self.color = color
        self.licence_type = licence_type
        self.location = location

    def __str__(self):
        return f"{self.manufacturer:<20}{self.model:<20}{self.vehicle_type:<20}{self.status:<20}{self.man_year:<20}{self.color:<20}{self.licence_type:<20}{self.location:<20}"
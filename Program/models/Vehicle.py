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
        return self.manufacturer + self.model + self.vehicle_type + self.status + self.man_year + self.color + self.licence_type + self.location
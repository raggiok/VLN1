class Employee:
    def __init__(self, name, age, role, address):
        self.name = name
        self.age = age
        self.role = role
        self.address = address

    def __str__(self):
        return self.name + " (" + self.age + ") - " + self.role + " - " + self.address
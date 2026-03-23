class BMW:
    brand = 'car'

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def fuel_type(self):
        print(self.name, "uses Petrol")

    def speed(self):
        print(self.name, "max speed is", self.max_speed, "km/h")


class Ferrari:
    brand = 'car'

    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def fuel_type(self):
        print(self.name, "uses Petrol")

    def speed(self):
        print(self.name, "max speed is", self.max_speed, "km/h")


# Creating objects
car1 = BMW("BMW M3", 250)
car2 = Ferrari("Ferrari 488", 340)

# Polymorphism
for car in (car1, car2):
    car.fuel_type()
    car.speed()
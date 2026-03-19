class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def __init__(self, capacity=50):
        super().__init__(capacity)

    def fare(self):
        base_fare = super().fare()
        maintenance = base_fare * 0.10
        return base_fare + maintenance


# Create Bus object
school_bus = Bus()

# Print total fare
print("Total Bus Fare:", school_bus.fare())
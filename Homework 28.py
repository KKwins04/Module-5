class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius


# Take input from user
r = float(input("Enter the radius of the circle: "))

# Create object
c1 = Circle(r)

# Display results
print("Area of the circle:", c1.area())
print("Perimeter of the circle:", c1.perimeter())
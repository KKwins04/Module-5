#Create class
class Dog:
    species = 'dog'
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

Neko = Dog("Neko", 16, "German Shepard")
Mike = Dog('Mike', 17, "Pitbull")

print("Neko is a {}".format(Neko.species))
print("Mike is a {}".format(Mike.species))
        
print("{} is {} years old".format(Neko.name, Neko.age))
print("{} is {} years old".format(Mike.name, Mike.age))

print("{} is a {}".format(Neko.name, Neko.breed))
print("{} is a {}".format(Mike.name, Mike.breed))
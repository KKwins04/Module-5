#Create class
class Parrot:

    #Class attribute
    species = 'bird'

    #Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Instantiate the parrot class
blu = Parrot("Blu", 15)
woo = Parrot("Woo", 10)

#Access the class variables
print("Blu is a {}".format(blu.species))
print("Woo is a {}".format(woo.species))

#Access the instant attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
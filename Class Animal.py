from abc import ABC
class Animal(ABC):

    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can slither and swallow objects whole")

class Dog(Animal):
    def move(self):
        print("I can bark and wag my tail when happy")

class Lion(Animal):
    def move(self):
        print("I can roar and bite with my sharp teeth")

H = Human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()

L = Lion()
L.move()
#Python program to show how parent constructors are called

#Parent class
class person(object):

    #init is known as the construtor
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    def display(self):
        print(self.name)
        print(self.id_number)

#Child class
class Employee(person):
    def __init__(self, name, id_number, salary, post):
       self.salary = salary
       self.post = post

       #Invoking the __init__ of parent class
       person.__init__(self, name, id_number)

#Creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, 'Intern')

#Calling a function of the class person using its instance
a.display()
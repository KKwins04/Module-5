#Create Class
class IOString():

    #constructor to set input value
    def __init__(self):
        self.str1 = ' '
    
    # Function to get input from user
    def get_String(self):    
        self.str1 = input("Enter String: ") 
    
    #function to print string in upper case
    def print_String(self):
        print("Result is: ",self.str1.upper())

#Object Creation
str1 = IOString()

#Call Functions
str1.get_String()
str1.print_String()
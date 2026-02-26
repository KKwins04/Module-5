#Create Class
class Employee:

    #Initialising
    def __init__(self):
        print("Employee created")

    #Calling Destructor
    def __del__(self):
        print("Destructor called")

def Create_Obj():
    print("Making Object")
    obj = Employee
    print("FUnction end")
    return obj
    
print("Calling Create_obj Function")
obj = Create_Obj()
print("Program end")
    
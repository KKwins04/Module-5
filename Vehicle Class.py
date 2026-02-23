#Create class
class Vehicle:

    #Create init method
    def __init__(self, max_speed, mileage):
        
        #Bind the arguements
        self.max_speed = max_speed
        self.mileage = mileage

#Object creation
modelx= Vehicle(240, 18)

#Access the variables inside init method
print("Model max speed: ", modelx.max_speed)
print("Model max mileage: ", modelx.mileage)
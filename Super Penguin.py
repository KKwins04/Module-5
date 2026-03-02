#Parent class
class Bird:

    def __init__(self):
        print("Bird is ready!")

    def WhoIsThis(self):
        print("Bird")

    def swim(self):
        print("Swim Faster")

    #Child class
class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is ready!")

    def WhoIsThis(self):
        super().WhoIsThis()
        print("Penguin")

    def run(self):
        print("Run Faster")

peggy = Penguin()
peggy.WhoIsThis()
peggy.swim()
peggy.run()
        

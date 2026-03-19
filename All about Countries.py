class India():
    def name(self):
        print("India")
    
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindi is the most widely spoken language in India")

    def stage(self):
        print("India is a developed country")

class United_States():
    def name(self):
        print("United States of America")
    
    def capital(self):
        print("Washington D.C. is the capital of the United States")

    def language(self):
        print("American English is the primary language in the United States")

    def stage(self):
        print("United States is a developed country")

class Singapore():
    def name(self):
        print("Singapore")
    
    def capital(self):
        print("Singapore is the capital of the Singapore")

    def language(self):
        print("British English is the primary language in the Singapore")

    def stage(self):
        print("Singapore is a developing country")

obj_IN = India()
obj_US = United_States()
obj_SG = Singapore()


for country in (obj_IN, obj_US, obj_SG):
    country.name()
    country.capital()
    country.language()
    country.stage()
    print()
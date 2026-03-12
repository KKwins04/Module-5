class myClass:

    __privateVar = 27

    def __priv_Meth(self):
        print("I am inside class myClass")

    def hello(self):
        print("Private variable value: ", myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__priv_Meth
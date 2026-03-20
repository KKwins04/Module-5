class A:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if(self.a < other.a):
            return "obj_1 is lesser than obj 2"
        else:
            return "obj_2 is lesser than obj 1"
        
    def __eq__(self, other):
        if (self.a == other.a):
            return "Both are equal"
        else:
            return "Both are not equal"
        
obj_1 = A(4)
obj_2 = A(3)
print("Passed Values: ", obj_1.a, "and", obj_2.a)
print(obj_1 < obj_2)

obj_3 = A(2)
obj_4 = A(4)
print("Passed Values: ", obj_3.a, "and", obj_4.a)
print(obj_3 == obj_4)
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __del__(self):
#         print("Object is been deconstructed!")

# p = Person("Rahul", 22)


class Vector:
    
    def __init__(self, x, y, Name="Rahul"):
        self.x = x
        self.y = y
        self.Name = Name
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y + other.y)
    
    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"
    
    def __len__(self):
        return 2
    
    def __call__(self):
        print(f"Hello {self.Name}, you called me?")
    
# v1 = Vector(10,20, "Rahul")
# v2 = Vector(30,40, "Rahul")
# v3 = v1 + v2
# print(v3)
# v3 -= v1
# print(v3)
# print(len(v3))
# v1()
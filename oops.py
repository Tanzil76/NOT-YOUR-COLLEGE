# Imperative Approach -:

a = 12
b = 13
print(a + b)

# Functional Approach -:

def addition(a,b):
    print(a + b)
addition(12,13)

# OOPS -:

# 1. Class -: it stores attributes and methods.

# Syntax of class -:
class Car:
    a = 12                             # attributes - variables that define in class is know as attributes.

    def hello():                       # Methods - functions that define in class is known as methods.
        print("Hello! How are you")

# You can access attributes 
# and methods after accessing  the class
print(Car.a)   # accessing attributes
Car.hello()    # accessing methods

# 2. Objects -:

class Bags:
    name = "Not Your College"

    def details(self):
        print("Hello this is a company who creates bag")

# Call the class inside a variable and that variable becomes an object.
# object has all the powers of a class therefore a class object can access atributes and methods of a class.
# Creating an object
obj1 = Bags()       
obj2 = Bags()

# Accessing the atrributes
print(obj1.name)
print(obj2.name)

obj1.details()

# 3. Constructor -: A constructor is a method that runs automatically when we call a class and this constructor function will target the objects location.
#  constructor function - > def __init__(self):
                              # pass

class Bags:
    def __init__(self,material,zips,pockets):     # 'self' captures objects location 
        self.material = material
        self.zips = zips
        self.pockets = pockets

# Creating an object with a value.
obj1 = Bags("Leather" , 3 , 2)
obj2 = Bags("Polyster" , 3 , 4)

# Accessing the attribute.
print(obj1.material)
print(obj2.material)
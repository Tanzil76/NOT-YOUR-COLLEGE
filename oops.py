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
print(Car.a)   # accessing attributes             # Output - 12
Car.hello()    # accessing methods                # Output - Hello! How are you

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
print(obj1.name)                     # Output - Not Your College
print(obj2.name)                     # Output - Not Your College

obj1.details()                       # Output - Hello this is a company who creates bag

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
print(obj1.material)          # Ouput - Leather
print(obj2.material)          # Output - Polyster

# 4. Attributes and Methods -:

class Animal:
    a = 12    # Class attribute - A normal variable created inside a class.

    def __init__(self,name):
        self.name = name      # Object/Instance attribute - An attribute created using an instance like self.name, self.age etc.

    def hello(self):          # Object/Instance method - Captures the location of object.
        print(f"How are you my name is {self.name}")

    @classmethod             # Decorators
    # jaise hi mai decorators lgata hu upar mai tbhi neeche wala jo method hai jo object ban skta tha lekin ab woh ek class ban gya hai.
    def details(cls):         # Class method - Captures the location of class.
        print(f"How are you my name is {cls.a}")

    @staticmethod
    def speak():              # This is a static method and it will not target any location.
        print("Hello! How are you I am a Static Method")

obj = Animal("Lion")

obj.hello()                                     # Output - How are you my name is Lion
obj.details()                                   # Output - How are you my name is 12
obj.speak()                                     # Output - Hello! How are you I am a Static Method

# 3. Inheritance -:

class Animal:             # Parent Class 
    a = 12
    def __init__(self,name):
        self.name = name

    def details(self):
        print(f"Hello your name is {self.name}")

class Humans(Animal):      # Child Class
    pass

obj1 = Animal("Lion")
obj2 = Humans("Tanzil")

obj2.details()            # Hello your name is Tanzil
print(obj2.a)             # 12

# Your Child Class objects has all the powers to access the attributes and methods of Parent Class.
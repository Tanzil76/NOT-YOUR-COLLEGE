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
    a = 12                             # attributes - variables that define in class is known as attributes.

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

# 3. Constructor -: A constructor is a method that runs automatically when we call a class and this constructor function will target the 
# objects location.
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

# 5. Inheritance -: It works between classes.
# Benefits of using Inheritance -:
# i. Code reusability
# ii. Organized structure
# iii. Easy to maintain and extend

class Animal:             # Parent Class 
    a = 12
    def __init__(self,name):
        self.name = name

    def details(self):
        print(f"Hello your name is {self.name}")

# Syntax of Inheritance -: Take parameters in functions here you will take parameters but those parameters will be classes.
class Humans(Animal):      # Child Class - Now the inherited class has all the powers of parent class that means all the methods, attributes can be accessed by the instance of child as well.
    pass

obj1 = Animal("Lion")
obj2 = Humans("Tanzil")

obj2.details()            # Hello your name is Tanzil
print(obj2.a)             # 12

# Your Child Class objects has all the powers to access the attributes and methods of Parent Class.

# Solve -:

class BagFactory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def details(self):
        print("Your bag details are -: ")
        print(self.material)
        print(self.zips)
        print(self.pockets)

class Reebok(BagFactory):
    def __init__(self, material, zips, pockets,color):            # color - extra add
        super().__init__(material, zips, pockets)                 # super() - access the parent class.
        self.color = color 
    
    def details(self):
        print(self.color)
        return super().details()

bag1 = BagFactory("Leather",3,4)
bag2 = Reebok("Polyster",4,2,"black")

bag2.details()
print(bag1.material)
print(bag2.color)

# Multiple Inheritance -:

class Animal:
    def __init__(self,name):
        self.name = name
    
class Humans:
    def __init__(self,id):
        self.id = id

# Multiple Inheritance means there will be 2 parent classes and only 1 child class and the child class will inherit all the attributes 
# and methods of both parents. The Constructor function will be inherited of the first class that has been inherited. This is MRO(Method 
# Resolution Order) followed by python. 
class Robots(Humans,Animal):
    def __init__(self, id,name):
        Humans.__init__(self,id)
        Animal.__init__(self,name)

robo = Robots(12,"Tanzil")
print(robo.id)
print(robo.name)

# 6. Polymorphism -:

class Animal():
    def speak(self):
        print("Animals will not speak")

class Humans:
    def speak(self):
        print("We are humans we can speak")

obj1 = Animal()
obj2 = Humans()

obj1.speak()             # Animals will not speak
obj2.speak()             # We are humans we can speak


# Method Overriding -: we need innheritance

class Animal:
    a = 12
    def __init__(self,name):
        self.name = name

    def details(self):
        print(f"Your name is {self.name}")

class Humans(Animal):     # Here inheritance is used.
    b = 12
    def details(self):
        # super().details() -: this is for calling animal class method.
        print(f"Your info is {self.name} and this is all we have")

obj = Humans("Tanzil")
# This only calls Humans class methods.
obj.details()                        # Output -: Your info is Tanzil and this is all we have

# When we are doing inheritance and parent and child classes have same method name so the child class method will override your parent 
# class method.

# 7. Encapsulation -:  It keeps data safe from being changed by mistake. It makes your code clean easy to use. It gives control over what
#  others can access or change.

# Access Modifiers -:

# i. Public Attributes and Methods - Till now every attributes and methods we have created are public means the inherited classes and 
# objects can access them no matter what.
class Factory:
    name = "Kia"  # Public class attribute

    def __init__(self,type,tyre,color):
        self.color = color        # Public object attribute
        self.tyre = tyre
        self.type = type

    def details(self):        # Public method
        print("Hello your details are -: ")

obj = Factory("Sedan","MRF","Black")

print(obj.name)            # Kia

# ii. Private Attributes and Methods - It cannot be accessed from outside the class - only from inside the class where it is defined. 
# In Python, we use two underscores(__) before the name to make it private.
class Factory:
    __name = "Kia"     # Private class attribute

    def __init__(self,type,tyre,color):
        self.__color = color        # Private object attribute
        self.__tyre = tyre
        self.__type = type

    def __details(self):        # Private method
        print("Hello your details are -: ")

obj = Factory("Sedan","MRF","Black")

#print(obj.__name)

# 8. Abstraction -: Abstraction does not exist in python but we can achieve it using a library we will see what is a library later. 
# Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecessary details. 
# It is used to define a common inteface for different classes.

# Abstract classed and methods -: Abstract classes that contains one or more abstract methods. A method that is defined but not 
# implemented in the abstract clas. subclasses must provide the implementation.
from abc import ABC , abstractmethod

class enforce(ABC):
    @abstractmethod
    def enginestart():
        pass


class bike(enforce):
    def enginestart():
        pass 

class car(enforce):
    def enginestart():
        pass

class truck():
    pass 

obj1 = bike()
obj2 = car()
obj3 = truck()



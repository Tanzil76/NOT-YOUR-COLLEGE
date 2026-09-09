# Decorators -: A decorator is just a function that modifies another function without changing its actual code.
               # For creating a decorator you first have to create a decorator functions and then inside that we will create a wrapper.
def extragreeting(func):
    def wrapper():
        print("Helllo from the NYC team")
        func()
        print("Thank You visit again")

    return wrapper

# This is Decorators -:
@extragreeting
def greetings():
    print("Good Morning")

greetings()

# Ouput -: 

# Hello from the NYC
# Good Morning 
# Thank You visit again

# Args -: specail keyword inpython used in function definitions to accept a flexible number of arguments.
          # so *args are used for multiple positional arguments.
def addition(*args):
    s = 0
    for i in args:
        s = s + i
    return s

print(addition(20,30,50,39,5,6,78,90))
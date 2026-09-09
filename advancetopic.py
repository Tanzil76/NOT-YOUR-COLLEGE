# Decorators -:

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

# Args -:

def addition(*args):
    s = 0
    for i in args:
        s = s + i
    return s

print(addition(20,30,50,39,5,6,78,90))
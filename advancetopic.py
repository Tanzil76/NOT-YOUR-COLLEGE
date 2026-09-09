# Decorators -:

def extragreeting(func):
    def wrapper():
        print("Helllo from the NYC team")
        func()
        print("Thank You visit again")

    return wrapper

@extragreeting
def greetings():
    print("Good Morning")

greetings()

# Ouput -: 

# Hello from the NYC
# Good Morning 
# Thank You visit again
          
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

# Args -: specail keyword in python used in function definitions to accept a flexible number of arguments.
          # so *args are used for multiple positional arguments.
def addition(*args):
    s = 0
    for i in args:
        s = s + i
    return s

print(addition(20,30,50,39,5,6,78,90))
#  Note -: args create tuple

# Kwargs(Keywordsarguments) -: kwargs are used for multiple key word arguments.
# Note -: keywords arguments create dictionary then ,after in dictionary we pass keys and values pairs.

def info(**kwargs):
    return kwargs

print(info(name = "Tanzil", age = 24, profession = "A.I. Engineer"))

# Important -:

a = 20

# if a % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

# ternary operation - : mtlb ek line mai if else ka condition print krna.
# sbse pehle jo print krna hai woh likhenge ,uske baad condition likhenge, fir jo print nhi hona hai woh likhenge.

print("even number") if a % 2 == 0 else print("odd number")

# List Comprehension -: 

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# sbe jo add krna hai list mai woh likhnege fir uske baad loop chalainge fir if-else condition check karenge.
b = [i for i in a if i % 2 == 0]

print(b)
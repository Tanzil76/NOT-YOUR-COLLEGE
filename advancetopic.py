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

# Comprehension -:

# List Comprehension -: 

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# sbe jo add krna hai list mai woh likhnege fir uske baad for loop chalainge fir if-else condition check karenge.
b = [i for i in a if i % 2 == 0]

print(b)

# Lambda function - : A lambda function is an anonymous, inline function defined using the lambda keyword.
            # It's often used for short, simple functions that are used only once or temporarily.

# def addition(a,b):
#     print(a + b)
# addition(12,13)

 # sbse pehle ek varibale banayenge , fir lambda expression likhenge , fir paramter denge, fir jo print krna hai woh likhenge.
addition = lambda a,b : a + b
print(addition(10,20))

# map() function -: Map is used for applying a function to multiple items. Takes a list (or any sequence). Applies the same function to 
# every item in that list. Gives you back a new list (in Python 3, it gives a map object which you can convert to a list. Use map() when 
# you want to transform every item in a list.

a = ["Tanzil" , "Kaif" , "Danish"]

length = list(map(len,a))
print(length)                # [6, 4, 6]

# filter() function -:  Filter as the name suggest is used to filter out the stuff. Takes a list (or other sequence). Checks each item 
# using a function (a test). Keeps only the items that pass the test (i.e., return True) 

m = [35,80,40,12,60]

# pehle ek varible banao, uske baad list banao, fir filter function lgao, uske baad lamba expression lgao, paramter daalo, fir condition 
# daalo , jiss pr condition chalana hai woh likho.
passed = list(filter(lambda x : x >= 40, m))

print(passed)

# zip() function -: binding two list.

name = ["Tanzil" , "Kaif" , "Danish"]
marks = [12,90,42,6,60]

result = list(zip(name,marks))

print(result)       # [('Tanzil', 12), ('Kaif', 90), ('Danish', 42)]

# Functions - A function is a reusable block of code with a name. Instead of writing the same logic 10 times, you write it ince as a fucntion and call it 10 times.
# Two functions -: 

# Pre-defined - print(), float(), int(), input(), len()
            
# User-defined -: def - you want to define a function or create a new function.

# Solve -:

def hello():
    print("Hello how are you")
    print("Welcome To NYC")
hello()                    # Function call here.


def addition(a,b):
    print(a + b)

addition(13,25)
addition(50,50)

# Check palindrome using function.

def palindrome_checker(a):
    copy = a
    rev = 0

    while a > 0:
        rev = rev * 10 + a % 10
        a = a // 10
    if copy == rev:
        print("Palindrome number")
    else:
        print("Not a Palindrome")
palindrome_checker(121)

# Types of Arguments -:

# 1. Positional arguments-

def multiplication(a,b,c,d):
    print(a * b * c * d)
multiplication(5,2,3,6)

# 2. Default arguments-

def addition(a,b,d,c = 12):
    print(a + b + c + d)
addition(5,5,5)

# 3. Keyword arguments-

def subtraction(a,b,c):
    print(b-a-c)
subtraction(20,c = 40, b = 34)

# return -: print inside a function 

def hello():
    return "How are you"
b = hello()
print(b)
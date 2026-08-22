#If-else statements -:

if True:
    print("My name is Tanzil") # My name is Tanzil

# You have to input of age and tell the person can vote or not

age = int(input("Please tell your age :-"))
if age >= 18:
    print("Hello brother you can vote")
else:
    print("Hello you can not vote sorry")

rupees = int(input(" Give money - "))
if rupees == 10:
    print("I will have a chocobar")
elif rupees == 50:
    print("I will have manchurian")
elif rupees == 100:
    print("Mcd")
elif rupees == 500:
    print("5 Star dhaba")       
else:
    print("Bhuka rahu ga mai") 

# Solve :

# 1. Accept two numbers and print the greatest between them.

num1 = int(input("Please give me me first number :- "))
num2 = int(input("Please give me me second number :- "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both the numbers are equal")

# 2.

gender = input("Please tell your gender in (M or F) :- ")

if gender == "M" or gender == "m":
    print("Hello Sir")
elif gender == "F" or gender == "f":
    print("Hello Mam")
else:
    print("Others")
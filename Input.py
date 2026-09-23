name = "Tanzil"
age = 23

# print string using variable in string - print(f"string {variable} string {variable}") - formatted string
# {}- python expect to provide some value
print(f"Hi my name is {name} and my age is {age}")   # Using f-string

# Other way - Using multiple values - print("string",varibale,"string",variable)
print("Hi my name is",name,"and my age is",age)

# Input -: input() always returns a string. If you need a number, convert it manually with int() or float().

age = input("What is your age -: ")
print(f"Hello your age is {age}")

# Converting age to integer due to some specific reason
age = int(input("What is your age -: "))
print(f"Hello your age is {age}")
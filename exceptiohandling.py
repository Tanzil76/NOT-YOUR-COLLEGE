# Exception Handling -:

a = int(input("Please give 1st number -: "))
b = int(input("Please give 2nd number -: "))

try:
    print(a/b)
except Exception as err:
    print(f"Sorry an error occured as {err}")

name = input("Tell name -: ")

print(f"Hello my name is {name}")
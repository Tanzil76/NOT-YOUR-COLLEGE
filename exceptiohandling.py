# Exception Handling -:

a = int(input("Please give 1st number -: "))
b = int(input("Please give 2nd number -: "))

# in python code runs line by line means - agr koi line mai error hai toh aage ka line execute nhi hoga isliye.
# isme hum log "try and except" use krte hai ki aage ka line execute ho jaaye agr koi error hai toh.
# aap yeh wale code mai dekh skte hai isme aisa hi hua hai. 

try:
    print(a/b)
except Exception as err:
    print(f"Sorry an error occured as {err}")

name = input("Tell name -: ")

print(f"Hello my name is {name}")
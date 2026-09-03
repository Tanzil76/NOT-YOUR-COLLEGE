# File Handling -: 
# File modes -:

  # 'r' -: read only

 # they create files -:
  # 'w' -: write(overwrite!) | 'a' -: append to end | 'x' -: create(fails if exists)

# This will create a file.
#open("Hello.txt","x")

# This helps to write data in file -:

# file = open("Python.txt","w")

# data = input("What you want to write in your file -: ")

# file.write(data)

file = open("Python.txt","r")
print(file.read())
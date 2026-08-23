# Loops -:

# range() function -: 

    # range() generates a sequence numbers. Think of its saying "count from here to there"

    # range(stop) - 0 up to stop-1
    # range(start, stop) - start up to stop-1
    # range(start, stop, step) - start, jumping by step

range(10, 101, 1)
range(23, 57, 1)
range(46)

# For loop -:

 # For numbers -:

  # Syntax - for i in range(start, stop, step):

for i in range(46):
    print(i)

# Print table of 5

n = int(input("Tell your number -: "))
for i in range(n, (n*10)+1, n):
    print(i)

 # For Strings -:

a = "Students"

for i in a:
    print(i)        # S t u d e n t s

for i in range(len(a)):  # (0, len(a), 1) -: default value -: len() is size of string.
    print(f"{i} : {a[i]}")
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

  # Syntax - for i in range(start, stop, step)

for i in range(46):
    print(i)

# Print table of 5

n = int(input("Tell your number -: "))
for i in range(n, (n*10)+1, n):
    print(i)
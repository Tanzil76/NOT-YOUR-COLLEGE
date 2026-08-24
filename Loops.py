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

   # break -: stops the loop
for i in range(1, 11):
    if i == 5:
        break
    print(i)   # 1 2 3 4 

   # continue -: jump from the value
for i in range(1, 11):
    if i == 5:
        continue
    print(i)     # 1 2 3 4 6 7 8 9 10

   # else -: it works with break means if break works else will not work and if break dosen't work then else work.
for i in range(1, 11):
    if i == 45:
        break
    print(i)  
else:
    print("no break was encountered")

 # Solve

# 1. Print "Hello World" n times.

n = int(input("Tell your number -: "))
for i in range(n):
    print("Hello World")

# 2. print natural numbers form 1 to n.

n = int(input("Tell how many natural numbers you want -: "))
for i in range(1,n+1):
    print(i)

# 3. Reverse for loop - print n down to 1.

n = int(input("Tell your number -: "))
for i in range(n,0,-1):
    print(i)

# 4. Print the multiplication table of a number.

n = int(input("Which number of table we want -: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

# 5. Sum of first n natural numbers.

s = 0
n = int(input("Tell how many natural numbers sum we want -: "))
for i in range(1,n+1):
    s = s + i
print(s)

# 6. Factorial of a number.

m = 1
n = int(input("Give number for factorial -: "))
for i in range(1,n+1):
    m = m * i
print(m)

# 7. Print sum of all even and odd numbers in a range separately.

n = int(input("Give number -: "))
evensum = 0
oddsum = 0

for i in range(1, n+1):
    if i % 2 == 0:
        evensum = evensum + i
    else:
        oddsum = oddsum + i
print(f"Even Sum is {evensum} and Odd Sum is {oddsum}")

# 8. Print all factors of a number.

n = int(input("Give number -: "))
for i in range(1,n+1):
    if n % i == 0:
        print(i)

# 9. Check if a number is perfect(sum of factors = the number itself.)

n = int(input("Give number -: "))

s = 0
for i in range(1,n):
    if n % i == 0:
        s = s + i
if s == n:
    print("Perfect number")
else:
    print("Not a perfect number")    

# 10. Check if a number is prime.

n = int(input("Give a number -: "))
count = 0
for i in range(1,n+1):
    if n % i == 0 :
        count = count + 1
if count == 2:
    print("Prime number")
else:
    print("Composite number")
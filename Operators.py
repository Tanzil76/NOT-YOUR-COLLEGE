#Arithmetic Operators - work on int, float, complex - follows bodmas rule
#(+, -, /, //-floor divison, *, **-power, %-mod)

a = 10
b = 20
c = 12
d = 56
print(a+b+c + d +23 + 56)

a = 34
print(a - 12)

a = 12
print(int(a/2)) 

a = 15
print(a//2) # if we divide it converts float to integer

print(12*12)

print(15**2) # it gives power to the number means like 15^2 = 225

print(37%5) # it gives remainder after division

"""
Bodmas Rule -:

1. () - brackets
2. ** - Exponent (right to left: 2**2**3 = 2**(2**3))
3. *, /, //, % - Multiplication, Divsion, Modulus
4. +, - - Addition, Subtraction
"""
# left to right - because all execute at same time
print(10 / 2 * 5)
print(10 * 2 / 5)

# Solve -:

print(3 + 4 * 2)             # 11
print(15 // 4 + 15 % 4)      # 6
print(3 + 2 ** 2 * 5 - 1)    # 22

# Comparison Operators -:

#(==. >, <, >=, <=, !=)

print(16 == 16)        # True

print(12 > 14)         # False

print(12 < 45)         # True

print(12 >= 12)        # True

print(45 <= 56)        # True

print(23 != 23)        # False

# Logical Operators -:

# and, or and not

# and - same answer then it will give true and if one answer is different it will give  whole false.
print(12 > 10 and 34 == 34 and 10 > 20) # False

# or - if one of the answer is true and others are false then it give true.
print(34 == 45 or 12 == 12 or 67 == 69) # True

# and - it change the answer if true convert to false and vice - versa.
print(not 12 == 34) # True

# Solve -:

print((5 > 3 and 10 == 10) or (4 != 4 and 2 < 1))  # True

print((10 == 10 and 23 != 23) or (34 == 12 and bool("hello"))) # False

print(not(5 == 5 and 3 != 4) or (10 > 20)) # False

# Assignment Operators -: are used to assign values to variables.

# += - add and assign, -= - subtract and assign, *= - multiply and assign , /= - divide and assign, //= - floor divide and assign, %= - modulus and assign, **== - power and assign

a = 10
a += 10
a += 10

print(a) # 30
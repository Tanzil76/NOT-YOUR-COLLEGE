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

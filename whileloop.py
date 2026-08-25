# While Loop -: the while loop keeps running as long as a condition is True. You use it when you don't know how many times you'll need to repeat.

# Always make sure your condition will eventually become False - otherwise your program runs forever.

# While loops also support - BREAk , CONTINUE and ELSE.

a = 1
while a != 20:
    print(a)
    a = a + 1

# Solve -:

# 1. Separate each digit of a number and print on a new line.

a = 456
print(a % 10)
a = a // 10
print(a % 10)
a = a // 10
print(a % 10)


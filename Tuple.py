# Tuple -: Exactly like a list , except you cannot change it once created. It is immutable nature. Use on constant data - days of the week, coordiantes or config. values.
   #   0     ,     1    ,  2 ,  3 ,  4 ,  5 ,  6
a = ["Monday", "Tuesday", 123, 567, 123, 123, 123]

tup = tuple(a)
print(type(tup))  
print(tup[0])
print(tup[-1])

# Methods -: 

# 1. index -  tup.index("string") - find index of a value.

print(tup.index("Monday"))

# 2. count - tup.count(how many times value repeat - count it).

print(tup.count(123))
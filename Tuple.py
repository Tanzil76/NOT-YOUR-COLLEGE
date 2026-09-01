# Tuple -: Exactly like a list , except t=you cannot change it once created. It is immutable. Use on constant data - days of the week, coordiantes or config. values.
   #   0     ,     1    ,  2 ,  3
a = ["Monday", "Tuesday", 123, 567]

tup = tuple(a)
print(type(tup))  
print(tup[0])
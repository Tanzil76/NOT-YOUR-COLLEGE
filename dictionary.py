# Dictionary -: keys and values -> {key:value}

# Vanilla python -:

# 1. reading a value -:

d = {10:100,20:200,30:300,40:400}       # 10,20,30,40 -> they are keys | 100,200,300,400 -> they are values of keys.
print(d[10])                     # 100

# 2. creating a new key value pair -:

d[50] = 500
print(d)                         # {10:100,20:200,30:300,40:400,50:500}

# 3. updating a key value that already exist -:

d = {10:11,20:200,30:300,40:400} 
d[10] = 100
print(d)

# Methods Approach -:


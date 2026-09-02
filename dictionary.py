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
print(d)                         # {10:100,........}

# Methods Approach -:

# clear() -: clears all the elements in dictionary.

d = {10:100,20:200,30:300,40:400} 
d.clear()
print(d)

# fromkeys() -: returns a dictionary with the specific keys and value.

q = d.fromkeys([10,20,30,40],50)
print(q)                          # {10:50,20:50,30:50,40:50}

# get() -: d.get() and d[] both are same.

d = {10:100,20:200,30:300,40:400} 
print(d.get(10))                   # 100

# items() -: returns a list containing the dictionary's key.

print(d.items())

# pop() -: pop elements from specified keys.

print(d.pop(20))                    # 200

# popitem() -: remove last element.

print(d.popitem())
print(d)

# setdefault() -: give new key value pair.

d = {10:100,20:200,30:300,40:400} 
print(d.setdefault(60,3000))
print(d)

# update() -:

d = {10:100,20:200,30:300,40:400} 
print(d.update({10:1000}))
print(d)
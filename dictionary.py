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

# update() -: update and create key value pair.

d = {10:100,20:200,30:300,40:400} 
print(d.update({10:1000}))
print(d.update({50:500}))
print(d)

# Traversing (loops) -:

d = {10:100,20:200,30:300,40:400} 

for i in d:   # i iterates on keys.
    print(f"key {i} : value {d[i]}")


# Solve -:

# 1. Merge two dictionaries into one.

d1 = {"a":10,"b":20,"c":30} 
d2 = {"d":40,"e":50,"f":60}

for i in d2:
    d1[i] = d2[i]
print(d1)
 
# sbse pehle d2 mai i chalega d pr 
# pr fir uske baad d1[i] -> d1[d] - yeh new key ban gya d1 mai
#  fir d2[i] -> d2[d] = 40 ho jayega iska mtlb jo naya key bana hai usme d1[d] usme 40 assign ho jayega 
# fir ek ek krke sb ho jayega vice-versa.
# print hoga {'a':10,'b':20,'c':30,'d':40,'e':50,'f':60} 

# 2. Sum all values in a dictionary.

d1 = {"a":10,"b":20,"c":30}
sum = 0

for i in d1:
    sum = sum + d1[i]
print(sum)                  # 60

# 3. Count the frequency of each element in a list using a dictionary.

l = ["a","b","c","a","b","c","a","b","c"]
d = {}

for i in l:
    if i in d.keys():
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)                   # {'a':3,'b':3,'c':3}

# 4. Combine two dicts, adding values for common keys.

d1 = {"a":10,"b":20,"c":30} 
d2 = {"c":40,"e":50,"f":60}

for i in d2:
    if i in d.keys():
        d1[i] = d1[i] + d2[i]
    else:
        d1[i] = d2[i]
print(d1)                 # {'a':10,'b':20,'c':70.'e':50,'f':60}



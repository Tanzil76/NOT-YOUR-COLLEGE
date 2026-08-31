# List - Use square bracket "[]".

a = [12,23,45,67,89]
# 1. Ordered nature you can access any element at any point of time.
print(a[1])

# 2. mutable nature - you can change any values on your list.
l = [10,22,30,40,50]
l[1] = 20
print(l)

# 3. It can be accessed- access  by index.
# 4. It can store duplicate values.

# Traversing on list -:

a = [10,20,30,40,50]

# 1. Traversing on Values.

for i in a:
    print(i)  # 10 20 30 40 50

# 2. Traversing on index.

for i in range(0,len(a)):
    print(f"{i} : {a[i]}")   # 0 : 10  , 1 : 20  , 2 : 30  , 3 : 40  , 4 : 50
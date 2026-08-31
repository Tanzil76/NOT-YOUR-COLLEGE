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

for i in range(0,len(a)):     # len(a) - means length of a list 
    print(f"{i} : {a[i]}")   # 0 : 10  , 1 : 20  , 2 : 30  , 3 : 40  , 4 : 50

# append method -: list.append(value) - adding new element in list in the end.

a = [10,20,30,40,50]
a.append(60)   # adds a value to the last spot
a.append("Hello")
print(a)     # [10,20,30,40,50,60,'Hello']

# insert method -: list.insert(index,add value) - add values in the middle.

a = [10,20,40,50]
a.insert(2,30) 
print(a)     #  [10,20,30,40,50]

# pop method -: list.pop(index) - remove or pop value from the list.

l = [10,20,30,40,55,50]
a = l.pop()    # default index value "-1".
print(l)
print(a)

# remove method -: list.remove(element value) - remove element

l = [10,20,55,30,40,55,50]
l.remove(55)
print(l)

# sort method -: sort list

# i. For ascending order -:

l = [29,45,67,12,90,34]
l.sort()
print(l)

# ii. For Descending order -:

l = [29,45,67,12,90,34]
l.sort(reverse=True)
print(l)

# Solve -:

# 1. Print all positive and negative elements seaprately.

l = [3,-1,4,-5,9]
pos = []
neg = []

for i in l:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

print(f"Positive Elements -: {pos}")
print(f"Neagtive Elements -: {neg}")

# 2. Find the mean (average) of all list elements.

l = [10,20,30,40]
sum = 0

for i in l:
    sum = sum + i

print(f"Average is {sum/len(l)}")

# 3. Find the greatest element and print its index.

l = [4,8,2,9,1]
largest = l[0]
index = 0

for i in range(len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i

print(f"Largest value is {largest} at index {index}")

# 4. Find the second largest element.

a = [4,8,2,9,1]
largest = a[0]
sec_largest = a[0]

for i in a:
    if i > largest:
        sec_largest = largest
        largest = i

print(sec_largest)
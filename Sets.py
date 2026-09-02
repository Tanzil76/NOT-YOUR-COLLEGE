# Sets -: A set automatically removes duplicates and has no guaranteed order. Great for checking membership and performing math-style set operations. It stores using hash values.use -{} for set representation.

l = [1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9]

s = set(l)      # convert list into set
print(s)        # {1,2,3,4,5,6,7,8,9}

# See hash value -:

s = "Hello"

print(hash(s))

# Only hashable values we should store in sets.

s = {1,"Hello", (1,2,3)}

# Set is unordered means - which one execute first python don't know.

l = {10,20,30,40}

for i in l:
    print(i)     # 40 10 20 30

# Methods -:

s = {10,20,30,40}

# 1. add() -:

s.add(60)
print(s)       # {40,10,20,60,30}

# 2. clear() -:

s.clear()
print(s)        # set()

# 3. discard() -:

s = {10,20,30,40}

s.discard(30)
print(s)        # {40,10,20}

# 4. pop() -: remove an element from set. (randomly popped)

s = {10,20,30,40}

a = s.pop()
print(s)       # {10,20,30}
print(a)       # 40

# 5. difference() -:  shortcut -> "-" -> returns a set containing the difference between two or more sets.

s1 = {10,20,30,40}
s2 = {30,40,50,60}

print(s1.difference(s2))     # print(s1-s2) = {10,20}
print(s2.difference(s1))     # print(s2-s1) = {50,60}

# 6. difference_update() -: shortcut -> "-=" -> removes the items in this set that are also included in another, specified set.

s2 -= s1
print(s2)                    # {50,60}

# 7. intersection() -: "&" -> 

s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s1 & s2)          #  print(s1.intersection(s2)) -> {40,30}

# 8. intersection_update() -: "&=" ->

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s1 &= s2
print(s1)              # {40,30}

# 9. issubset() -: "<=" ->

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = {30,40}
print(s3 <= s2)           # True
print(s2 >= s3)           # True

# 10. symmetric_difference() -: "^" ->

s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s1 ^ s2)            # {10, 50, 20, 60}

# 11. union() -: "|" ->

print(s1 | s2)            # {40,10,50,20,60,30}


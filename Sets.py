# Sets -: A set automatically removes duplicates and has no guaranteed order. Great for checking membership and perorming math-style set operations. It stores using hash values.use -{} for set represenatation.

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

# 1. add -:

s.add(60)
print(s)       # {40,10,20,60,30}

# 2. clear -:

s.clear()
print(s)        # set()

# 3. discard -:

s = {10,20,30,40}

s.discard(30)
print(s)        # {40,10,20}

# pop -:

s = {10,20,30,40}

a = s.pop()
print(s)
print(a)
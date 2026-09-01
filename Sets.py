# Sets -: it stores using hash values.use -{} for set represenatation.

l = [1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9]

s = set(l)      # convert list into set
print(s)        # {1,2,3,4,5,6,7,8,9}

# See hash value -:

s = "Hello"

print(hash(s))

# Only hashable values we should store in sets.

s = {1,"Hello", (1,2,3)}
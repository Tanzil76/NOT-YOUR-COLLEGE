# Find unique code -: print(ord(variable))

a = " "
print(ord(a))

#Indexing -: print(variable[index])

a = "COLLEGE"
#Positive indexing - 0 to 1
print(a[6])

#Negative indexing - -1 to negative infinity from right to left
print(a[-1])
print(a[6],a[-1]) 

#Slicing -: take out some part or portion of string - print(variable[start:stop:step]) 
            # start - index starts , stop - index stops + 1 , step - taking steps

a = "COLLEGE"

#LEG-
print(a[3:6:1])

#CLEE-
print(a[0:7:2])

#default value - start - 0 - by default , stop - 7- by default
print(a[::2])

#Task -:
a = "This is Not Your College"

#Not-
print(a[8:11:1])

#College-
print(a[17:24:1])

#Type Conversion -:

#if we have  to convert string into integer - use this int()
a = "12" #string
b = int(a) #integer
print(a)
print(b)
print(type(a)) #str - output
print(type(b)) #int - output
# we can convert string if it holds valid integers

# we can convert float values to int
a = 12.5 
a = int(a) 
print(a)

#bool()-       7 values will be false -: false, 0, 0.0, "", [], (), {}
a = 12
b = 0
c = 12.4
d = 0.0
e = ""
f = "hello"
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))
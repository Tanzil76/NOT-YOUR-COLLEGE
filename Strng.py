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
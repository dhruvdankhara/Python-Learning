# if you write tup = (1) then this is int you need to write like this, tup = (1,)
# tuples is unchangeable / immutable
tup = (1,2,3,4,"red", True) 
print(type(tup))
# tup[0] = 0 # this throw error
print(tup)
print(tup[0])
print(tup[-1])  # all this type of function like list
print(tup[2])
print(tup[3])
print(tup[4])

if 4 in tup:
    print("yes")
else:
    print("no")


# we can do slice of tuple but it return new tuple
tup2 = tup[1:5]   # all other method like list
print(tup2)













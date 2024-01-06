# set not contain dublicate item
# set item will not chnage / unchangable
# they store multiple item in single variable 
# set is unorder collection of element 
# made using {}
s = {1,2,3,4,2,3,True,"dhruv"}  # here 1 == true
print(type(s))  #output in random order
print(s) # ouput order charge able

s1 = {}
print(type(s1))

s1 = set()  # we create empty set like this
print(type(s1))

for i in s:
    print(i)
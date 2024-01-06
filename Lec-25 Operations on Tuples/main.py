# we can change in tuple using this method
# tup = (1,2,3,4,5,6)
# print(tup)
# temp = list(tup)
# temp.append(7)
# temp.pop(3)
# temp[2] = 22
# tup = tuple(temp)
# print(tup)



# tup1 = (1,2,3,4)
# tup2 = (5,6,7,8)
# tup3 = tup1 + tup2
# print(tup3)



tup1 = (1,2,3,4,33,3)

# count() : count the item present how many times in tuple
print(tup1.count(3))

# index(element : start : end) : say element is avaliable in tuple first time in index
print(tup1.index(4))  # we can also do start and end point

# len()
print(len(tup1))
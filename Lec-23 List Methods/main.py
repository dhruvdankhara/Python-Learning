list = [1,2,3,4,5]
# append()  : add element at the end of list
list.append(6)
print(list)


# sort() : sort element
list = [10,21,85,65,21,8]
list.sort()
list.sort(reverse=True)  # sort in decending order
print(list)


# reverse() : reverse list item
list = [4,3,2,1]
list.reverse()
print(list)

# index : find element on which index
print(list.index(3))


# count : count how many times element have in list
list = [4,3,2,1,2,5,3,2,2]
print(list.count(2))


# this is to know in python
# in python we not copy list m is the referance of l 
# so, we can maniupulate list l from m;
l = [1,2,3,4,5]
m = l
m[0] = 0
print(l)
# so we use copy()

# copy() : copy list from 
list = [1,2,3,4,5,6,7]
m = list.copy()
print(m)


# insert() : insert element at any posistion
list = [1,2,3,4,5,6,7]
list.insert(1,1111)
print(list)


# extend() : this add entire list of tuple to any list
a = [1,2,3,4,5]
b = [6,7,8,9,0]
c = a + b # this is another way to joint list and create new list
a.extend(b)
print(a)
print(c)


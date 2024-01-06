s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7,8}
s3 = s1.union(s2)  # this is for all
print(s3)
s1.update(s2) # s2 values added to s1
print(s1)

s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7,8}
print(s1.intersection(s2)) # for one time
s1.intersection_update(s2)  # for upadate
print(s1)


s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7,8}
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)  # for upadate
print(s1)


s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7,8}
print(s1.difference(s2))
print(s2.difference(s1))
s1.difference_update(s2)  # for upadate
print(s1)


s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7,8}
print(s1.isdisjoint(s2))  # set has no intersection


s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7,8}
print(s1.issuperset(s2))  # set 2s all element in set 1
print(s1.issubset(s2))  # set 1s all element in set 2



# add() : add eleemtn in set
s1 = {1,2,3,4,5}
s1.add(6)
print(s1)


# remove() / discard() : remove item in set
# remove() : throw error if item not present in set
# discard() : don`t throw error evenif item not present in set
s1 = {1,2,3,4,5}
s1.remove(3)
print(s1)


# pop() : pop remove any element from set
# it return removed element
s1 = {1,2,3,4,5,"dhruv"}
item = s1.pop()
print(s1)
print(item)


# del : delete entire set
s1 = {1,2,3,4,5,"dhruv"}
print(s1)
del s1
# print(s1)


# clear() : this delete set items
s1 = {1,2,3,4,5,"dhruv"}
s1.clear()
print(s1)



s1 = {1,2,3,4,5,"dhruv"}
if "dhruv" in s1:
    print("yes")
else:
    print("no")



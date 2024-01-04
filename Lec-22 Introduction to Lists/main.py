# # extra item can add in list BUT we can`t add extra item in tuple
# l = [1,2,3,"dhruv",True]
# print(l)
# print(type(l))
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[-2])  # negative indexing
# print(l[len(l)-2])

# if 4 in l :
#     print("yes")
# else:
#     print("no")

# if "ruv" in "dhruv":
#     print("yes")
# else:
#     print("no")


# l = [1,2,3,"dhruv",True]
# print(l[:])
# print(l[1:])
# print(l[1:-1])
# print(l[1:4])
# print(l[1:4:2])  # jump index




# List Comprehension
list = [i*i for i in range(4)]
print(list)

list = [i for i in range(10) if i%2 == 0]
print(list)
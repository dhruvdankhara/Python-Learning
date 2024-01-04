# def avg(a, b):
#     print("average is :", (a+b)/2)

# avg(1,3)

# def avg(a = 5, b = 4):
#     print("average is :", (a+b)/2)

# avg()

# def avg(a = 5, b = 4):
#     print("average is :", (a+b)/2)

# avg(1,3)

# def avg(a = 5, b = 4):
#     print("average is :", (a+b)/2)

# avg(1)

# def avg(a = 5, b = 4):
#     print("average is :", (a+b)/2)

# avg(b = 1)

# we can change order of arguments
# def avg(a, b):
#     print("average is :", (a+b)/2)

# avg(b = 1, a = 9)

# we need to pass value in function
# def avg(a, b):
#     print("average is :", (a+b)/2)

# avg(a = 1)


# give arugment as tuple: 
def avg(*nums):
    print(type(nums))
    sum = 0
    for i in nums:
        sum = sum + i
    return sum
    # print("average is :", sum / len(nums))
ans = avg(5,6,4,6,2,4)
print(ans)


# # give argument as dictanry
# def name(**name):
#     print(type(name))
#     print("name is :", name["fname"], name["lname"])
# name(fname = "dhruv", lname = "dankhara") # call : = this called key-value pair

# def name(fname, mname = "shah", lname = "patel"):
#     print("name is :", fname, mname, lname)

# name("dhruv")

# def name(fname, mname = "shah", lname = "patel"):
#     print("name is :", fname, mname, lname)

# name("dhruv","raj")
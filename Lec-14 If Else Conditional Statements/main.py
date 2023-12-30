a = int(input("enter any number : "))

if(a < 0):
    print("number is negative")
elif(a > 0):
    if(a <= 10): # here can`t add two condition using and
        print("number is 1 - 10")
    elif(a > 10 and a < 20):
        print("number is 11 - 20")
    else:
        print("number is grater then 20")
else:
    print("number is zero")

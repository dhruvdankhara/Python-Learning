import time
a = time.strftime('%H:%M:%S') # hour minute second
print(a)
a = time.strftime('%D') # date mm/dd/yy
print(a)
a = time.strftime('%h') # month in word 
print(a)
a = time.strftime('%m') #  month in number 
print(a)
a = int(time.strftime('%H')) 
print(a)

if(a > 20):
    print("good night")
elif(a > 16):
    print("good afternoon")
elif(a > 10):
    print("good noon")
elif(a > 4):
    print("good morning")
else:
    print("sleep well")
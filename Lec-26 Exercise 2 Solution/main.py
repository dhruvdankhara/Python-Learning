# for more information about time see lec 15
import time

a = int(time.strftime('%H'))
print("time is ", a)
if(a >= 3 and a < 11):
    print("good morning")
elif(a >= 11 and a < 20):
    print("good afternoon")
elif(a >= 20 and a < 3):
    print("good night")

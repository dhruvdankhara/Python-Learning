def fact(num):
    if(num == 1 or num == 0):
        return 1
    else:
        return (num * fact(num - 1))
num = 5
ans = fact(num)
print(ans)


def febo(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return febo(n - 1) + febo(n-2)
    
n = 8
ans = febo(n)
print(ans)

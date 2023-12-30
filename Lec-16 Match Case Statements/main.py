# switch case
x = int(input("enter number : "))

match x: 
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case _ if x < 80:
        print("x is above 80")
    case _ if x < 90:
        print("x is above 90")
    case _:
        print("x is above 100")
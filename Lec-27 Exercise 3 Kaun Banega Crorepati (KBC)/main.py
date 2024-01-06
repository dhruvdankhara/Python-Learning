que = ("how many colors in rainbow.","name of our country.","what is extenstion of python file.","richest person of world")
op = ((5,7,2,4),("india","bharat","china","USA"),(".exe",".obj",".py",".python"),("elon musk","mukesh ambani","dhruv","adani"))
MCQ = ("A","B","C","D")
ans = ("B","A","C","C")
prize = (1000,5000,20000,100000)
won = 0
# print(type(prize[0]))
print("welcome to kaun banega crorepati(KBC): ")
for i in range(len(que)):
    print(i+1,".",que[i])
    for j in range(4):
        print(MCQ[j],op[i][j])
    inp = input()
    if(inp == ans[i]):
        print("you are right. you won",prize[i],"$")
        won = won + prize[i]
    else:
        print("you are wrong right answer is ",ans[i])
    print("if you want to play next question enter 'Y', otherwise enter 'N'.")
    next = input()
    if(next == 'N'):
        break
print("GAME IS ENDED.")
print("you won",won,"$")
    


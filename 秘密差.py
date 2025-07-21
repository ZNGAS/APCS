#c290. APCS 2017-0304-1秘密差
#https://zerojudge.tw/ShowProblem?problemid=c290
num = input()
d,p = 0,0
for index,i in enumerate(num):
    if index%2 == 0:d+=int(i)
    else:p+=int(i)
print(abs(p-d))
#c290. APCS 2017-0304-1秘密差
#https://zerojudge.tw/ShowProblem?problemid=c290

a = input()
ans1 = ans2 = 0
for i in range(1,len(a),2):
    ans1 += int(a[i])
for i in range(0,len(a),2):
    ans2 += int(a[i])
print(abs(ans1-ans2))

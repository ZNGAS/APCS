#b964. 1. 成績指標
#https://zerojudge.tw/ShowProblem?problemid=b964
a = input()
n = list(map(int,input().split()))
r = []
s = []
for i in n:
    if i < 60:
        r.append(i)
    elif i >= 60:
        s.append(i)
p=len(n)
n.sort()
r.sort()
s.sort()
print(" ".join(map(str, n)))
if len(r)>0:
    print(r[-1])
else:
    print("best case")
if len(s)>0:
    print(s[0])
else:
    print("worst case")
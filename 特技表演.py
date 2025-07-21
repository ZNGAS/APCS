#o076. 1. 特技表演
#https://zerojudge.tw/ShowProblem?problemid=o076
n = int(input())
arr = list(map(int,input().split()))
num = 1
ans = []
for i in range(1,n):
    if arr[i-1]-arr[i] > 0:
        num += 1
    else:
        if num > 1:
            ans.append(num)
        num = 1
if num > 1:
    ans.append(num)
print(max(ans))
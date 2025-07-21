#f605. 1. 購買力
#https://zerojudge.tw/ShowProblem?problemid=f605
n,d = map(int,input().split())
num,cost = 0,0
for i in range(n):
    item = list(map(int,input().split()))
    if max(item) - min(item) >= d:
        num += 1
        cost += sum(item)//3
print(num,cost)
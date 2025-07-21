#g595. 1. 修補圍籬
#https://zerojudge.tw/ShowProblem?problemid=g595
n = int(input())
h = list(map(int, input().split()))
num = 0
for i in range(n):
    if h[i] == 0:
        if i == 0:
            h[i] = h[i + 1]
        elif i == n - 1:
            h[i] = h[i - 1]
        else:
            h[i] = min(h[i - 1], h[i + 1])
        num += h[i]
print(num)
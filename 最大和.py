#c295. APCS-2016-1029-2最大和
#https://zerojudge.tw/ShowProblem?problemid=c295
n,m = map(int,input().split())
max_num,ans = [],[]
for i in range(n):
    num = list(map(int,input().split()))
    num.sort()
    max_num.append(num[-1])
sum_num = sum(max_num)
print(sum_num)
for k in max_num:
    if sum_num % k == 0:ans.append(k)
if len(ans) != 0:print(*ans)
else:print(-1)
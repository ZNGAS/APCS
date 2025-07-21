#q181. 1. 等紅綠燈
#https://zerojudge.tw/ShowProblem?problemid=q181
ab=list(map(int,input().split()))
a,b=ab[0],ab[1]
n=int(input())
t=list(map(int,input().split()))
time=sum(ab)
ans=0
for i in t:
    num=i%time
    if num>a:ans+=time-num
    elif num<a:ans+=0
    elif num==a:ans+=b
print(ans)
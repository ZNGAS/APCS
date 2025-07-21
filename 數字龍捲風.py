def line(a, n, t):
    global ans
    p = 1
    aindex = [t,t]
    for i in range(n):
        if p%2 == 1:            
            for j in range(i):
                aindex[0] += 1
                ans.append(a[aindex[0]][aindex[1]])
            for j in range(i):
                aindex[1] -= 1
                ans.append(a[aindex[0]][aindex[1]])
            p += 1
        else:
            for j in range(i):
                aindex[0] -= 1
                ans.append(a[aindex[0]][aindex[1]])
            for j in range(i):
                aindex[1] += 1
                ans.append(a[aindex[0]][aindex[1]])
            p += 1
    for i in range(n-1):
        aindex[0] -= 1
        ans.append(a[aindex[0]][aindex[1]])

def ch(arr):
    return [list(reversed(col)) for col in zip(*arr)]

n = int(input())
r = int(input())
a = []
t = n//2

for i in range(n):
    a.append([x for x in input().split()])

ans = []
ans.append(a[t][t])

if r == 0:
    for _ in range(1):
        a = ch(a)
    line(a, n, t)
elif r == 1:
    line(a, n, t)
elif r == 2:
    for _ in range(3):
        a = ch(a)
    line(a, n, t)
else:
    for _ in range(2):
        a = ch(a)
    line(a, n, t)

print(*ans,sep="")


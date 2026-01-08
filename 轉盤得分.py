num = [int(x) for x in input().split()]
m,n,k = num[0],num[1],num[2]

s = [] #字串
run = [] #回合

for i in range(m):
    s.append(input())
for i in range(k):
    run.append([int(x) for x in input().split()])

for i in range(k):
    p = []
    for j in range(m):
        o = []
        if run[k][m] > 0:
            for l in range(n):
                o.append(s[m][l-run[k][m]%n])
        if run[k][m] == 0:
            o.append(s[m])
        if run[k][m] < 0:
            for l in range(n):
                o.append(s[m][l+run[k][m]%n])
        p.append(o)
    for t in range(n):
        score = 0



    

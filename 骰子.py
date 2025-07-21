n,m = map(int,input().split())
ans = [1]*n
p = [[4,1,2] for _ in range(n)] #設a為頂點,a對面為b,a+b恆為7
const = 7
for i in range(m):
    a,b = map(int,input().split())
    s = p[a-1]
    j = 0
    if b > 0:
        ans[a-1],ans[b-1]=ans[b-1],ans[a-1]
        p[a-1],p[b-1]=p[b-1],p[a-1]
    elif b == -1:
        j = const - s[0]
        s[0] = s[1]
        s[1] = j
        ans[a-1] = s[1]
    elif b == -2:
        j = const - s[2]
        s[2] = s[1]
        s[1] = j
        ans[a-1] = s[1]
print(*ans)


a,b = map(int,input().split())
n = int(input())
total = 0
for i in range(n):
    arr = [int(x) for x in input().split()]
    count_a = 0
    count_b = 0
    for i in arr:
        if i == 0:break
        if abs(i) == a:
            count_a += 1 if i > 0 else -1
        if abs(i) == b:
            count_b += 1 if i > 0 else -1
    if count_a > 0 and count_b > 0:total += 1
print(total)
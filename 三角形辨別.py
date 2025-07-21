line = list(map(int,input().split()))
line.sort()
a,b,c = line[0],line[1],line[2]
print(*line)
if a+b<=c:print("No")
elif a*a+b*b==c*c:print("Right")
elif a*a+b*b>c*c:print("Acute")
elif a*a+b*b<c*c:print("Obtuse")
n = int(input())
x_arr,y_arr,result_max,result_min = [],[],-1000,1000
for i in range(n):
    x,y = map(int,input().split())
    x_arr.append(x)
    y_arr.append(y)
for i in range(1,n):
    result_max = max(result_max,abs(x_arr[i-1]-x_arr[i])+abs(y_arr[i-1]-y_arr[i]))
    result_min = min(result_min,abs(x_arr[i-1]-x_arr[i])+abs(y_arr[i-1]-y_arr[i]))
print(result_max,result_min)
n = int(input())

a = list(map(int, input().split()))

max_num = a[0]
for i in range(n):
    if a[i] > max_num:
       max_num = a[i]
       

for i in range(n):
    a[i] = a[i] / max_num * 100
    
total = 0
for i in range(n):
    total += a[i]
    
print(total / n)
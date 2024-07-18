n, m = map(int, input().split())
n_list = [i for i in range(1, n + 1)]

for i in range(m):
    x, y = map(int,input().split())
    temp = n_list[x-1 : y]
    temp.reverse()
    n_list[x-1 : y] = temp
    
for i in range(n):
    print(n_list[i], end=" ")
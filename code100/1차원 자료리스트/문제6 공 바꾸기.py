n, m = map(int,input().split())

list_a = [index for index in range(1, n+1)]

for i in range(m):
    i, j = map(int,input().split())
    list_a[i- 1], list_a[j - 1] = list_a[j - 1], list_a[i - 1]

for i in range(n):
    print(list_a[i], end=" ")
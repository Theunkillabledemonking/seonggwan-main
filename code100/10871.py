a, b = map(int, input().split())
list_a = list(map(int, input().split()))

for i in range(a):
    if list_a[i] < b:
        print(list_a[i], end=" ")

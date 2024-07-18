a__lenth = int(input())

num_value = list(map(int, input().split()))
list_count = int(input())
count = 0
for i in num_value:
    if list_count == i:
        count += 1
print(count)

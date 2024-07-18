# max min
num = int(input())
list_lenth = list(map(int,input().split()))
min_num = list_lenth[0]
max_num = list_lenth[0]

for i in list_lenth:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i
print(min_num, max_num)
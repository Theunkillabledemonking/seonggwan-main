num_list = []
for i in range(9):
    num_list.append(int(input()))
    
new_list = num_list[:]

for i in range(8):
    if num_list[i] > num_list[i + 1]:
        num_list[i + 1] = num_list[i]

print(num_list[-1])
print(new_list.index(num_list[-1]) + 1)
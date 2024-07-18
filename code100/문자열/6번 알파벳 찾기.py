value = (input())
eng = 'abcdefghijklmnopqrstuvwxyz'

for i in eng:
    found = False
    for index in range(len(value)):
        if value[index] == i:
            print(index, end=" ")
            found = True
            break
    if not found:
        print("-1", end=" ")
n = int(input("ㅇ"))

for i in range(n):
    for j in range(n):
        print(" " * (n - i) + "*" * (i)) 
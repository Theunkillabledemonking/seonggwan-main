num = []

for i in range(10):
    n = int(input())
    if n % 42 not in num:
        num.append(n % 42)

print(len(num))
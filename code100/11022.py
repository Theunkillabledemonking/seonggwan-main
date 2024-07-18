n = int(input("n"))

for i in range(1, n+1):
    a, b = map(int,input("input").split())
    print(f"Case #{i}: {a} + {b} = {a + b}")
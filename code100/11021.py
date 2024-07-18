n = int(input("반복 횟수를 입력하세요."))

for i in range(1, n+1):
    a, b = map(int,input("글자 입력").split())
    print(f"Case # {i} : {a+b}")


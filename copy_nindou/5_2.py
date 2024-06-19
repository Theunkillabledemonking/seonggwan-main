# 별 증가
num = int(input("별 입력 : "))

for i in range(1, num+1):
    for j in range(i):
        print("*", end = "")
    print()
    
for i in range(num - 1, 0, -1):
    for j in range(i):
        print("*", end = "")
    print()
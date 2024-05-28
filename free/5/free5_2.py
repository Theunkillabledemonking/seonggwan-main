# N 값 입력
num = int(input("N을 입력해:"))


# 1 <= "*" <= N, N번 반복하면 별을 1식 증가하면서 출력
# 반복 (count)
# count * "*"
for i in range(1, num+1):
    #print('*' * i)
    for _ in range (0, i):
        print("*", end="")
    print()
# N -> 1, 1 씩 감소
# count * "*"    
for i in range(num-1,0,-1):
   print('*' * i)
    

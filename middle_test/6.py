# 10 ~ 20 사이 정수 중 짝수의 합을 계산

# sum = 0

# for value in range(10, 21, 2):
#     sum += value
    
# print(value)
    

# for i in range(10, 21):
#     if i % 2 == 0 :
#         sum += i
        
# print(sum)

# 구구단 

# 2단부터 9단 까지
# 2 X 1 = 2
# 2 X 2 = 4
#
# 2 X 9 = 18
#------------
#
# 9 X 9 = 콘

# for value in range(2,10): # 2단 -> 9단 : 5단과 7단은 제외
#     if value == 5 or value == 7:
#         continue

#     for index in range(1,10):
#         print(value, "X", index, "=" , value * index)
#     print("--------------------------------------")

import random

count = 0
computer_random = random.randint(1,100)

while count < 10 :
    user_random = int(input(f"{count+1}입력하세요"))
    # 0 입력시 프로그램 종려
    if user_random == 0:
        print("종료")
        break
    
    if user_random > computer_random :
        print("값이 큽니다.")
    elif user_random < computer_random :
        print("값이 작습니다")
    else: 
        print("세이카이")
        break
    
    count += 1
    
if count == 10:
    print("횟수 초과 게임종료")
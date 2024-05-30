# while , break 문을 사용하여 1부터 100 사이의 숫자를 맞추는 게임 작성

import random

# 랜덤 함수
random_choice = random.randint(1,100)

while True:
    # 유져 입력
    
    input_user = int(input("1부터 100 사이의 숫자를 맞춰보세요 :"))
    
    # 조건 값 비교
    if input_user > random_choice :
        print("더 작은 숫자입니다.")
    elif input_user < random_choice :
        print("더 큰 숫자입니다.")
    elif random_choice == input_user :
        print("정답입니다.")
        break
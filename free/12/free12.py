import random

# 난수를 생성하여 리스트에서 요소를 선택하는 방법

use = input("가위, 바위, 보 중 하나를 선택하세요: ")
choices = ['가위', '바위', '보']
computer_choice = random.choice(choices)
print("컴퓨터의 선택: ", computer_choice)

if computer_choice == use :
    print("무승부입니다!")
elif (computer_choice == '가위' and use =='바위') or (computer_choice == '바위'and use =='보') or (computer_choice == '보' and use == '가위'):
    print("당신이 이겼습니다!")
elif (computer_choice == '바위' and use =='가위') or (computer_choice == '보'and use =='바위') or (computer_choice == '가위' and use == '보'):
    print("당신은 졌습니다!")
else:
    print("잘못된 입력입니다. 가위, 바위, 보 중에서 선택해주세요.")
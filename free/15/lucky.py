# 사용자로부터 가위,바위,보 중 하나 입력받고 컴퓨터가 선택한 값과 대결하여 승, 패, 무를 판단 후 결과 출력

# 게임은 3판 2선 승제로 진행

# 매 게임마다 승, 패, 무 결과 출력

# 게임이 종료되면 전체 승, 무 , 패의 결과와 최종 승자를 출력

# 사용자가 입력하는 값은 "가위", "바위", "보" 중 하나 이며= 이외의 값이 입력되면 다시 입력

# in not in 연산자 사용 금지

# import random

# choice = ['가위','바위','보']

# Win = 0
# Lose = 0
# Draw = 0

# while Win < 2 and Lose < 2 :
#         user_choice = input("가위, 바위, 보 중 입력하세요: ")
#         if user_choice == '가위' or user_choice == '바위' or user_choice == '보':
#             computer_choice = random.choices(choice)
#             print(f"컴퓨터{computer_choice}")

#             if user_choice == '가위' and computer_choice == '바위':
                  
            



import random # 내장함수 랜덤 가져오가

choice_list = ["가위", "바위", "보"] # 가위바위보 리스트 작성
W = 0 # 승리 횟수
L = 0 # 패배 횟수
D = 0 # 무승부 횟수

while W < 2 and L < 2 and D < 2: # 승리 2번이나 패배 2번 할 때 까지 반복
    choice = input("가위, 바위, 보 중 하나를 입력하세요: ") # 가위바위보 입력
    if choice == "가위" or choice == "바위" or choice == "보": # 만약 입력한 게 가위바위보이면 진행
        computer_choice = random.choice(choice_list) # 컴퓨터는 가위바위보중 랜덤으로 선택
        print("컴퓨터:", computer_choice) 
        if choice == "가위" and computer_choice == "보": # 만약 사용자는 가위 컴퓨터가 보이면 
            W += 1 # 1승 추가
            print("승리! 현재 전적:",W,"승",L,"패",D,"무")
        elif choice == "바위" and computer_choice == "가위": # 사용자가 바위 컴퓨터가 가위이면
            W += 1 # 1승 추가
            print("승리! 현재 전적:",W,"승",L,"패",D,"무")
        elif choice == "보" and computer_choice == "바위": # 사용자가 보 컴퓨터가 바위이면
            W += 1 # 1승 추가
            print("승리! 현재 전적:",W,"승",L,"패",D,"무")
        elif choice == computer_choice: # 만약 사용자랑 컴퓨터가 같은 거라면
            D += 1 # 무승부 추가
            print("무승부! 현재 전적:",W,"승",L,"패",D,"무")
        else: # 그외 나머지 경우는 패배하는 경우이기 때문에 한번에 else로 묶어서 표현
            L += 1  # 패배 추가
            print("패배! 현재 전적:",W,"승",L,"패",D,"무")
    else: # 가위바위보 중에서 입력 안했을시
        print("가위, 바위, 보 중에서 선택하세요.")
            
if W >= 2: # 승리가 2번 이상이면 사용자가 이김
    print("최종 승자: 사용자")
elif D >= 2:
    print("최종 결과: 무승부")
else: # 나머지 경우인데 한마디로 패배가 2번이상이면 컴퓨터 승리
    print("최종 승자: 컴퓨터")

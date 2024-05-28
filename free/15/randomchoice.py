# 가위바위보 
import random

# 리스트 생성 후 가위 바위 보
choice_list = ['가위', '바위' , '보']

# 승 패 무 초기 값 설정
player_win = 0
player_lose = 0
player_draw = 0

# 조건 반복문 3판 2선 2승시 먼저 끝남
while 2 > player_win and 2 > player_lose :
    # 사용자 가위바위보 입력
    youser_choice = input("가위, 바위, 보 중 하나를 입력하세요: ")
    # 컴퓨터 가위바위보 랜덤 출력
    computer_choice = random.choice(choice_list)
    print("컴퓨터: ",computer_choice)

    # 사용자가 맞지 않는 입력값을 넣으면 걸러냄
    if youser_choice == '가위' or youser_choice == '바위' or youser_choice == '보':

        # 무승부
        if youser_choice == computer_choice:
            player_draw += 1
            print(f"무승부! 현재 전적: {player_win}승 {player_lose}패 {player_draw}무")

            #컴퓨터가 이긴 조건
        elif (youser_choice == '가위' and computer_choice == '바위') or \
             (youser_choice == '바위' and computer_choice == '보') or \
             (youser_choice == '보' and computer_choice == '가위'):
            player_lose += 1
            print(f"패배! 현재 전적: {player_win}승 {player_lose}패 {player_draw}무")
            # 사용자가 이긴 조건 값
        else:
            player_win +=1
            print(f"승리! 현재 전적: {player_win}승 {player_lose}패 {player_draw}무")

    else : 
        input("가위, 바위, 보 중 하나를 입력하세요:")


# 플레이어가 2승하면 출력
if player_win >= 2 :
        print(f"전적: {player_win}승 {player_lose}패 {player_draw}무")
        print("최종 승자 : 사용자")
# 플레이어가 2패하면 출력
else:
        print(f"전적: {player_win}승 {player_lose}패 {player_draw}무")
        print("최종 승자 : 컴퓨터")
    

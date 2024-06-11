import random
# 컴퓨터 난수 3개 생성 후 하나 랜덤 선택
def generate_random_numbers():
    rand_com_list = []
    while len(rand_com_list) < 3:
        rand_com = random.randint(1,9)
        if rand_com not in rand_com_list:
            rand_com_list.append(rand_com)
    return rand_com_list

# 사용자 정수 입력 함수
def get_user_input():
    print("사용자 입력 1~9 정수 입력하세요.")
    while True:
        user_input = [int(input()) for _ in range(3)]
        
        found_dup = True
        for num in user_input:
            if num < 1 or num > 9:
                found_dup = False
                print("모든 숫자는 1부터 9까지여야 합니다.")
                break
            
        if found_dup:
            break
        
    return user_input

# strike, balls 체크 함수
def calculate_stirkes_and_balls(rand_com_list, user_input):
    strike = 0
    balls = 0
    for i in range(3):
        if user_input[i] == rand_com_list[i]:
            strike += 1
        elif user_input[i] in rand_com_list:
            balls += 1
            
    return strike, balls

def get_game_finish(strike, count_game_trial, count_stirke_out):
    
    if count_stirke_out >= 2 or count_game_trial >= 5:
        msg = "5회 이상 실행" if count_game_trial >= 5 else "스트라이크 아웃"
        print(msg, "\t게임종료")
        return True
    
    if strike >= 3:
        msg = "승리 \t게임 종료"
        return True
    
    return False
    
rand_com_list = generate_random_numbers()
print("컴퓨터 난수", rand_com_list)

count_strike_out = 0
count_game_trial = 0

while True:
    user_input = get_user_input()
    print("사용자 입력", user_input)
    
    strike, balls = calculate_stirkes_and_balls(rand_com_list, user_input)
    print("Strike", strike, "Balls", balls)
    
    if strike == 0 and balls == 0:
        count_strike_out += 1
        
    count_game_trial +=1 
    
    if get_game_finish(strike, count_game_trial, count_strike_out):
        break


# while True:
#     strike = 0
#     balls = 0
#     user_try += 1
    
#     print("사용자 입력 : ")
#     user_input = [int(input())for _ in range(3)]

#     # 인덱스 위치로 값 확인
#     for i in range(3):
#         for j in range(3):
#             if user_input[i] == rand_com_list[i]:
#                 if i == j:
#                     strike += 1
#                 else:
#                     balls += 1
#                 break

#     # 스트라이크 아웃 판별
    
#     if strike == 0 and balls == 0:
#         user_strike_out += 1
#         print("스트라이크 아웃!")
#     else:
#         print("strike", strike, "\tBall:", balls)

    

# # # 게임 패배 시도 횟수 5 or 스트라이크 아웃 횟수 2번 이상
#     if user_strike_out == 5 or user_try == 2:
#         msg = "5회 이상 실행" if user_try >= 5 else "스트라이크"
#         print("패배 게임종료!")
#         break
    
# # # 게임 승리 strike 3일떄 승리
#     if strike >= 3 :
#         print("승리 게임종료")
#         break
# # def 함수명(인자값):
# #    함수 호출 시 실행 명령어

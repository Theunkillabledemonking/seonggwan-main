# # 컴퓨터가 생성한 중복되지 않는 3개의 난수를 플레이어가 맞추는게임
# # 각 시도마다 입력한 숫자와 컴퓨터의 숫자를 비교하여 스트라이크와 볼의 개수를 알려줍니다,
# # 게임은 플레이어가 정답을 맞추거나 패배 조건에 도달할 때까지
# import random

# # 컴퓨터 난수 생성
# #   - 컴퓨터 난수 생성 0~9 사이의 중복되지 않는 정수 3개 생성

# # 플레이어 입력
# #  - 플레이어는 키보드를 통해 0~9 사이의 정수 3개 입력
# #  - 예외 처리는 하지 않는다. 올바른 입력이 들어온다 가정

# # 게임패배 조건
# #  - 시도 횟수가 5번 이상일 경우
# #  - 스트라이크 아웃횟수가 2번 이상일 경우

# # 승리 조건
# #  - 프레이어가 컴퓨터가 생성한 난수 값을 자리 순서대로 맞출 경우


# # 중복되지 않은 1~10사이 정수 3개 생성
# # in, not in, list 내 중복되지 않은 랜덤 정수 생성 함수 사용금지

# # 3 7 4 : computer
# # 2 3 4 : user
# # result : 1 strike, 1 ball

# import random


# def getRandValue():
#     rand_list = list()

#     count = 0

#     while count < 3:
#         rand_value = random.randint(1, 10)
#         found_duplicated_value = False
        
#         for sub_count in range(count):
#             # 중복 값이 있을 경우
#             if rand_value == rand_list[sub_count]:
#                 found_duplicated_value = True
#                 break
        
#         if not found_duplicated_value:
#             rand_list.append(rand_value)
#             count += 1
            
#     return rand_list

# count_game_trial = 0
# count_strike_out = 0
# count_strike = 0

# com_list = getRandValue()

# while True:
#     # 사용자 입력

#     # strike, Ball 판별

#     # 변수 업데이트

#     # 종료 조건 : 패배
#     if count_game_trial >= 5 or count_strike_out >= 2:
#         break
    
#     # 종료 조건 : 승리
#     if count_strike >= 3:
#         break



import random

# 중복되지 않은 0~9 사이 정수 3개 생성 (in, not in 사용 금지)
def getRandValue():
    rand_list = list()
    
    count = 0
    
    while count < 3:
        rand_value = random.randint(1, 10)  # 1에서 10 사이의 정수 생성
        found_duplicated_value = False
        for sub_count in range(count):
            if rand_value == rand_list[sub_count]:
                found_duplicated_value = True
                break
        if not found_duplicated_value:
            rand_list.append(rand_value)
            count += 1
    return rand_list

count_game_trial = 0
count_strike_out = 0
com_list = getRandValue()


while True:
    # 사용자 입력
    input_user = input(f"시도 {count_game_trial + 1}: 입력한 숫자 (공백으로 구분) - ")
    user_list_split = input_user.split(" ")
    user_list = list()
    for num_str in user_list_split:
        user_list.append(int(num_str))

    # 스트라이크, 볼, 아웃 판별
    strikes = 0
    balls = 0
    outs = 0
    for i in range(3):
        # [i]를 사용해 같은 위치에 있는 숫자가 동일한지 확인
        if user_list[i] == com_list[i]:
            strikes += 1
        else:
            #다른 위치에 있는 경우 i != j 서로 다른 위치 숫자 비교 조건
            found = False
            for j in range(3):
                if user_list[i] == com_list[j] and i != j:
                    balls += 1
                    found = True # 볼을 찾았음을 표시
                    break
            if not found: # 볼을 찾지 못했으므로 아웃 증가
                outs += 1

    print(f"결과: {strikes} 스트라이크, {balls} 볼, {outs} 아웃")

    # 변수 업데이트
    count_game_trial += 1
    if strikes == 0: # 스트라이크가 0인 경우 스트라이크 아웃 횟수를 증가시킴
        count_strike_out += 1

    # 종료 조건 : 패배
    if count_game_trial >= 5 or count_strike_out >= 2:
        print(f"게임 종료 : 패배 (시도 횟수 {count_game_trial}회, 스트라이크 아웃 {count_strike_out}회 초과)")
        print(f"정답 : {com_list}")
        break

    # 종료 조건 : 승리
    if strikes >= 3:
        print("게임종료 : 승리!")
        print(f"정답 : {com_list}")
        break
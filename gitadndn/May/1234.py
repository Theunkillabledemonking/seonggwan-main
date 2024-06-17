# hello

# stage = 5
# stage_A = stage - 1
# for value in range(stage):
#     space = (" " * (stage_A - value))
#     stars = ("*" * (value * 2 + 1))
#     print(space + stars)
    
# for value in range(stage_A):
#     space = (" " * (value + 1))
#     stars = ("*" * (2 * (stage_A - value) - 1))
#     print(space + stars)

# list = []
# for i in range(1, 21):
#     list.append(int(i))

# li = [value for value in range(1,21) if value % 3 == 0]
# print(li)

# # 아래 리스트 중 'c'가 포함된 단어만 선택해서 리스트로 구성하라
# foo = ['abc', 'dcd', 'ef', 'gh']
# bar = [word for word in foo if len(word) >= 3]
# print(bar)

# # 1에서 10사이 정수 중, 홀수는 10을 곱하고, 짝수는 20을 곱한 리스트 생성

# num = [value * 10 if value % 2 != 0 else value * 20 for value in range(1, 11)]
# print(num)

# s_list = [value for value in range(1, 21) if value % 3 == 0 and value % 4 == 0]
# print(s_list)

# bar = ["hello", "world", "Richard"]
# #found_word = False # 플래그 변수 불린값으로 값을 찾음

# for word in bar:
    
#     if word == "l":
#         print("단어를 찾았습니다.")
#  #       found_word = True
#         break
# else:
#     print("못참음")
# #if not found_word:

#    print("단어를 찾지 못했음 나빠또")

# import random

# #컴퓨터 랜덤 정수 생성하기
# com_list = []
# for value in range(3):
#     while True:
#         rand_com = random.randint(1,9)
        
#         if rand_com not in com_list:
#             com_list.append(rand_com)
#             break

# print(com_list)

# # 유저 입력하기
# trial_count = 0
# strike_out = 0

# while True:
#     strike = 0
#     ball = 0
#     user_list = []
    
#     trial_count += 1
#     for i in range(3):
#         user_input = int(input("입력하세요"))
#         rand_user = user_list.append(user_input)
#         print(f"{i + 1}: 입력한 숫자 - ")
    
#     for i in range(3):
#         if user_list [i] == com_list [i]:
#             strike += 1
#         elif user_list [i] in com_list:
#             ball += 1

#     # 아웃값
#     if strike == 0 and ball == 0:
#         strike_out += 1
                
#     print(f"시도 {trial_count:} 입력한 숫자 -")
#     print(f"결과 : {strike}Strike, {ball}Ball, {strike_out} Out")
    
# # 게임 패배 조건
#     if trial_count >= 5 or strike_out >= 2:
#         msg = "5회 이상 실행" if trial_count >=5 else "스트라이크 2회 이상"
#         print(msg, "\t게임 종료")
#         break
    
#     if strike >= 3:
#        print("승리\t게임종료")
#        break 





import random

# 컴퓨터 난수 생성
rand_come = []

for value in range(3):
    while True:
        rand_comlist = random.randint(1,9)
        if rand_comlist not in rand_come:
            rand_come.append(rand_comlist)
            break
print(rand_come)

# 사용자 입력

count_trail = 0
count_strike_out = 0

while True:
    balls = 0
    strike = 0

    user_list = []
    count_trail += 1
    for value in range(3):
        input_value = int(input(f"{count_trail}: 입력한 숫자 -"))
        user_list.append(input_value)
        print(user_list)
        
    # index 비교
    for i in range(3):
        if user_list [i] == rand_come [i]:
            strike += 1
        elif user_list [i] in rand_come:
            balls += 1
            
    # 삼진아웃
    if strike == 0 and balls == 0:
        count_strike_out += 1
    
    print(f"시도{count_trail}: 입력한 숫자 - ", rand_come)
    print(f"결과: {strike} Strikes, {balls} Ball, {count_strike_out} Out")
    
    if count_strike_out >= 2 or count_trail >= 5:
        msg = "게임 종료: 패배 (시도 횟수 5회 초과)" if count_trail >= 5 else "스트라이크 5회 초과"
        print(msg, "\t게임종료")
        break
    elif strike >= 3:
        print("게임 종료 승리")
        print("정답 : ", rand_come)
        break



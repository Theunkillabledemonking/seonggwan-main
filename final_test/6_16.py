# import random
# # 야구 게임

# # 컴퓨터 중복되지 않는 랜덤 난수 값 3개 생성
# rand_com = []
# count = 0
# while count < 3 :
#     rand_list = (random.randint(0,2))
#     for index in range(count) :
#         if rand_com[index] == rand_list:
#             break
#     else:
#         rand_com.append(rand_list)
#         count += 1
# print(rand_com)

# count_strike_out = 0
# count_trial = 0
# while True:
# # 플레이어 3개의 값 입력 받기
#     count_strike = 0
#     count_ball = 0
    
#     input_value = input("정수 3개를 입력해주세요")
#     input_list = [int(index) for index in input_value.split()]
#     print(input_list)

# # index 값으로 strike, ball 판별
#     for i in range(3):
#         for j in range(3):
#             if rand_com[i] == input_list[j]:
#                 if i == j:
#                     count_strike += 1
#                 else:
#                     count_ball += 1
    
# # strike X , ball X strike out 추가
#     if count_strike == 0 and count_ball == 0:
#         count_strike_out += 1
#     count_trial += 1
#     print(f"Strike :{count_strike}, Ball : {count_ball}, Out : {count_strike_out}")

# # 게임 종료 조건

# # strike 3회
#     if count_strike >= 3:
#         print("유저 승리")
#         break
# # trial 5번 or strike out 2번
#     if count_strike_out >= 2 or count_trial >= 5:
#         print("유저 패배")
#         break



# 단어 맞추기 게임
import random

# 단어 입력
input_list = ["hello", "aniiny", "abcdef"]

# 조건문 추후 구현
rand_selet = list(input_list[random.randint(0,2)])
print(rand_selet)
rand_print = rand_selet [:]

# 단어의 반올림화
char_num_word = len(rand_selet)
blind_num_word = (char_num_word + 1) // 2
blind_num_word = int(blind_num_word)
print(blind_num_word)

# 단어 블라인드화
blind_num_list = [index for index in range(0, char_num_word)]
print(blind_num_list)
for index in range(0, char_num_word - blind_num_word):
    del blind_num_list[random.randint(0, len(blind_num_list) - 1)]
print(blind_num_list)

for index in blind_num_list:
    rand_print[index] = "_"
print(rand_print)

# 단어 맞추기
while len(blind_num_list) > 0:
    print(rand_print)
    found_list = []
    input_value = input("맞출 단어를 입력해주세요 : ")
    
    for index in blind_num_list:
        if rand_selet[index] == input_value:
            rand_print[index] = input_value
            found_list.append(index)
    
    for f_index in found_list:
        blind_num_list.remove(f_index)
        
print(''.join(rand_print))
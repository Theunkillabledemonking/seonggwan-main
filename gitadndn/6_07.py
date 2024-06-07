# import random

# # 컴퓨터 난수 설정
# input_list = []
# for index in range(3):
#     while True:
#         input_value = input("입력하세요")
#         if 5 <= len(input_value) <= 20:
#             input_list.append(input_value)
#             break
#         print("다시입력하세요")
        
# print(input_list)

# # 임의 단어 선택
# word_select = list(input_list[random.randint(0, 2)])
# print(word_select)
# # 복사
# word_print = word_select[:]

# char_num_word = len(word_select)
# # 반올림 처리
# blind_num_word = char_num_word / 2
# if blind_num_word < char_num_word // 2:
#     blind_num_word += 1

# blind_num_word = int(blind_num_word)

# # index 값을 리스트로 불러오기
# blind_num_list = [index for index in range(0, char_num_word)]
# print(blind_num_list)

# # index 값을 반올림 숫자 만큼 빼주기
# for index in range(1, char_num_word - blind_num_word):
#     del blind_num_list[random.randint(0, char_num_word - 1)]

# print(blind_num_list)
# # 게임 시작 블라인드 처리
# for index in blind_num_list:
#     word_print[index] = "_"
# print(word_print)


# # 입력
# while len(blind_num_list) > 0 :
#     print(word_print)
#     found_list =  []
    
#     input_value = input("입력하세요")
    
#     # 단어 찾기
#     for index in blind_num_list :
#         if word_select[index] == input_value:
#             word_print[index] = input_value
#             found_list.append(index)

#     # 인덱스 값 지우기
#     for f_index in found_list:
#         blind_num_list.remove(f_index)
        
# print(word_print)        
# # 해제
















import random
input_list = []
# 단어 입력
for index in range(3):
    while True:
        input_value = input("입력하세요")
        if 5 <= len(input_value) <= 20 :
            input_list.append(input_value)
            break
        print("5이상 20이하 단어를 입력하세요")
#단어 복사
        
# 단어 랜덤 선택
word_select = list(input_list[random.randint(0, 2)])
word_print = word_select[:] # 복사
print(word_print)
# 반올림 처리
char_num_word = len(word_select)
blind_num_word = char_num_word / 2
if blind_num_word < char_num_word // 2:
    blind_num_word += 1
print(blind_num_word)
blind_num_word = int(blind_num_word)
# 블라인드 처리
blind_num_list = [index for index in range(0, char_num_word)]
print(blind_num_list)

for index in range(1, char_num_word - blind_num_word):
    del blind_num_list[random.randint(0, len(blind_num_list) - 1)]
print(blind_num_list)

for index in blind_num_list:
    word_print[index] = "_"

count = 1
print(word_print)
# 정답 입력
while len(blind_num_list) > 0 :
    print(word_print)
    found_list = []
    
    input_value = input(f"{count}번째 시도 입력하세요")
    for index in blind_num_list:
        if word_select[index] == input_value:
           word_print[index] = input_value
           found_list.append(index)
           
    # 인덱스 값 지우기
    for f_index in found_list:
        blind_num_list.remove(f_index)
    
    count += 1
# 블라인드 해제

# 게임 종료
print(f"clear 선택된 단어 {word_select}, 총 시도 횟수 {count}")

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

# 단어 입력
def get_user_input():
    input_list = []
    for index in range(3):
        while True:
            input_value = input("입력하세요")
            if 5 <= len(input_value) <= 20 :
                input_list.append(input_value)
                break
            print("5이상 20이하 단어를 입력하세요")
    return input_list
#단어 복사
        
# 단어 랜덤 선택
def select_random_word(input_list):
    word_select = list(input_list[random.randint(0, 2)])
    word_print = word_select[:] # 복사
    return word_select, word_print
    #print(f"단어 선택 완료 게임을 시작합니다. 선택된 단어 : {''.join(word_print)}")

# 반올림 처리
def calculate_blind_num_word(char_num_word):
    if char_num_word % 2 == 0:
        return char_num_word // 2
    else:
        return (char_num_word // 2) + 1

# 블라인드 처리
def get_blind_indeice(char_num_word, blind_num_word):
    blind_num_list = [index for index in range(char_num_word)]
    # 필요한 만큼 인덱스를 제거
    while len(blind_num_list) > blind_num_word:
        del blind_num_list[random.randint(0, len(blind_num_list) - 1)]
    return blind_num_list

# for index in range(1, char_num_word - blind_num_word):
#     del blind_num_list[random.randint(0, len(blind_num_list) - 1)]


def blind_word(word_print, blind_num_list):
    for index in blind_num_list:
        word_print[index] = "_"
    return word_print

def play_game(word_select, word_print, blind_num_list):
    count = 0
    # 정답 입력
    while len(blind_num_list) > 0 :
        print(''.join(word_print))
        found_list = []
            
    # 블라인드 해제
        input_value = input(f"{count + 1}번째 시도 입력하세요")
        for index in blind_num_list:
            if word_select[index] == input_value:
                word_print[index] = input_value
                found_list.append(index)
            
    # 인덱스 값 지우기
        for f_index in found_list:
            blind_num_list.remove(f_index)
        
        count += 1
    return count

def main():
    input_list = get_user_input()
    word_select, word_print = select_random_word(input_list)
    print(f"단어 선택 완료. 선택된 단어 {''.join(word_print)}")
    
    char_num_word = len(word_select)
    blind_num_word = calculate_blind_num_word(char_num_word)
    
    blind_num_list = get_blind_indeice(char_num_word, blind_num_word)
    
    word_print= blind_word(word_print, blind_num_list)
    print("선택된 단어", ''.join(word_print))
    
    count = play_game(word_select, word_print, blind_num_list)
    
    print(f"완성된 단어 : {''.join(word_print)}, 총 시도된 횟수 : {count}")
    

if __name__ == "__main__":
    main()

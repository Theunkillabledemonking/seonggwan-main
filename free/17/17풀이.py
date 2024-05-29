import random

list_words = []

for index in range(3):
    while True:
        input_value = input("단어를 입력하세요")
        
        if 5 <= len(input_value) <= 20 :
            list_words.append(input_value)
            break
        
        print("5이상 20이하 문자를 쳐주세요")
    
#list_words = ["kkikk", "aannaaf", "aeekeet"]

word_selected = list(list_words[random.randint(0, 2)])
word_printed = word_selected[:] # 리스트 카피를 한다.
print("선택된 단어 : ", word_selected)
# 선택된 단어의 글자 수
char_num_word = (len(word_printed))

# 선택된 단어의 글자 수의 50%를 블라인드 처리
blind_num_word = char_num_word / 2
# 반올림 처리 알고리즘 // 연산자는 몫만 가지고 온다.
if blind_num_word < char_num_word // 2:
    blind_num_word += 1
    
blind_num_word = int(blind_num_word)

list_blind_index = [value for value in range(0, char_num_word)]

print("blind index B : ", list_blind_index)

for index in range(1, char_num_word - blind_num_word):
    del list_blind_index[random.randint(0, len(list_blind_index) - 1)]

print("blind index A : ", list_blind_index)

for index in list_blind_index:
    word_printed[index] = "_"
    
print("printed word : ", word_printed)

answer_count = 0
while len(list_blind_index) > 0: # 블라인드 처리된게 있으면 계속 돌게 됨.
    print(word_printed) 
       
    input_value = input("글자를 입력하세요: ")
    
    found_index_list = []

    for index in list_blind_index:
        if word_selected[index] == input_value :
            word_printed[index] = input_value
            found_index_list.append(index)
    
    for f_index in found_index_list:
        list_blind_index.remove(f_index)

print(word_printed)
import random

# 3번 이름
input_list = []

for index in range(3):
    input_value = input("단어를 입력하세요: ")
    while True:
        if 5 <= len(input_value) <= 20:
            input_list.append(input_value)
            break
        print("5이상 20이하 입력하세요")
        
word_choice = list(input_list[random.randint(0,2)])
print(word_choice)
word_printed = word_choice[:]
print(word_printed)
char_num_word = len(word_printed)

blind_num_word = char_num_word / 2
if blind_num_word < char_num_word // 2:
    blind_num_word += 1
    
print(blind_num_word)

range_word_list = [index for index in range(0, char_num_word)]
print(range_word_list)

for index in range(1, char_num_word - blind_num_word):
    # if rnadom
    del range_word_list[random.randint(0, len(range_word_list) -1)]

print(range_word_list)
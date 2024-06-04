import random

word_list = []
for i in range(3):
    while True:
        user_input = input("입력하세요")
        if 5 <= len(user_input) <= 20 :
            word_list.append(user_input)
            break
        print("5이상 20이하 쳐주시오")
    
word_select = list(word_list[random.randint(0, 2)])
word_printed = word_select[:]

print(word_select)
char_num_word = len(word_printed)
blid_word_len = char_num_word / 2
# 반올림처리
if blid_word_len < char_num_word // 2:
    blid_word_len += 1
    
blind_num_word = int(blid_word_len)

list_blind_index = [value for value in range(0, char_num_word)]
print(list_blind_index)

for index in range(1, char_num_word - blind_num_word):
    del list_blind_index[random.randint(0, len(list_blind_index) - 1)]

print(list_blind_index)

for index in list_blind_index:
    word_printed[index] = "_"

print(word_printed)

while len(list_blind_index):
    print(word_printed)
    
    input_value = input("글자를 입력하세요")
    
    found_list = []
    
    for index in list_blind_index:
        if word_select[index] == input_value:
            word_printed[index] = input_value
            found_list.append(index)
            
    for found in found_list:
        list_blind_index.remove(found)
        
print(word_printed)

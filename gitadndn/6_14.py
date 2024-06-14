import random
# 나중에 마무리 하기
# 글자 입력
# number = ["첫", "두", "세"]
# word_list = []
# input_value = (input (f"{number[index]}글자를 입력하세요") for _ in range(3))
# if 5 <= len(input_value) <= 20:
#     word_list.append(input_value)

print(word_list)

word_select = list(word_list[random.randint(0,1)])
print(word_select)
word_print = word_select [:]

# 글자 반갈죽
char_num_word = len(word_select)
blind_num_word = (char_num_word + 1) // 2
blind_num_word = int(blind_num_word)
print(blind_num_word)

# 블라인드 처리화
blind_num_list = [index for index in range(char_num_word)]
print(blind_num_list)
for index in range(0, char_num_word - blind_num_word):
    del blind_num_list[random.randint(0, len(blind_num_list) -1)]
print(blind_num_list)

for index in blind_num_list:
    word_print[index] = "_"
print(word_print) 

count = 0
# 답 맞추기
while len(blind_num_list) > 0:
    print(word_print)
    found_list = []
    count += 1
    input_value = input(f"시도횟수 {count}정답을 입력하세요")
    
    for index in blind_num_list:
        if word_select[index] == input_value:
            word_print[index] = input_value
            found_list.append(index)
            
    for f_index in found_list:
        blind_num_list.remove(f_index)
        
print(f"시도 횟수 {count} 정답 : {word_print}")
        
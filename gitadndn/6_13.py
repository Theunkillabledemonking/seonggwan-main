import random
# 글자 입력
word_list = ["hello", "hello"]

# 선택
word_select = list(word_list[random.randint(0,1)])
print(word_select)
word_print = word_select[:]

# 글자를 반올림 시키기
char_word_num = len(word_select)
print(char_word_num)
if char_word_num % 2 == 0:
    bchar_word_num = char_word_num // 2 
else :
    bchar_word_num = char_word_num // 2 + 1
bchar_word_num = int(bchar_word_num)
# char_word_num = (char_word_num + 1) // 2
print(char_word_num)
# 블라인드 처리 화
blind_word_num = [index for index in range(len(word_select))]
print(blind_word_num)


for index in range(0, char_word_num - bchar_word_num):
    del blind_word_num[random.randint(0, len(blind_word_num) - 1)]
print(blind_word_num)

# 단어 _ 로 바꾸기
for index in blind_word_num:
    word_print[index] = "_"
print(word_print)
# 정답 맞추기

user_try = 0
while len(blind_word_num) > 0:
    print(word_print)
    user_try += 1
    input_value = input(f"{user_try}번째 입력 입력하세요")
    
    found_list = []
    
    for index in blind_word_num:
        if word_select[index] == input_value:
            word_print[index] = input_value
            found_list.append(index)
            
    for f_index in found_list:
        blind_word_num.remove(f_index)
        
print("정답",''.join(word_print))
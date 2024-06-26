# 문자열 검색을 위한 사전 문자 입력 문장
sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 개행 문자가 포함된 여러 줄 문자열 출력
print(sentence)

# 전체 문장
# 단어의 개수, 전체 문자, 수 줄 수
word_list = []
msg = ""
word_count = 0
line_count = 1
index = 0
index_list = [0]

for i in sentence:
    if i == " ":
        index += 1
    
    if not (i == " " or i == "\n"):
        index += 1
        word_count += 1
        msg = msg + i
        
    elif i == " " or i == "\n":
        if msg:  # 빈 문자열이 아닌 경우에만 추가
            word_list.append(msg)
            index_list.append(index)
            msg = ""
        if i == "\n":
            line_count += 1
            index += 5  # 개행 문자는 인덱스를 3으로 계산
    
if msg != "":
    word_list.append(msg)
    index_list.append(index)

# 공백 문자열 제거
word_index_list = [int(value) for value in range(len(word_list))]
print("Word index list:", word_index_list)

for i in word_index_list:
    if word_list[i] == '':
        del word_list[i]
        break
print("Cleaned word list:", word_list)

# 유저 입력
while True:
    input_value = input("검색할 문자열을 입력하세요: ")
    
    # 해당 문자가 없을시 다시 입력
    if input_value not in word_list:
        print("해당 문자열이 없습니다. 다시 입력해주세요.")
        continue

    # 검색된 문자열의 개수
    found_count = 0
    for i in word_list:
        if i == input_value:
            found_count += 1
    print("검색된 문자열의 개수:", found_count)
    
    # 검색된 문자열의 위치
    found_list = []
    word = 0
    for i in word_list:
        if i == input_value:
            found_list.append(index_list[word])
        word += 1
    
    print("검색된 문자열의 위치:", found_list)
    
    # 단어의 개수
    print("단어의 개수:", len(word_list)) 
    
    print("전체 문자의 수:", word_count)
    
    # 줄 수
    print("줄 수:", line_count)
    break

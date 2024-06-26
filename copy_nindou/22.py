# 문자열 검색 프로그램
# 요구사항:
# 1. 미리 입력된 문장에서 검색 문자열을 입력 받고,
# 2. 입력된 문자열이 있을 경우 검색 결과를 출력한 후 프로그램을 종료
# 3. 만약 검색된 결과가 없을 경우 검색 문자를 재입력 받는다

# split 사용 금지split 사용 금지split 사용 금지split 사용 금지split 사용 금지

sentence = """pos pos hello  bar
    foo bar foo pos kin pos
    test test pos"""

index = 1
index_list = [0]
# 전체 문자 수
total_word = 0
# 줄 수 카운트
line_count = 1
word = ""
word_list = []
for i in sentence:
    if not (i == ' ' or i == "\n"):
        total_word += 1
        word = word + i
        index += 1
    elif i == ' ' or i == "\n":
        word_list.append(word)
        index_list.append(index)
        word = ""
    if i == " " :
        index += 1
    if i == "\n":
        line_count += 1
        index += 1
word_list.append(word)
index_list.append(index)
print(index_list)

word_list_index = [value for value in range(len(word_list))]
for i in word_list_index:
    if word_list[i] == '':
        del word_list[i]
        break

# 문자열 카운트
word_count = 0

# • 기능 상세
# – 문자열 검색
while True:
    # ① 입력 받은 문자열이 문장 내 있을 경우
    user_input = input("검색할 문자열을 입력하세요: ")
    
    # ② 입력 받은 문자열이 문장 내 없을 경우
    # – 해당 문자열이 없음을 화면에 출력하고, 검색할 문자열을 재입력 받는다
    # – 검색된 문자열이 있을 때 까지 반복한다
    if user_input not in word_list:
        print("해당 문자열이 없습니다. 다시 입력해주세요.")
        continue
    
    #  검색된 문자열에 대한 정보를 출력
    # » 검색된 문자열의 개수
    for i in word_list:
        if i == user_input:
            word_count += 1
    print(f"검색된 문자열의 개수: {word_count}")
    # » 검색된 문자열의 위치(들)
    # • 위치는 문자열이 시작되는 인덱스를 기준으로 하며, 문장의 첫 번째 글자는 인덱스 0으로 한다
    # • 예를 들어, "hello world"에서 "o"를 검색하면, 위치는 [4, 7]로 출력
    user_input_list = []
    user_input_list += user_input
    sentence = list(sentence)
    sentence_index = [int(value) for value in range(len(sentence))]
    save_list = []
    
    trigger = True
    for i in sentence_index:
        if trigger == True:
            if sentence[i] == user_input_list[0]:
                save_list.append(i)
                trigger = False
        if trigger == False:
            if sentence[i] == " ":
                trigger = True
    print(f"검색된 문자열의 위치: {save_list}")
    #  전체 문장에 대한 정보를 출력
    # » 단어의 개수 (단어는 띄어쓰기로 구분)
    print(f"단어의 개수: {len(word_list)}")
    # » 전체 문자 수(공백과 개행 문자를 제외한 글자 수)
    print(f"전체 문자 수: {total_word}")
    # » 줄 수 (The number of lines)
    print(f"줄 수: {line_count}")
    
    break
    
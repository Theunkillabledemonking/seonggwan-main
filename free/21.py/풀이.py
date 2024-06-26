msg = """pos pos bar
    foo bar pos
    test test pos"""
 


count = 0 # 전체 문자 수
count_line = 1 # 줄 수
count_word = 0 # 단어 수
count_found_word = 0 # 찾은 단어의 수
count_char = 0 # 공백과 줄바꿈을 제외한 문자 수
find_list = [] # 찾은 단어의 시작 인덱스를 저장하는 리스트

prev = "" # 이전 글자를 저장하기 위한 변수

find_word = input("단어를 입력하세요") #찾을 단어
find_word_index = 0 #찾을 단어의 인덱스
find_word_len = len(find_word)  #찾을 단어의 길의

for cur in msg: 
    # 현재 문자가 찾을 단어의 현재 인덱스와 일치하는지 확인
    if find_word[find_word_index] == cur :
        find_word_index += 1
        if find_word_index == find_word_len: # 찾을 단어의 모든 문자가 일치하는 경우
            count_found_word += 1 #찬은 단어 수 추가
            find_word_index = 0 # 단어 인덳 ㅡ초기화화
            find_list.append(count - find_word_len + 1) #단어의 시착 위치 저장
    else:
        find_word_index = 0        # 문자가 일치하지않을 경우 초기화
    
    #현재 문자가 공백이나 줄바꿈이 아닌 ㅕㅇ우
    if cur != " " and cur != "\n": 
        # 이전 문자도 공백이나 줄바꿈이 아닌경우
        if prev != " " and prev != "\n":
            count_word += 1 # 단어 수추가

    # 마지막 문자 처리
    elif count == len(msg) - 1: #마지막 글자
        if prev != " " and prev != "\n":
            count_word += 1 # 단어 수 추가

    # 현재 문자가 공백이나 줄바꿈이 아닌 경우
    if cur != " " and cur != "\n":
        count_char += 1 # 공백과 줄바꿈을 제외한 문자 수 증가

    # 현재 문자가 줄바꿈인 경우
    if cur == "\n":
        count_line += 1
    count += 1
    
    prev = cur # 현재 글자를 이전 글자로 업데이트


print(f"총 글자 수 : {count_char}")
print(f"총 줄 수 : {count_line}")
print(f"총 개수", count_word)
print(f"검색된 단어 수 :", count_found_word)
print(f"검색된 단어 위치: {find_list}")
# for 문으로 돌리는건 비효율적이다 왜? 메모리


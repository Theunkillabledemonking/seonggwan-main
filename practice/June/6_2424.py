msg = """pos pos hello  bar
    foo bar foo pos kin pos
    test test pos"""
 


count = 0
count_line = 1
count_word = 0
count_found_word = 0
count_char = 0
find_list = []

prev = "" # 이전 글자를 저장하기 위한 변수

find_word = "test"
find_word_index = 0
find_word_len = len(find_word)

for cur in msg:
    if find_word[find_word_index] == cur :
        find_word_index += 1
        if find_word_index == find_word_len: # 글자 찾음
            count_found_word += 1
            find_word_index = 0
            find_list.append(count - find_word_len + 1)
    else:
        find_word_index = 0        
    
    if cur != " " and cur != "\n":
        if prev != " " and prev != "\n":
            count_word += 1
    elif count == len(msg) - 1: #마지막 글자
        if prev != " " and prev != "\n":
            count_word += 1

    if cur != " " and cur != "\n":
        count_char += 1

    if cur == "\n":
        count_line += 1
    count += 1
    
    prev = cur # 현재 글자를 이전 글자로 업데이트

print(prev)
print(f"총 글자 수 : {count_char}")
print(f"총 줄 수 : {count_line}")
print(f"총 개수", count_word)
print(f"검색된 단어 수 :", count_found_word)
print(f"검색된 단어 위치: {find_list}")
# for 문으로 돌리는건 비효율적이다 왜? 메모리


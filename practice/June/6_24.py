sentence = """pos pos hello  bar
foo bar foo pos kin pos
test test pos"""

# 문자열의 길이를 계산하는 함수
def len_(m):
    c = 0
    for i in m:
        c += 1
    return c

# 단어의 개수와 문자의 수를 세기 위한 초기화
m = ""
msg_li = []
cher_li = []
for i in sentence:
    if (i == " " or i == "\n"):
        if len_(m) >= 1:
            msg_li.append(m)
            m = "" # 초기화
        else:
            m = "" # 초기화
            continue
    else:
        m += i
        cher_li.append(i)
if len_(m) >= 1:
    msg_li.append(m)

# 문자열의 위치를 찾는 함수
def num_msg(msg):
    li = [] # 위치 저장할 리스트
    m = "" # 단어를 누적하기 위한 변수
    n = 1 # 줄 수 (1로 초기화)
    for i in range(len_(sentence)): # 문장의 각 문자 i에 대해 루프를 돌린다.
        # 단어의 위치를 찾기, 공백 또는 개행 문자를 만나면, 현재 단어 "m"이 "msg"와 일치하는 경우 위치를 계산하여 li에 추가한다.
        if (sentence[i] == " " and m == msg) or (sentence[i] == "\n" and m == msg):
            l = (i - len_(m) + (4 * n)) # 위치 계산
            li.append(l)
        # 공백이나 개행 문자일 경우 m 초기화 후, 개행 문자인 경우 n을 증가 시킨다.
        if sentence[i] == "\n" or sentence[i] == " ":
            if sentence[i] == "\n":
                n += 1
            m = ""
        else: # 공백이나 개행 문자가 아닌 경우 현재 문자를 m에 추가한다.
            m += sentence[i]
    # 마지막 단어 확인
    if m == msg: # 루프가 끝난 후 마지막 단어를 확인하여 "msg"와 일치하면 위치를 계산하여 li에 추가한다.
        l = i - (len_(m) - 1) + (4 * n)
        li.append(l)
    return li, n #li와 줄수 n 반환

# 문자열을 입력 받고 해당 문자열이 있는지, 몇 개 있는지 확인
while True:
    input_msg = input('검색할 문자열을 입력하세요 : ')

    # 입력 값이 문자열에 있는지 확인
    c = 0
    for m in msg_li: # msg_li에 입력한 문자열과 일치하는 단어를 개수를 센댜.
        if m == input_msg:
            c += 1
    if c > 0: # 일치된 단어가 하나 이상인 경우 검색된 문자열의 개수를 출력 후 루프를 종료
        print("검색된 문자열의 개수 : ", c)
        break
    print("해당 문자열이 없습니다. 다시 입력해주세요.") # 없을 경우 다시 입력 요청 받음

# 문자열의 위치와 줄 수 함수 호출
li, n = num_msg(input_msg)
print("검색된 문자열의 위치 : ", li)

# 단어의 개수와 전체 문자의 수 출력
print(f"단어의 개수 : {len_(msg_li)}\n전체 문자 수 : {len_(cher_li)}")
print("줄 수 :", n)



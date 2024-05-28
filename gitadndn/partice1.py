import random

# 올림 처리 하는 함수
def numberUp(number_float):
    number_f = number_float
    number_i = int(number_float)
    
    if number_f > number_i :
        return number_i + 1
    else:
        return number_i
    
# 리스트 내에 함수가 존재하면 인덱스를 없으면 -1을 반환하는 함수
def index_catch(arg_list, arg_value):
    try:
        return arg_list.index(arg_value)
    except:
        return -1
    
# 단어 세 개를 입력 받고 랜덤으로 하나를 선택
words = []

for i in range(3):
    if i == 0:
        number = "첫"
    elif i == 1:
        number = "두"
    else:
        number = "세"
        
    word = input(f"{number} 번째 단어를 입력 하세요\n")
    
    while not (len(word) > 3 and len(word) < 20):
        word = input("3이상 20이하 글자로 구성된 단어를 입력 하세요\n")
        
    words.append(word)
    
# 랜덤으로 단어 선택 후 랜덤으로 블라인드
select = random.choice(words)
print(f"\n단어 선택 완료 게임을 시작합니다. 선택된 단어: {select}\n")

select_list = list(select)
select_list_alpha = [None for _ in range(len(select_list))]

count = 0
while count < numberUp(len(select) / 2):
    index = random.randint(0, len(select_list) -1)
    
    alpha = select_list[index]
    
    if alpha != "_":
        count += 1
        select_list_alpha[index] = select_list[index]
        select_list[index] = "_"
        
#모든 단어를 맞출 때 까지 반복
try_count = 0
while True:
    try_count += 1
    print(f"{try_count}번째 시도, 아래 단어를 구성하는 알파벳 한 개를 입력하세요.")
    print("".join(map(str, select_list)))
    
    alpha = input("\n")
    print()
    
    exist = 0
    while True:
        index = index_catch(select_list_alpha, alpha)
        
        if index != -1 :
            select_list[index] = select_list_alpha[index]
            select_list_alpha[index] = None
            exist += 1
        else:
            break
        
    count -= exist
    
    # 모든 단어를 맞추면 출력 후 종료
    if count == 0:
        print(f"Clear = 선택된 단어: {select}, 총 시도 횟수: {try_count}")
        break

    if exist == 0:
        print("단어 내 포함되지 않은 알파벳입니다.")
    else:
        print(f"입력한 알파벳 단어 내 포함: {exist}글자")
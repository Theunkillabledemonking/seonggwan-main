
#사용자로부터 여러 문장으로 구성된 하나의 문자열 입력

# 지정한 단어가 몇 번 등장하는지 카운트하는 프로그램 작성

# 단어와 문장은 공백으로 구분된다.

# 결과는 단어의 출현 횟수를 출력한다.

# 문제에서 함수는 input, print 및 형변환 함수만 사용이 가능 in, not in 연산자를 사용 x
# 문제에서 list의 append(), insert(), len() 사용가능
user_string = input("문자열 입력 :")

#.split()

user_value = input("단어 입력: ")

count = 0

word = ""


for char in user_string:
    if char == " ": # 공백을 만나면 단어가 종료됨
        if word == user_value: # 추출한 단어가 사용자가 입력한 단어와 일치하는지 확인
            count += 1
        word = "" # 단어를 초기화
    else:
        word += char #단어를 형성하기 위해 문자를 추가
#마지막 단어가 공백이 아닌 경우를 확인
if word == user_value:
    count += 1

print(f"단어'{user_value}'의 출현 빈도:{count}")
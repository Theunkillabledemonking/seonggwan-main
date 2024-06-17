# 구조적 프로그래밍 언어의 구성 요소
# 1. 주석 2. 변수 3. 연산자 4. 흐름제어 5. 함수

# 함수가 나와야지만 지역 변수가 생기는 걸로 일단 알고 잇음.
# 지역 변수와 전역 변수로 나눠짐
# 선언 후에 사용이 가능함.
# 이변수가 언제 할당이 되고 언제 해제가 되는지 확인을 해라.

# 연산자 -> 그 값을 저장하여 비교한다.
# 1.산술 2.비교 3. 논리 연산자 4. 복합 연산자 5. 기타&비트연산자
# 두번째로 우선순위 식이 있으면 나중에 계산하는것이 대입 연산자이다.
# 세번째로 기능대로 연산자를 나눌 수 있는데, 연산이 있으면 연산을 하는게 피연산자
# 오퍼레이트 갯수에 따라서 이항, 삼항 연산자로 나눠짐
# 이항 -> 연산을 할려면 연산자가 하나가 있고 좌항과 우항이 자료형일 일치해야함
# Type Consensus(데이터 타입 일치화) 명시적형변환, 묵시적형변환
# 명시적 -> 프로그래머가 함수를 이용해서 자료형을 변환 시킴
# 일시적 -> 인터프리터가 자기만의 규칙으로 자료형을 변환 시킴

# 흐름제어 
# 프로그램의 구성요소란 무엇인가?? -> 알고리즘과 데이터
# 알고리즘이란 무엇인가? -> 어떤 문제를 해결하기위한 명령어의 순서와 절차
# 구조적언어에서는 무조건 선택과 반복이 있다.
# if 시리즈 -> 모든 프로그래밍 언어에서도 똑같이 돌아가나 표기하는 방법 다름
# 반복 for & while 문이 있다 다른언어는 살짝 다름.

# 함수
# 함수를 어떻게 정의하는가 호출하는가
# overloaing을 지원을 하는가? Check할 것.

# 방학후에 pdf파일을 다시 봐서 왜 이렇게 하셨는지 확인을 할 것.

# 그래픽에서 쓰임
# def bar(arg_fnc):
#     arg_fnc()
    
# def foo():
#     print("안녕하세요 : ")
    
# bar(foo)

# 함수를 거의 안쓰고 로직 구현
# 

#     input_value = input("-을 포함한 주민등록번호를 입력하세요")
#     check_number = [2,3,4,5,6,7,8,9,2,3,4,5]
    
#     sum = 0
#     count = 0
    
#     space = ""
#     for num in input_value:
#         if num != "-":
#             space += num 

#     for num in input_value:
#         if num != "-" and count < 12 :
#             sum += int(num) * check_number[count]
#             count += 1
    
#     check_value = (11 - (sum % 11)) % 10 
    
#     if check_value == int(input_value[-1]):
#         print("유효한 값입니다.")
#     else:
#         print("유효하지 않은 값")


def get_check_digit(arg_ssid):
    #weight = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5] 쓰다보면 아래방법이 익숙
    weight = [(value % 8) + 2 for value in range(12)]
    
    ssid = [int(value) for value in arg_ssid]
    
    sum_values = sum([ssid[index] * weight[index] for index in range(12)])
    
    return (11 - sum_values % 11) % 10
    

# 유효한 주민번호 -> True else False
def is_valid_ssid(arg_ssid):
    
    arg_ssid = arg_ssid.replace("-", "")
    
    if len(arg_ssid) != 13:
        return False
    
    # 체크값 계산 알고리즘 구현 필요
    check_digit = get_check_digit(arg_ssid[:-1]) 
    if check_digit == int(arg_ssid[-1]):
        return True
    else:
        return False

print(is_valid_ssid("010410-3")) 
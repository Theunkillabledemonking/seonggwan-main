# 사용자로부터 초기값(baseValue)을 입력받아 전역 변수로 선언
baseValue = float(input("기본값을 입력하세요: "))
print("1. 더하기\n2. 빼기\n3. 곱하기\n4. 나누기")

select =int(input(f"선택 : "))
num = int(input(f"숫자 입력 : "))

sum = baseValue + num
subtraction = baseValue - num
multiply = baseValue * num


# 프로그램은 합,차,곱,나누기 모두 실행
def selectOperation():
    global baseValue
    global num
    global select
# 사용자가 연산을 선택하고 숫자를 입력하면, selectOperation() 함수에서 선택한 연산을 baseValue에 적용    
    
# selectOperation() 함수는 전역 변수 baseValue를 참조하여 연산을 실행       
 
    if select == 1: 
        return (f"연산 결과:{sum}")
    elif select == 2:
        return (f"연산 결과:{subtraction}")
    elif select == 3:
        return (f"연산 결과:{multiply}")
    elif select == 4:
        
        if num == 0:
            return(f"에러 {0}으로 나눌 수 없습니다.")    
        else :
            division = baseValue / num
            return (f"연산 결과:{division}")
# 나누기 연산에서 분모가 0일 경우, "에러: 0으로 나눌 수 없습니다"라는 메세지를 출력 이경우 연산결과 출력 x

        
print(selectOperation())









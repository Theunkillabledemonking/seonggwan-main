# 사용자 입력 받기
numbers_str = input("숫자들을 쉼표로 구분하여 입력해주세요:")
# 문자열을 숫자 리스트로 변환
numbers = numbers_str.split(',')
# 리스트 생성
int_list = []
# 더할 값 생성
sum = 0
# 초기화 값
duplication = False
# 리스트 -> int값으로 변환
for index in numbers:
    num = int(index)
    sum += num
    int_list.append(num)
    
    if sum > 100 :
        duplication = True
        break
    
if duplication :
    print("총합이 100을 초과하였습니다.")
    print("현재까지의 입력값들: ", int_list )
    print("현재까지의 총합:", sum)
else:
    print("총합이 100을 초과하지 않습니다.")
    print("현재까지의 입력값들: ", [int(num) for num in int_list])
    print("현재까지의 총합", sum)    


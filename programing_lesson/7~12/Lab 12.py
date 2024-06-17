income = int(input("소득 금액을 입력하세요: "))

#소득세 계산 함수
def calculate_tax(income):
    if (income<10000):
        tax = income * 0.1
    elif (10000<income<20000):
        tax = (income-10000) * 0.15 + 1000
    elif (income>20000):
        tax = (income-20000) * 0.2 + 2500
    return tax

#계산된 소득세 계산
tax = calculate_tax(income)

#계산된 소득세를 출력합니다.
print(f"소득세는 {tax}입니다.")

# 온도 변환 함수
def conver_celius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#사용자에게 섭씨 온도를 입력 받는다
celsius = float(input("섭씨 온도를 입력하세요: "))
    
#변환된 화씨 온도 계산
fahrenheit = conver_celius_to_fahrenheit(celsius)

#변환된 화씨 온도를 출력한다
print(f"화씨 온도는 {fahrenheit}입니다.")
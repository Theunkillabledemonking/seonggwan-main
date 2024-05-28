# 면적 단위 변환기(1)
# 사용자로부터 토지의 면적을 제곱미터(m²) 단위로 입력 받습니다.

# 1제곱미터 = 10.7639 평방피트
# 1에이커 = 4046.86 제곱미터
def convert_to_square_feet(square_meters):
    convert_to_square_feet = square_meters * 10.7639
    return convert_to_square_feet
    #여기에 제곱미터를 평방피트로 변환하는 코드를 작성하세요.

# 여기에 제곱미터를 에이커로 변환하는 코드를 작성하세요
def convert_to_acres(square_meters):
    convert_to_acres = square_meters / 4046.86
    return convert_to_acres
# 마이너스 부호가 오면 잘못된 입력이라고 출력

square_meters = float(input("토지의 면적을 제곱미터(m^2) 단위로 입력하세요: "))
if square_meters < 0 :
    print("잘못된 입력입니다.")
else :
    print(f"{square_meters}제곱미터는 {convert_to_square_feet(square_meters)} 평방피트입니다.")
    print(f"{square_meters}제곱미터는 {convert_to_acres(square_meters)} 입니다.")



# 제공된 변환 공식을 사용하여 면적을 평방비트(ft²)와 에이커(ac)로 변환합니다.

# 두 개의 함수를 정의하여 각 단위로의 변환을 담당합니다
# convert_to_square_feet: 제곱미터를 평방피트를 변환합니다
# convert_to_acres: 제곱미터를 에이커로 변환합니다.

# 입력받은 면적이 음수일 경우, 변환 대신 "잘못된 입력입니다"를 출력합니다
#이를 위해 if 선택문을 활용한다

# 변환된 면적을 평방피트와 에이커 단위를 출력한다
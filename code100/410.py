# # # 사용자 나이 입력 1번 문제
# def all_age(age):
    
#     if age<=12:
#         return "어린이 이용권을 사용가능"
    
#     elif 13<=age<=18:
#         return "청소년 이용권을 이용가능"
    
#     else :
#         return "성인 이용권 이용가능"
        


# age = int(input("사용자의 나이를 입력해주세요"))
# print(all_age(age))
# # 12세 미만 ,13세~18세 청소년 ,19세 성인

# # 2번 문제 삼각형 문제
# def tryangle(num1,num2,num3):
#     if (num1+num2<=num3) or (num2+num3<=num1) or (num3+num1<=num2):
#         return "입력하신 변의 길이로는 삼각형을 만들 수 없습니다 \n삼각형을 만들기 위해서는 어떤 두 변의 길이의 합이 다른 한 변의 길이보다 커야 합니다."
    
    
    
#     if num1 == num2 == num3 :
#         return "입력하신 변의 길이로는 정삼각형을 만들 수 있습니다."
#     elif (num1==num2) or (num2==num3) or (num1==num3):
#         return "입력하신 변의 길이로는 이등변삼각형을 만들 수 있습니다."
#     else: 
#         return "입력하신 변의 길이로는 부등변삼각형을 만들 수 있습니다."
    
# # 사용자 세변의 길이 입력

# num1 = int(input("첫 번째 변의 길이를 입력하세요: "))
# num2 = int(input("두 번째 변의 길이를 입력하세요: "))
# num3 = int(input("세 번째 변의 길이를 입력하세요: "))
# print(tryangle(num1,num2,num3))
# # 세변의 길이 삼각형 형성할 수 있는 조건을 만족 검사

# # 형성할 수 없으면 안되는지 이유를 포함한 메시지를 출력


# 사용자에게 토지의 면적을 m^2 단위로 입력

# 변환 공식을 이용하여 면적을 평방피트(ft^2)와 에이커(ac)로 변환
# 미터가 음수일때 판별
#3번
# def convert_to_square_feet(square_meters):
#     if square_meters <0:
#         return None
#     else:   
#         convert_to_square = square_meters * 10.7639
#         return f"{square_meters}제곱미터는 {convert_to_square} 평방피트입니다."

# def convert_to_acres(square_meters):
#     if square_meters <0:
#         return None
#     else: 
#         conver_to_acres = square_meters / 4046.86
#         return f"{square_meters}제곱미터는 {conver_to_acres} 에이커입니다."
# # 변환된 면적을 평방 피트와 에이커 단위로 출력
# square_meters = float(input("토지의 면적을 제곱미터(m^2) 단위로 입력하세요: "))   
# square_feet_result = convert_to_square_feet(square_meters)
# acres_result = convert_to_acres(square_meters)

# if square_feet_result is None or acres_result is None:
#     print("잘못된 입력입니다.")
# else :
#     print(square_feet_result)
#     print(acres_result)


#  #세과목 점수 입력받아 평균 점수를 계산 , 평균에 따른 학점 등급을 부여
# def calculate_average(math_score, science_score, english_score):
#     diary = (math_score+science_score+english_score) / 3
#     grade_system = {
#         'A': 90,
#         'B': 80,
#         'C': 70,
#         'D': 60,
#         'F': 0
#     }
#     for grade, threshold in grade_system.items():
#         if diary >= threshold:
#             return f"평균 점수는 {diary}, 학점은 {grade}"
    
# # 사용자로부터 수학,과학,영어의 점수를 입력


# math_score = float(input("수학 점수를 입력하세요: "))
# science_score = float(input("과학 점수를 입력하세요: "))
# english_score = float(input("영어 점수를 입력하세요: "))

# print(calculate_average(math_score,science_score,english_score))
# # 계산 후 학점 등급 결정


# 각 과목의 점수와 함께 평균 점수 및 해당하는 학점 등급 출력


# 3-1 사전 예약 시스템 시뮬레이터

def Pre_booking(age,event_code,reservation_date):
    # 예약 성공
    msg = "예약이 완료되었습니다!"
    #잘못되었을 때 거절
    if reservation_date not in range (1,31) or event_code not in ['E1', 'E2', 'E3']:
        return "잘못된 입력입니다. 프로그램을 종료합니다."
    
    if event_code == 'E1':
        if age>=18 :
            return msg
        else :
            return "나이가 맞지 않습니다."
    
    elif event_code == 'E2':
        if reservation_date % 2==0:
            return msg
        else:
            return "날짜가 맞지않습니다."
        
    
    elif event_code == 'E3': 
        if age>=16:
            if reservation_date % 7==0:
                return msg
            else: 
                return "날짜가 맞지않습니다"
        return  "나이가 맞지 않습니다"
    
    
   
# 사용자에게 나이, 이벤트 코드 ,원하는 날짜 입력
age = int(input("나이를 입력하세요: "))
event_code = input("예약하려는 이벤트 코드를 입력하세요: ")
reservation_date = int(input("원하는 예약 날짜를 입력하세요"))

print(Pre_booking(age,event_code,reservation_date))
# E1 만 18세 이상만 예약 가능
# E2 모든 연령대가 예약 가능하지만, 날짜는 짝수일에만 예약할 수 있다
# E3 만 16세 이상만 예약할 수 있으며, 7의 배수인 날짜에만 예약 가능


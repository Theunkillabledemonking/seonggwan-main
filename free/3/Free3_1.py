# def reservent_Date(age,event_code,reservation_date):
#     # 예약 성공 : "예약이 완료되었습니다."
#     success = "예약이 완료되었습니다!"
#         # 입력값이 잘못된 경우 확인
#     if not reservation_date in [i for i in range(1, 31)] or not event_code in ["E1", "E2", "E3"]:
#         return "잘못된 입력입니다. 프로그램을 종료합니다"
    
#     # E1은 만 18세 이상만 예약이 가능하다
#     if event_code == "E1" :
                
#         if age >= 18 :
#             return success
#         # 나이 미달 : "나이 제한으로 인해 예약할 수 없습니다."
#         else : 
#             return "나이 제한으로 인해 예약할 수 없습니다."
    
#     # E2는 모든 연령대가 예약 가능하지만, 날짜는 짝수일에만 예약할 수 있다   
#     elif event_code == "E2" :
        
#         if reservation_date % 2 == 0 :
#             return success
#         else :
#             return "선택하신 날짜에는 예약할 수 없습니다."
    
#     # E3는 만 16세 이상만 예약할 수 있으며, 7의 배수인 날짜에만 예약 가능  
#     elif event_code == "E3" :
        
#         if age >= 16 :
#         # 잘못된 입력 : "잘못된 입력입니다. 프로그램을 종료합니다."
#             if reservation_date % 7 == 0  :
#                 return success
#             else :
#                 return"선택하신 날짜에는 예약할 수 없습니다."
#         # 나이 미달 : "나이 제한으로 인해 예약할 수 없습니다."
#         else :
#             return "나이 제한으로 인해 예약할 수 없습니다."
#     # 잘못된 입력 : "잘못된 입력입니다. 프로그램을 종료합니다."

# # 사용자의 나이를 입력 받습니다
# age = int(input("나이를 입력하세요: "))
# # 사용자가 예약하려는 이벤트 코드 (E1,E2,E3) 하나다
# event_code = input("예약하려는 이벤트 코드를 입력하세요.")
# #사용자가 예약을 원하는 날짜는 1~30 까지의 숫자로 입력
# reservation_date = int(input("원하는 예약 날짜를 입력하세요."))

# print(reservent_Date(age,event_code,reservation_date))








# 사용자에게 입력 확인
def sub_main(age, event_code, reservation_date):
    succes = "예약이 완료되었습니다."
# 틀린경우에 검증
    if reservation_date not in range(1,31) or event_code not in ['E1', 'E2', 'E3']:
        return "잘못된 입력입니다. 프로그램을 종료합니다"


# e1 검증

# e2 검증

# e3 검증
    if event_code == 'E1':
        if age >= 18 :
            return succes
        else : 
            return "나이 제한으로 예약할 수 없습니다."
        
    elif event_code == 'E2':
        if reservation_date % 2 == 0 :
            return succes
        else:
            return "선택하신 날짜에는 예약할 수 없습니다."
    
    elif event_code == 'E3':
        if age >= 16 :
            if reservation_date % 7 == 0:
                return succes
            else:
                return "선택하신 날짜에는 예약할 수 없습니다."
        return "나이 제한으로 인해 예약할 수 없습니다."


# 출력
age = int(input("나이를 입력하세요"))
event_code = input("예약하려는 이벤트 코드를 입력하세요")
reservation_date = int(input("원하는 예약 날짜를 입력하세요: "))

print(sub_main(age, event_code, reservation_date))
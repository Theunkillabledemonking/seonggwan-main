'''
def reservation(age, event_code, reservation_date):
    #예약 성공 문구
    succes = "예약이 완료되었습니다."
    #E1 18세 이상만 예약 가능
    if event_code == 'E1':
        if age >= 18:
            return succes
        else :
            return "나이 제한으로 인해 예약 할수 없습니다."
    #E2 모든 연령대가 예약 가능 but 날짜는 짝수일만 예약 가능    
    elif event_code == 'E2':
        if reservatin_date % 2 == 0 :
            return succes
        else :
            return "선택하신 날짜에는 예약할 수 없습니다."
    #E3 만 16세이상만 예약 가능 but 7의 배수인 날짜에만 예약 가능
    elif event_code == 'E3':
        if age >= 16 :
            if reservation_date % 7 == 0 :
                return succes
            else :
                return "선택하신 날짜에는 예약할 수 없습니다."
        else :
            return "나이 제한으로 인해 예약할 수 없습니다."
    elif reservatin_date== {1~30}
        return "잘못된 입력입니다. 프로그램을 종료합니다."
# 사용자의 나이 입력
age = int(input("나이를 입력하세요:"))
# 사용자가 예약하려는 이벤트 코드 입력
event_code = (input("예약하려는 이벤트 코드를 입력하세요:"))
# 사용자가 예약을 원하는 날짜 입력
reservatin_date = int(input("원하는 예약 날짜를 입력하세요"))

print(reservation(age, event_code, reservatin_date)) 
'''

def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
    all_week = hours_per_week * 15
    panelty = absence_hours / all_week
    total_count = 20 - (20 * panelty)
    
    if tardy_count >=3 :
        all_week -= 1
    
    if absence_hours > 1/4:
        return "당신의 출석 점수는 F점 입니다"
    else :
        return f"당신의 점수는 {total_count}입니다."
    
    # 계산은 20점 - (20 * 결석시간수 / 총 수업시간 수)
    
    # 총 수업은 15주
    # 지각 3회는 결석 1시간으로 처리
    # 결석 시수가 총 수업시수의 1/4을 초과할 경우 학점 미부여 (F)
    

# 사용자에게 수업시간, 결석 시간, 지각 횟수를 입력 받기
hours_per_week = int(input("주당 수업시간"))
absence_hours = int(input("결석 시간"))
tardy_count = int(input("지각 횟수"))
# 출석 점수를 출력
print(calculate_attendance_score(hours_per_week, absence_hours, tardy_count))
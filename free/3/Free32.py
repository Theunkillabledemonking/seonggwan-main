
#score = 20 - (20 * absence_hours / (hours_week * 15) )
# 출석 점수는 20점 만점 계산식 20점 - (20 x 결석시간 수 / 총 수업시간 수)

def calculate_attendance_score(hours_per_week, absence_hours, tardy_count):
    #score = (f"당신의 출력 점수는{20 - (20 * absence_hours / hours_per_week  )}점입니다.")
    total_hours = hours_per_week * 15 # 총 수업 시간 계산
    absence_penalty = absence_hours / total_hours # 결석 시간에 대한 패널티 계산
    score = 20 - (20 * absence_penalty) # 출석 점수 계산
    
    #지각 3시간은 결석 한시간으로 처리
    if tardy_count >= 3:
        total_hours -= 1
    
    #결석 처리 규칙 : 결석시수가 총 수업시수의 1/4초과할시 학점 미부여
    if absence_penalty > 1/4:
        return "F (학점 미부여)"
    else :
        return (f"당신의 출석 점수는 {score:.2f}입니다.")
    

# 사용자로부터 주당 수업 시간(시수/주), 결석한 총 시간, 지각 횟수를 입력 받는다.
hours_week = int(input("주당 수업시간을 입력하세요: "))
absence_hours = int(input("결석한 총 시간을 입력하세요: "))
tardy_count = int(input("지각 횟수를 입력하세요: "))
# 위의 기준에 따라 계산된 출석 점수를 출력 한다.
print(calculate_attendance_score(hours_week, absence_hours, tardy_count))


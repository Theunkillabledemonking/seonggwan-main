# 입력 출발 시간(시), 출발 시간(분), 도착 시간(시), 도착 시간(분), 이동 거리(km)




time_1 = int(input("출발 시 시간을 입력하세요: "))
time_2 = int(input("출발 시 (분)을 입력하세요: "))
Time_1 = int(input("도착 시 (시간)을 입력하세요: "))
Time_2 = int(input("도착 시 (분)을 입력하세요: "))
Distance = float(input("이동 거리(Km)를 입력하세요: "))

# 총 이동 시간은 분 단위로 환산하여 계산
total_minutes1 = time_1 * 60 + time_2
total_minutes2 = Time_1 * 60 + Time_2
total_goal = total_minutes2 - total_minutes1
speed = Distance / (total_goal/60)

print(f"이동 거리: {Distance}km")
print(f"출발 시간: {time_1}시 {time_2}분")
print(f"도착 시간: {Time_1}시 {Time_2}분")
print(f"평균 속도: {speed:.2f}km/h")

if speed < 60 :
    print("속도 상태: 느림")
elif 60<= speed <90 :
    print("속도 상태: 보통")
else :
    print("속도 상태: 빠름")
# 출력 이동 거리, 도착 시간, 평균 속도(km/h), 속도 상태("느림", "보통", "빠름")

# 평균 속도가 60km/h 미만 느림, 60~90 미만 보통, 90 이상이면 빠름
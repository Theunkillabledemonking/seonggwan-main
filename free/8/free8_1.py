# 사용자로부터 온도를 입력
temperature = float(input("현재 온도(섭씨)를 입력하세요:"))
# 30도 이상 수영
if temperature >= 30:
    print(f"현재 온도 : {temperature}도")
    print("추천 활동 : 수영")
elif 30> temperature >= 20 :
    print(f"현재 온도 : {temperature}도")
    print("추천 활동 : 등산")
elif 20> temperature >= 10 :
    print(f"현재 온도 : {temperature}도")
    print("추천 활동 : 자전거 타기")   
else : 
    print(f"현재 온도 : {temperature}도")
    print("추천 활동 : 스키")
# 20도 이상 30도 미만 등산
# 10도 이상 20도 미만: 자전거 타기
# 10도 미만 스키
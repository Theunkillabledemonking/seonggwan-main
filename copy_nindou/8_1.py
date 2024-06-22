temp = int(input("현재 온도(섭씨) 입력하세요: "))

msg = "수영" if temp >= 30 else "등산" if temp >= 20 else "자전거 타기" if temp >= 10 else "스키"


print(f"현재 온도 : {temp}\n추천 활동 : {msg}")
#사용자로부터 "left", "right", "up", "down" 중 하나의 단어를 입력받는다.
direction = input("방향을 입력하세요(left, right, up, down): ")



#입력받은 값이 "left" 일시 "왼쪽으로 이동합니다" 라고 출력
if direction=="left":
    print("왼쪽으로 이동합니다.")
#입력받은 값이 "right" 일시 "오른쪽으로 이동합니다" 라고 출력
elif direction=="right":
    print("오른쪽으로 이동합니다.")
#입력받은 값이 "up" 일시 "위로 이동합니다" 라고 출력    
elif direction=="up":
    print("위로 이동합니다.")
#입력받은 값이 "down" 일시 "아래로 이동합니다" 라고 출력    
elif direction=="down":
    print("아래로 이동합니다.")
#만약 다른 단어가 입력되면 "알 수 없는 명령입니다"를 출력
else :
    print("알 수 없는 명령입니다.")


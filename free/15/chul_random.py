import random

# count_win = 0
# count_lose = 0
# count_draw = 0

count_win, count_lose, count_draw = 0, 0, 0

# 가위, 바위 보 게임 만들기

while True:
    # 승리 회수가 2번 이상 또는 패배 회수 2번 이상이면, 프로그램 종료
    if count_win >= 2 or count_lose >= 2:
        print("승리 :", "사용자" if count_win >= 2 else "컴퓨터")
        print("전적", f"{count_win}승 {count_lose}패 {count_draw}무")
        
        break

    while True:
        # 사용자로부터 입력 받기
        input_user = input("가위, 바위, 보 중 입력: ")

        if input_user == "가위" or input_user == "바위" or input_user == "보":
            break
        print("가위 바위 보 중에서 하나를 입력하세요")
    

    # 컴퓨터 랜덤하게 가위, 바위, 보 중 하나를 선택
    # random -> 정수 (integer)
    rsp = ["가위", "바위", "보"]
    input_coumputer = rsp[random.randint(0, 2)] #지금은 함수를 만들어 내는 능력이 중요

    msg_result = ""
    # 결과 판별
    # 1) 무승부
    if input_user == input_coumputer:
        msg_result = "무승부"
        count_draw += 1
    # 2) 승
    elif (input_user == "가위" and input_coumputer == "보") or \
         (input_user == "바위" and input_coumputer == "가위") or \
        (input_user == "보" and input_coumputer == "바위"):
        msg_result = "승리"
        count_win += 1
    # 3) 패
    else :
        msg_result = "패배"
        count_lose += 1
    # 출력
    print("사용자: ", input_user, "\t컴퓨터: ", input_coumputer)
    print("결과", msg_result)
    print("전적", f"{count_win}승 {count_lose}패 {count_draw}무")
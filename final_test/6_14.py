import random

def rand_comuter_mage(argStart = 0 , argEnd = 10):
#3개의 랜덤 컴퓨터 난수 생성
    # count = 0
    # rand_list = []

    # while count < 3:
    #     rand_com = (random.randint(argStart, argEnd))
        
    #     for index in range(count):ffff
    #         if rand_list[index] == rand_com:
    #             break
    #     rand_list.append(rand_com)
    #     count += 1
    
    # 다른 방법 날먹
    rand_list = [index for index in range(argStart, argEnd)]
    
    for index in range(7):
        del rand_list[random.randint(0, len(rand_list) - 1)]
    
    return rand_list
rand_list = rand_comuter_mage()
print("컴퓨터 랜덤 정수: ", rand_list)

count_trial = 0
count_strike_out = 0

while True:
    count_strike = 0
    count_ball = 0
    # 플레이어 입력
    input_value = input("3개의 숫자를 입력해주세요(공백)")
    input_list = [int(index) for index in input_value.split()]
    print(f"시도횟수 [{count_trial + 1}] 유저 입력", input_list)

    # 스트라이크 볼 카운트
    for i in range(3):
        for j in range(3):
            if input_list[i] == rand_list[i]:
                if i == j:
                    count_strike += 1
                else:
                    count_ball += 1	
                    
    # 스트라이크 아웃 카운트
    if count_strike == 0 and count_ball == 0:
        count_strike_out += 1
    print(f"Strike {count_strike}, Ball {count_ball}, Out {count_strike_out}")
    count_trial += 1
    # 게임 승리 조건 스트라이크 3회
    if count_strike >= 3:
        print("사용자 승리")
        break
    
    # 게임 패배 조건 시도 횟수 5회 or 스트라이크 아웃 2회
    if count_trial == 5 or count_strike_out == 2:
        print("사용자 패배")
        break
    

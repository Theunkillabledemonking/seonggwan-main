# 함수이름 (매개변수)
# 함수 호출 시 실행 코드

# 함수 호출 시 입력 값을 전달 할 수 있따
# -> 1) Argument(인자 값)
# -> 2) Parameter(매개변수)

# def get_sum_avg (arg_a, arg_b, arg_c):
    
#     sum = arg_a + arg_b + arg_c
    
#     avg = sum / 3
    
#     return sum, avg

# print(get_sum_avg(1, 2, 3,))

# sum, avg = get_sum_avg(1, 2, 3)
# print(sum + avg)

# bar = [3, 4, 5, 6]

# bar [1] = 10

# bar [2] = 20

# bar [0]

# bar = [2, 3, 5]

# def foo(arg_list):
#     copied_list = arg_list[:]
    
#     copied_list[0] = 100

# foo(bar)
# print(bar)

# def kin(arg_list):
#     arg_list[0] = 200

# kin(bar.copy())
# print (kin)
# print(bar)


# 야구 게임
import random
# 랜덤 컴퓨터 리스트 생성
com_list = []
for value in range(3):
    while len(com_list) < 3:
        rand_com = (random.randint(0,2))
        if rand_com not in com_list:
            com_list.append(rand_com)
            break
print(com_list)

# 사람이 세개의 값 입력

try_strike_out = 0
tryial = 0

while True:
    balls = 0
    strike = 0
    input_value = [input("입력하세요") for _ in range(3)]
    print(input_value)
    
    for i in range(3):
        for j in range(3):
            if input_value[i] == com_list[i]:
                if i == j:
                    strike += 1
                else:
                    balls += 1
                    
    print("strike : ", strike, "Balls : ", balls)
    
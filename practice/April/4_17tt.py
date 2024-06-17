# 유효값 : 1<= traial_num <= 100
# 유효범위 이외 값인 경우 에러메시지 출력 후 재입력
# import random
# number = 5
# genarated_number = []

# for char in range(number):
#     Defubed = True
#     while  genarated_number:
#         Defubed = False



# while True:

#     trail_num = int(input("N값 : "))

#     if 1 <= trail_num <= 100:
#         break
import random

# 무한루프
while True:
    
    # N 값 입력
    trail_num = int(input("N값 : "))
    
    # 입력 받은 N 값이 유효범위
    if 1 <= trail_num <= 100:
        print("으아~~ 정답이야~")
        # 무한루프 탈출
        break
    
    # 에러 메시지 출력
    print("에러: 1이상 100이하 값 입력")

# 중복 값이 없는 정수의 개수


# 중복 값이 없는 정수를 저장할 List
output_list = []

# trail_num 개수 만큼 중복값이 없는 정수 생성 후 리스트에 저장
for trial_count in range(0, trail_num):

    while True:
    
        random_num = random.randint(1, 5)
        
        found_duplication = False

        for made_index in range(0, trial_count):
            if output_list[made_index] == random_num:
                found_duplication = True
                break
        
        if not found_duplication:
            output_list.append(random_num)
            trail_num
            break

while True:
    input_index =int(input("index:"))

    if 0<= input_index < len(made_index):
        print("원소 값:",output_list[made_index])
        break
    print("x")
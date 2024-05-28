# 이 프로그램은 print, input, random.randint, len 함수 외에 다른 함수 사용해서는 안됨
# 중복 값 검사를 위해 not in, in 연산자 사용 금지
# 사용자가 입려간 n이 1미만이거나 100 초과일 경우 계속해서 입력을 받는다
# 사용자가 유효하지 않은 인덱ㅅ를 입력한 경우, 에러메시지를 출력

# 사용자에게 먼저 생성할 랜덤 정수의 개수 n을 입력

# import random
# my_list = []
# random_number = random.randint(1, 100)


# while True:
#     user_num = int(input("N값을 입력하세요: "))
#     if 100>= user_num >= 1 :
#         break
        
#     else:
#         print("에러 1이상 100 이하의 정수여야 합니다.")

# while len(my_list) < user_num:
#     new_number = random.randint(1, 100)
#     if my_list.count(new_number) == 0:
#         my_list.append(new_number)

# print("생성된 리스트:", my_list)

# while True:
#     user_num2 = int(input("원하는 원소의 인덱스를 입력하세요 (0-4): " ))
#     if 4>= user_num2>= 0:
#         print("선택한 인덱스의 원소: ",my_list[user_num2])
#         break
#     else:
#         print("에러: 유효한 인덱스 범위를 벗어 났습니다.")


import random
generated_random_num = []
while True:
    n = int(input("N의 값을 입력하세요 (1-100): "))
    if 100>= n >=1:
        break
    else:
        print("에러: N은 1이상 100 이하의 정수여야 합니다.1")



for char in range(n):

    

    while True:
        found_duplication = False
        random_num = random.randint(1,100)

        for made_num_index in range(0, char):
            if generated_random_num[made_num_index] == random_num:
            # 중복값 발생 -> 랜덤 넘버를 다시 발상해서 처음부터 다시 검사
                found_duplication = True
                break

        if not found_duplication:
            break

    generated_random_num.append(random_num)


print("생선된 리스트",generated_random_num)

while True:
     index_number = int(input(f"원하는 원소의 인덱스를 입력하세요 (0-{n-1}): " ))
     if 0 <= index_number < n :
         print("선택한 인덱스의 원소:",generated_random_num[index_number])
         break
     else:
         print("에러: 유효한 인덱스 범위를 벗어 났습니다.")
         


# 입력받은 n에 따라, 1부터 100까지 숫자 중 중복되지 않은 n개의 랜덤 숫자를 생성

# 생선된 랜덤 숫자들은 리스트에 저장

# 사용자에게 리스트에서 원하는 원소의 인덱스 입력받음

# 프로그램은 사용자가 선택한 인덱스에 해당하는 리스트의 원소를 출력한다.


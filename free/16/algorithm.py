import random

# 중복되지 않은 1 ~ 10 사이 정수 3개 생성
# in, not in, list 내 중복되지 않은 램덤 정수 생성 함수 사용 금지

# 3 7 4 : computer
# 2 3 4 : user
# result : 1 strike, 1 ball

# 여기까지만 짜도 점수가 있다.
# not in 연산자 쓰고 로직 짜기
# com_list = list()

# # 3개의 리스트 생성
# for count in range(9):

#     while True:
#     # 랜덤 값 생성 :GR
#         rand_value = random.randint(1, 10)
    
#     # 생성된 랜던 값이 리스트 내 없을 경우 로직 종료
#         if rand_value not in com_list:
#             com_list.append(rand_value)
#             break

    # 중복 값 걸려내기
    

# print(com_list)

# not in 연산자 사용하지 않고 로직 짜기
# 왜 이렇게 하냐? 파이썬을 제외하고 다른 언어에는 not in,  연산자가 존재하지 않는다
# 그러므로 알고리즘 능력을 키워서 다른 언어에도 잘 적응하기 위해서 씀

com_list = list()

count = 0


# 카운트 값이 3이 되면 종료
while count < 3:
    rand_value = random.randint(1,10)
    # 초기값을 중복값으로 없다고 설정 후 시작
    found_duplicatd_value = False

    # 카운트 수에 맞춰서 반복
    for sub_count in range(count):
        # 중복 값이 있을 경우
        if rand_value == com_list[sub_count]:
            found_duplicatd_value = True
            break #위로 올라가 다시 리스트 생성 후 검증

    # 중복값이 없을 경우 list에 rand_value값을 추가 후 카운트 1값을 추가    
    if not found_duplicatd_value :
        com_list.append(rand_value)
        count += 1



print(com_list)
    



# for i in range(5,0,-1):
#     print(" " *(5-i) +i*"*")





# # 초기화 값 설정
# total = 0
# count= 5

# # 1 ~6 까지 반복
# for i in range (1,6):
#     num=int(input(f"{i}번째 값 입력"))
#     total += num #입력받은 숫자를 결과에 더함

# average = total / count

# print(f"합계 : {total}")
# print(f"평균 : {average}")



# while문을 사용해서 정수를 처리하는 프로그램 작성

# 입력 받은 수가 양수면 "양수"라는 문자열 출력

# 입력 받은 수가 음수면 "음수"라는 문자열 출력

# while True:
#     input_num = int(input("정수를 입력 하세요"))
    
#     if input_num == 0:
#         break

#     if input_num> 0 :
#         print("양수 입니다.")
#     elif 0>input_num:
#         print("음수 입니다.")


# for i in range(6):

#     print(" " * (6-i) + ("*")* i)



# while True:
#     number = int(input("정수를 입력 하세요"))

#     if number > 0 :
#         print("양수 입니다.")
#     elif number < 0 : 
#         print("음수 입니다")
    
#     if number == 0 :
#          break

# number = 6

# for i in range (1,6):
#     print(" " * (i-1) + "*" * (6-i))


number = 0
for i in range(1,6):
    input_value = int(input(f"{i}번째 값 입력"))
    number += input_value

print("")
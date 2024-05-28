# while True:
#     # 메뉴 출력
#     print("-" * 20)
#     print("1. 구구단 출력")
#     print("2. 프로그램 종료")
#     print("-" *20)

#     # 메뉴 값 입력
#     selected_menu = input("메뉴값을 입력하세요:")


#     # 메뉴 값 == 1
#     if selected_menu == '1':
#         # 구구단의 단 입력
#         while True: # 예외가 발생하지 않은 값이 나왔을 때 더 이상의 값을 안 받음
#             dan = int(input("입력하세요")) 
#         # 해당 단의 구구단 출력
#             if 2<= dan <=9 :
#                 for num in range(1,10):
#                     print(dan, "X", num, "=", dan*num )
#                 break # 조건 찰출

#             print("단은 2~9사이의 정수 값 입력")
        

 
#     # 메뉴 값 == 2
#     elif selected_menu == '2':
#         #프로그램 종료
#         print("프로그램 종류")
#         break

#     # 메뉴 값이 != 1 and 메뉴 값 != 2
#     # 에러메세지 출력
#     else:
#         print("메뉴 값은 1 또는 2만 입력")


# # while True:
# #     input_value = int(input("양의 정수를 입력하세요"))

# #     if input_value > 0:
# #         print("입력 값은 : ", input_value)
# #         break

# #     print("양의 정수를 입력하세요")

# 1~100 사이 정수 중, 3의 배수와 7의 배수를 출력

# for i in range(1,101):
#     if i % 3 == 0 and i % 7 == 0:
# #         print(i)

# input_value = input("값 입력해라")

# if input_value == '1':
#     print("1 입니다.")

# else:
#     print("1이 아니에요~~")


# 양의 정수 5개를 입력 받아, 합과 평균을 출력하는 프로그램을 작성

#초기화 값
# total = 0

# for i in range(1,6):
#     num = int(input("양의 정수를 입력하세요"))

#     total += num
    
# print("합계",total)
# print("평균",total/5)

# input_num = 5

# sum = 0
# avg = 0.0

    
# for trial_count in range(1, input_num+1):
#     while True:
#         msg = str(trial_count) + "번째 입력:"

    
#         input_value = int(input(msg))
        
#         if input_value> 0:
#             break
#         print("에러 다시 입력하세요")
        

#     sum = sum + input_value

# avg = sum / input_num
# print(sum,avg)


# 다음과 같이 출력하는 프로그램을 작성하시오.

# 1, 3, 5, 7, 9, 11, 13, 15, 17, 19

for i in range(1,20):
    if i % 2 == 0:
        print(i)
    else:
        print(i)


# # 배수 확인 프로그램


# # 사용자로부터 정수 입력 
# # print("-"*30)
# # print("1. 홀수 짝수 구분 프로그램")
# # print("2. 3의 배수 확인 프로그램")
# # print("-"*30)

# # input_Value = (input("메뉴를 선택해 주십시오."))

# # if input_Value not in ["1","2"]:
# #     print(f"입력하신 값은 {input_Value}은 유효하지 않은 선택 값 ")
# # else:
# #     if input_Value == "1":
# #         print("홀수 짝수 구분 프로그래을 선택 하셨습니다.")
# #         insert_number = int(input("정수 값을 입력 하세요: "))
# #         if insert_number % 2 == 0:
# #             print(f"입력하신 값 {insert_number}은 짝수 입니다")
# #         else:
# #             print(f"입력하신 값 {insert_number}은 홀수 입니다")
    
# #     elif input_Value == "2":
# #         print("3의 배수 확인 프로그램을 선택 하셨습니다.")
# #         insert_number = int(input("정수 값을 입력 하세요: "))
# #         if insert_number % 3 == 0:
# #             print(f"입력하신 값 {insert_number}은 3의 배수입니다")
# #         else:
# #             print(f"입력하신 값 {insert_number}은 3의 배수가 아닙니다")





# # 사용자로 입력 받은 정수가 그 수에 맞는 배수가 맞는지 확인한다.

# # 그외에는 에러 메시지 출력

# # 사용자로부터 정수를 입력 받아 그 수가 홀수인지 짝수인지 판별

# # 사용자로부터 정수를 입력 받아 그 수가 3배의 배수인지 확인한다.

# print("-"*30)
# print("1. 홀수 짝수 구분 프로그램")
# print("2. 3의 배수 확인 프로그램")
# print("-"*30)
# # 메뉴 생성

# input_menu = (input("메뉴를 선택해 주십시오."))

# # 1과 2가 아니면 먼저 거르기
# if input_menu not in ['1','2']:
#     print(f"입력하신 값 {input_menu}은 유효하지 않은 메뉴 선택 값입니다. 메뉴 선택은 1과 2만 가능합니다. ")
# else:

#     if input_menu == '1':
#         print("홀수 짝수 구분 프로그램을 선택 하셨습니다.")
#         number_1 = int(input("정수 값을 입력해주세요"))
#         if number_1 % 2 == 0:
#             # a먼저 짝수부터
#             print(f"입력하신 값은 {number_1}짝수입니다.")
#         else:
#             print(f"입력하신 값은 {number_1}홀수입니다.")
    
#     elif input_menu == '2':
#         print("3의 배수 확인 프로그램을 선택 하셨습니다.")
#         number_2 = int(input("정수 값을 입력 하세요."))
#         if number_2 % 3 == 0:
#             print(f"입력하신 값 {number_2}, 3의 배수가 입니다.")
#         else:
#             print(f"입력하신 값{number_2}, 3의 배수가 아닙니다.")




print("-"*30)
print("1. 홀수 짝수 구분 프로그램")
print("2. 3의 배수 확인 프로그램")
print("-"*30)

# 사용자로부터 정수르 입력 받아 홀수, 짝수인지 판별
select_menu =(input("메뉴를 선택해 주십시오."))

if select_menu not in '1,2':
    print("에러 메세지")
else:


    if select_menu == '1':
        print("홀수 짝수 구분 프로그램을 선택 하셨습니다.")
        number = int(input("정수 값을 입력 하세요"))
        if number % 2 == 0 :
            print(f"입력하신 값 {number} 짝수입니다.")
        else:
            print(f"입력하신 값 {number} 홀수입니다.")

    elif select_menu == '2':
        print("3의 배수 확인 프로그램을 선택했다.")
        number = int(input("정수 값을 입력 하세요."))
        if number % 3 == 0:
            print(f"입력하신 {number}, 3의 배수입니다.")
        else:
            print(f"입력하신 값 {number}, 3의 배수가 아닙니다.")
    
# 사용자로부터 정수를 입력 받아 그 수가 3의 배수인지 확인
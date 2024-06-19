# 비밀번호 검증 ``

while True:
    password_input = input("비밀번호를 입력하세요 : ")
    
    has_upper = False
    has_digit = False
    
    for char in password_input:
        if 'A' <= char <= 'Z':
            has_upper = True
        if '0' <= char <= '9':
            has_digit = True
            
    if len(password_input) < 8 :
        print("비밀번호 길이 부족합니다.")
    elif not has_upper:
        print("대문자 영문자가 없습니다.")
    elif not has_digit:
        print("비밀번호 숫자 없습니다.")
    else:
        print("비밀번호가 안전합니다.")
        break

# while True:
#     input_password = input("비밀번호 입력하세요 : ")
    
#     alp_tf = False
#     num_tf = False
    
#     for i in input_password:
#         if 'A' <= i <= 'Z':
#             alp_tf = True
#         if '0' <= i <= '9':
#             num_tf = True
    
#     if alp_tf and num_tf and len(input_password) >= 8 :
#         print("비밀번호가 안전합니다.")
#         break
#     elif alp_tf == False and num_tf == False:
#         print("숫자와 큰 알파벳이 없습니다.")
#     elif not alp_tf:
#         print("큰 알파벳이 없습니다.")
#     elif not num_tf:
#         print("숫자가 없습니다.")
#     elif not len(input_password) >= 8 :
#         print("길이가 부족합니다.")
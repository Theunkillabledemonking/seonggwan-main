import random

def generate_password(length):
    # 대문자, 소문자, 숫자를 포함한 문자열 정의
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



    lowercase_letters = uppercase_letters.lower() #대문자 소문자 변환
    digits = '0123456789'
    # 모든 가능한 문자를 하나의 문자열로 결합
    all_characters = uppercase_letters + lowercase_letters + digits
    
    # 패스워드 초기화
    password = ""
    
    for _ in range(length):
        password += random.choice(all_characters) # 랜덤 문자를 패스워드에 추가
        
    # 생성된 패스워드 반환
    check1 = False
    check2 = False
    check3 = False
    
    # 비밀번호 검증
    for char in uppercase_letters:
        if char in password:
            check1 = True
            break
    
    for char in lowercase_letters:
        if char in password:
            check2 = True
            break
    
    for char in digits:
        if char in password:
            check3 = True
            break
        
    if check1 and check2 and check3:
        return password
    else :
        return generate_password(length)
    
password_length = int(input("패스워드를 입력하시오"))

if password_length >= 3 :
    generated_password = generate_password(password_length)
    print(generated_password)
else :
    print("3자리미만의 패스워드 x")


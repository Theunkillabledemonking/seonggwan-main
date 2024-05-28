password = input("비밀번호를 입력하세요:")
if len(password) >= 8:
    has_uppercase = False
    has_number = False
    
    for char in password():
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_uppercase = True
            
        
    if has_number and has_uppercase :
        print("비밀번호가 안전합니다.")
    else :
        print("비밀번호가 안전하지 않습니다.")
else :
    print("비밀번호가 안전하지 않습니다.")
    

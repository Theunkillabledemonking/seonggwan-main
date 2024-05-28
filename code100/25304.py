'''def password_tuer(rg):
    #비밀번호 검증
    if len(rg) != 14 or not rg[:6].isdigit() or rg[6] != '-' or not rg[7:].isdigit():
        return False
    
    front = rg[:6]
    back = rg[7:]
    total = 0
    weights = [2, 3, 4, 5, 6, 7 ,8 ,9 , 2, 3 ,4 ,5]
    
    for i in range(len(front)):
        total += int(front[i]) * weights [i]
    for i in range(len(back)-1):
        total += int(back[i]) * weights [i+6]
    #나머지 구하기
    remainder = total % 11
    #검증하기
    check_degit = (11-remainder) % 10
    
    if check_degit == int(back[-1]):
       return True
    else :
       return False


def main():
    #주민번호 입력 받기
    rg = input("주민번호를 입력하시오")
    
    #주민번호 유효성 검사
    if password_tuer(rg):
        print ("유효한 주민번호입니다.")
    else :
        print ("유효하지않은 주민번호입니다.")
    
if __name__ == "__main__":
    main()'''
    
    
    
    
    
    
    
    
# def password_reword(Rp):
#     if len(Rp) != 14 or not Rp[:6].isdigit() or Rp[6] != '-' or not Rp[7:].isdigit():
#         return False
    
#     front = Rp[:6]
#     back = Rp[7:]
#     num = 0
#     weights = [2,3,4,5,6,7,8,9,2,3,4,5]
    
#     for i in range(len(front)):
#         num += int(front[i]) * weights [i]
#     for i in range(len(back)-1):
#         num += int(back[i]) * weights [i+6]
        
#     lane1 = num % 11
#     lane2 = (11-lane1) % 10
    
#     if lane2 == int(back[-1]):
#         return True
#     else :
#         return False
    

# def main():
#     Rp = input("주민번호 입력")
    
#     if password_reword(Rp):
#         print("유효")
#     else :
#         print("유효 x")
        
# if __name__ == "__main__":
#     main()







# 물건 총 가격 입력
total = int(input())
# 물건 종류 입력
Type = int(input())
num = 0
# 물건의 가격과 갯수들 입력 후 판단

for i in range(Type):
    a, b = map(int,input().split())
    num += a*b
    
if total == num :
    print("Yes")
else :
    print("No")
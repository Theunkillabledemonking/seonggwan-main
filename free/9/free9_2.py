def password_rewar(Rg):
    if len(Rg)!=14 or not Rg[:6].isdigit() or Rg[6]!= '-' or not Rg[7:].isdigit():
        return False
    
    front = Rg[:6]
    back = Rg[7:]

    total = 0
    weights = [2,3,4,5,6,7,8,9,2,3,4,5]

    for i in range (len(front)):
        total += int(front[i]) * weights[i]
    for i in range (len(back)-1):
        total += int(back[i]) * weights[i+6]
    
    rssult_password = (11 - total % 11) % 10

    if rssult_password == int( back[-1]):
        return True
    else :
        return False


def main():
    
    Rg = input("주민번호를 입력하세요")
    
    if password_rewar(Rg):
        print ("유효한 주민번호입니다.")

    else :
        print ("유효하지 않은 주민번호.")
    
if __name__ == "__main__":
    main()
# Identity Operator
# is , is not

bar = [2,3,4] # 리스트 2,3,4
 
pos = bar # 같은 객체 선언

if bar == (foo := list((2, 3, 4))): #리스트 튜플 변환
    print("참")
else:
    print("거짓")

print("참" if bar == (foo := list((2, 3 ,4))) else "거짓")
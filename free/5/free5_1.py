# 사용자로부터 세개의 정수를 입력받는다.
def main(int1, int2, int3) :

# 세 수의 관계에 따라 다음과 같이 출력
    if int1 == int2 == int3 :
        print("모든 수가 같습니다.")
    elif int1 == int2 or int2 == int3 or int2 == int3 :
        if int1 == int2 :
            print(f"두 수가 같습니다({int1},{int2})")
        elif int2 == int3 :
            print(f"두 수가 같습니다({int2},{int3})")
        elif int3 == int1 :
            print(f"두 수가 같습니다({int1},{int3})")
            
    else: 
        max_number = max(int1, int2, int3)
        print(f"모든 수가 다릅니다. 가장 큰 수는{max_number}입니다.")



int1 = int(input("첫 번째 수 입력: "))
int2 = int(input("두 번쨰 수 입력: "))
int3 = int(input("세 번째 수 입력: "))
# 모든 수가 같으면, "모든 수가 같다"
# 두 수가 같으면, "두 수가 같습니다."와 같은 두 수도 출력
# 모든 수가 다르면, "모든 수가 다릅니다. 가장 큰 수는 x입니다." x는 가장 큰수
main(int1,int2,int3)
# print(), input(), int() 외 다른 함수의 사용 금지
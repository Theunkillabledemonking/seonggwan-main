# 사용자가 입력한 세 개의 수를 변의 길이로 하는 삼각형이 형성될 수 있는지
# 가능하다면 어떤 유형의 삼각형인지 판별
# 삼각형을 판별하기 위한 기준은 다음과 같다

# 만약 세 변의 길이가 모두 같다면, '정삼각형'입니다
# 만약 세 변의 길이가 모두 같다면, '이등변삼각형'입니다.
# 만약 세 변의 길이가 모두 다르다면, '부등변삼각형'입니다.
# 만약 어느 두 변의 길이 합이 나머지 한 변의 길이보다 작거나 같으면

# 요구사항

# 사용자로부터 세변의 길이를 입력으로 받습니다.
inputValue1 = int(input("첫 번째 변의 길이를 입력하세요: "))
inputValue2 = int(input("두 번째 변의 길이를 입력하세요: "))
inputValue3 = int(input("세 번째 변의 길이를 입력하세요: "))
# 세 변의 길이가 삼각형을 형성할 수 있는 조건을 만족하는지 검사합니다.
# 삼각형 형성되지않는 식 
if (inputValue1+inputValue2<=inputValue3) or (inputValue3+inputValue2<=inputValue1) or (inputValue3+inputValue1<=inputValue2):
    print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다. \n삼각형을 만들기 위해서는 어떤 두변의 길이의 합이 다른 한 변의 길이보다 커야 합니다")
else :
       
    if (inputValue1==inputValue2==inputValue3):
        print("입력하신 변의 길이로는 정삼각형을 만들 수 있습니다.")
    elif (inputValue1==inputValue2!=inputValue3) or (inputValue2==inputValue3!=inputValue1) or (inputValue1==inputValue3!=inputValue2):
        print("입력하신 변의 길이로는 이등변삼각형을 만들 수 있습니다.")
    else:
        print("입력하신 변의 길이로는 부등변삼각형을 만들 수 있습니다")
    
#함수는 괄호가 있다
#def FunctionName(Input):
    
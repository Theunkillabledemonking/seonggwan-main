# 사용자로붙터 수학, 과학, 영어의 점수를 입력받는다.
math = float(input("수학 점수를 입력하세요: "))
science = float(input("과학 점수를 입력하세요: "))
english = float(input("영어 점수를 입력하세요: "))

average = (math + science + english) / 3

def calculate_average(math, science, english):
    
    if average >= 90 :
        test = "A"
    
    elif 90 > average >= 80 :
        test = "B"
    
    elif 80 > average >= 70 :
        test = "C"
    
    elif 70 > average >= 60 :
        test = "D"
    
    else :
        test = "test"
    
    return average, test

average,test = calculate_average(math, science, english)
print ("평균 점수는" ,average,"점이고, 학점은",test,"입니다.")
    




# 입력받은 점스들을 바탕으로 평균 점수를 계산한다

# 계산된 평균 점수를 사용하여 학점 등급을 결정한다

# 학전 등급은 A 90이상 B 80~90 C 70~80 D 60~70 F60점 미만으로 나눠진다

# 각 과목의 점수와 함께 평균 점수 및 해당하는 학점 등급을 출력
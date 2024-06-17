score = [99, 29, 30, 40, 20, 60]

# 변수 초기화
student_num = 0
sum = 0

for i in score:
    sum += i
    student_num += 1

# 평균
avg = sum / student_num
    
print("학생 수 :", student_num, ", 총점 : ", sum, ", 평균 : ", avg)
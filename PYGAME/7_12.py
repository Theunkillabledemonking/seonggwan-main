std_grades = {} # Ditctionary

std_grades[240001] = ["홍길동", 10, 20, 30, 60, 30]
std_grades[240002] = ["홍길삼", 10, 20, 30, 60, 30]
std_grades[240003] = ["홍길사", 10, 20, 30, 60, 300]

for key, value in std_grades.items():
    print(f"학번 ({key}) 이름 : {value[0]} 국어{value[1]} 영어{value[2]} 수학{value[3]} 총점 {value[4]} 평균 {value[5]}")

print(std_grades[240003][-1])
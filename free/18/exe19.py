# 학생 점수
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99, 82, 67, 50, 77, 89]

# 점수 구분
a = [i for i in scores if i>= 90]
b = [i for i in scores if 90 > i >= 80]
c = [i for i in scores if 80 > i >= 70]
d = [i for i in scores if 70 > i >= 60]
f = [i for i in scores if 60 > i]

# 평균 값 구하는 함수
def all_averge(list):
    if len(list) >= 0 :
        return sum(list) / len(list)

# 함수 반환
a_avg = all_averge(a)
b_avg = all_averge(b)
c_avg = all_averge(c)
d_avg = all_averge(d)
f_avg = all_averge(f)

# 결과 출력
print("등급 분포 및 평균 점수:")
print(f"A 등급: 평균 점수 = {format(a_avg,".2f")}\n{"*" * len(a)} ({len(a)}명)")
print(f"B 등급: 평균 점수 = {format(b_avg,".2f")}\n{"*" * len(b)} ({len(b)}명)")
print(f"C 등급: 평균 점수 = {format(c_avg,".2f")}\n{"*" * len(c)} ({len(c)}명)")
print(f"D 등급: 평균 점수 = {format(d_avg,".2f")}\n{"*" * len(d)} ({len(d)}명)")
print(f"F 등급: 평균 점수 = {format(f_avg,".2f")}\n{"*" * len(f)} ({len(f)}명)")

        
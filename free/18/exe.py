# 학생 점수
scores = [92, 85, 34, 76, 58, 90, 61, 70, 45, 99]

woos = []
yangho = []
bootong = []
mihub = []

# 학생 점수 분류
for i in scores:
    if i >= 90 :
       woos.append(i)
    elif 90 > i >= 70 :
        yangho.append(i)
    elif 70 > i >= 50 :
        bootong.append(i)
    else:
        mihub.append(i)

def caculatd_average(score_list):
    if len(score_list) > 0:
        return sum(score_list) / len(score_list)
    else:
        return
    
woos_avg = caculatd_average(woos)
yangho_avg = caculatd_average(yangho)
bootoong_avg = caculatd_average(bootong)
mihub_avg = caculatd_average(mihub)

print(f"우수: {woos} 평균 :{woos_avg}")
print(f"양호: {yangho} 평균 :{yangho_avg}")
print(f"보통: {bootong} 평균 :{bootoong_avg}")
print(f"미흡: {mihub} 평균 :{mihub_avg}")

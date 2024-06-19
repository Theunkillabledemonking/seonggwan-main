subject_name = ["수학", "과학", "영어"]
subject_count_li = []

for i in range(len(subject_name)):
    subject_count = int(input(f"{subject_name[i]} 점수를 입력하세요 :"))
    subject_count_li.append(subject_count)
subject_count_li_sum = 0
[subject_count_li_sum := subject_count_li_sum + i for i in subject_count_li]
subject_count_li_avg = subject_count_li_sum / len(subject_count_li)

if 90 <= subject_count_li_avg:
    msg = "A"
elif 80 <= subject_count_li_avg:
    msg = "B"
elif 70 <= subject_count_li_avg:
    msg = "C"
elif 60 <= subject_count_li_avg:
    msg = "D"
else:
    msg = "F"
    
print(f"평균 점수는 {subject_count_li_avg} 점이고, 학점은 {msg} 입니다.")
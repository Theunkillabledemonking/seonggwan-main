# 학생 성적을 키보드로부터 입력 받아 리스트에 저장 후 입력 값을 출력
def printlist():
    print("=" * 25)
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력(입력 순)")
    print("3. 프로그램 종료")
    print()
    print(f"현 입력 데이터 개수 : {len(new_list)}")
    print(f"전체 학생 평균 값 : {total_avg / len(new_list):.2f}" if len(new_list) > 0 else "")
    print("=" * 25)


new_list = []
total_avg = 0

while True:
    printlist()
    input_value = int(input(""))
# 1. 학생 성적 입력 (학번, 이름, 국어 성적, 영어 성적, 수학 성적)
    if input_value == 1:
       class_num = int(input("학번을 입력하세요\n"))
       
       class_name = input("이름을 입력하세요\n")
       
       krean_score = int(input("국어 성적을 입력하세요\n"))
       
       english_score = int(input("영어 성적을 입력하세요\n"))
       
       math_score = int(input("수학 성적을 입력하세여\n"))
       
       sum_score = (krean_score + english_score + math_score)
       avg_score = sum_score / 3
       new_list.append([class_num, class_name, krean_score, english_score, math_score, sum_score,avg_score])
       total_avg += avg_score
       
# 2. 학생 목록 출력 (입력 순)
    elif input_value == 2:
        for row in new_list:
                print(f"id : {row[0]}, name : {row[1]}, kor : {row[2]}, eng : {row[3]}, math : {row[4]}, sum: {row[5]}, avg : {row[6]:.2f}")

        for col in new_list:
            for row in col:
                print(row, "\t", end="")
            print()

# 3. 프로그램 종료.
    elif input_value == 3 :
        print("프로그램 종료")
        break
    

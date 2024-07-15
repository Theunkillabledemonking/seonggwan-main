# 학생 성적 입력
def stu_grade():
    print("=" * 25)
    print("1. 학생 성적 입력")
    print("2. 학생 목록 출력(입력순)")
    print("3. 프로그램 종료")
    print(f"현 입력 데이터 갯수 : {len(my_dict)}")
    print(f"전체 학생 평균 값 {(avg_num):.2f}" if len(my_dict) > 0 else "전체 학생 평균 값 : 0.0")
    print("=" * 25)

def stu_information():
    # 학번 -> Dictionary
    input_gradenum = (input("학번을 입력하세요"))
    # 이름 입력 -> value
    input_name = input("이름을 입력하세요")
    # 국어, 영어, 수학 성적 입력
    input_korean = int(input("국어 성적을 입력하세요."))
    input_eng = int(input("영어 성적을 입력하세요"))
    input_math = int(input("수학 성적을 입력하세요"))
    # 합계 및 평균
    total_score = input_korean + input_eng + input_math
    avg_score = total_score / 3
    my_dict[input_gradenum] = {'name' : input_name, 'kor' : input_korean, 'eng' : input_eng, 'math' : input_math, 'sum' : total_score, 'avg' : avg_score}

def display_student_information():
    for key_num, value in my_dict.items():
            print(f"id : {key_num}, kor : {value['kor']}, eng : {value['eng']}, math : {value['math']}, sum : {value['sum']}, avg : {value['avg']:.2f}")
            
my_dict = {}
avg_num = 0

while True:
    stu_grade()
    input_value = int(input(""))
    
    if input_value == 1:
        stu_information()
        
    # 학생 목록 출력(입력순)
    elif input_value == 2:
        display_student_information()

    elif input_value == 3:
        sute_1, grade = (input("성적을 출력하시기 위해서는 학번과 과목을 입력하세요(스페이스 바로 구분) :").split())
        print(f"학번 {sute_1}님의 {grade}성적은 {my_dict[sute_1][grade]}입니다.")

    # 프로그램 종료
    elif input_value == 4:
        print("프로그램 종료")
        break
    
    # # 전체 학생 평균 계산
    if len(my_dict) > 0 :
         total_avg_sum = sum(student['avg'] for student in my_dict.values())
         avg_num = total_avg_sum / len(my_dict)
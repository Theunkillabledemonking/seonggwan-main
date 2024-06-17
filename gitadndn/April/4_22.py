# # 리스트를 사용하기 위해서는 리스트를 생성

# bar = [] # barㅡㄴ 참조 변수
# foo = list()

# # CRUD

# # Create : 원소 삽입
# bar.append(10) # bar -> [10]
# bar.append(20) # bar -> [10, 20]

# # index 0,  1   2
# # bar [10, 100, 20]
# #          index value
# bar.insert(1, 100)

# # Read
# # bar [10, 100, 20]

# for index in range(0, len(bar)): # 0, 3: len(리스트) -> 리스트의 원소 개수
#     print (bar[index]) # index 0 -> 2

# # bar[2]


# bar = [value for value in range(10,20)]


# #slicing 
# # 참조변수 [start:stop:step]
# # start : 0 -> stop : 4-1
# # 슬라이싱은 현재 작업하는 리스트를 건드리지 않는다
# # 지정된 범위만큼 복사를 해와서 
# foo = bar[-1:-6:-1]
# print(foo)
# print (bar)

# CRUD : Update
# Befor : [2,3,4,5,6]
# bar[1] = 20
# # After : [2, 20, 4, 5, 6]

# bar [0:3] = [100,200,300]

# print(bar)

# bar = [100,200,300,400,500,600,700]

# CRUD : Delete
# 원소 삭제: 원소 한개 삭제, 리스트 내 전체 원소 삭제
# 원소 한 개 삭제 : 세가지 방법
# 1) del 명령어를 사용해서 해당 index의 원소를 삭제
# 2) remove 함수를 이용해서 값을 이용해서 해당 원소를 삭제
# 3) pop 함수를 이용해서 해당 index의 원소를 삭제하고, 삭제된 값을 반환

# bar = [10,20,30,40,50,60]
# print("befor: ", bar, len(bar)) # [10,20,30,40,50]
# del bar[1]
# print("after: ", bar, len(bar)) # [10,30,40,50,60]

# bar.remove(50)
# print(bar, len(bar)) # [10,30,40,60] 

# print(bar.pop(2)) # 40, 
# print("after: ", bar , len(bar))

# import random
# n = 5 #범위
# max_num = 6 # 최대 값 지정

# sample_list = [ value for value in range(1, max_num) ]
# # 주어진 범위 내 리스트 생성 ,value for value 리스트 내에서 원소들을 자동적으로 생산함
# # sample_list -> [1, 2, 3, 4, 5]

# random_list = []
# # 새 리스트 생성
# for trial_count in range(0, n): # 범위반복
#     # 무작위 인덱스 번호를 지정
#     random_index = random.randint(0, len(sample_list) -1 )
#     # 무작위 숫자 뽑아냄
#     random_num = sample_list.pop(random_index)
#     # 중복된 수의 인덱스 번호를 입력하고 제거하고 수를 뽑아낸다
#     random_list.append(random_num)    
#     # ㅏ온 무작위 숫자를 새로 생성한 리스트에 집ㅇ 넣음
# print(random_list)

# bar = [1,2,3,4,5,6]
# bar.clear()
# print(bar)

# foo = [1,2,3,4,5,6]
# del foo # 리스트는 살아잇지만 참조변수를 지워서 리스트 접근 불가
# print (foo)


# 메뉴 선택안 출력

while True:
    
    print("-"*20)
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("-"*20)

    # 1. 2번 출력 그 외의 값 걸러내기
    select_num = int(input(""))
    
    if select_num == 1:
            while True:
                number = int(input("출력할 구구단의 단을 입력하세요. 구구단의 단은 2~9 사이 입력\n2~9사이 정수를 입력하세요"))
            # 구구단 입력
            #try: # 블록 내에는 예외가 발
            
                if 2<= number <= 9  : # 2~9이외의 아닐시 반복
                    for i in range(1,10): # 1~9 범위지정
                        print(f"{number} X {i} = {number * i}")
                    break # for 문에 break 걸면 1행만 실행 for문 앞인 while 문에 break를 걸어 잘못된 입력 구구단 다시
                
            #except ValueError: #
             #    print("정수를 입력하세요.")

                

    elif select_num == 2: # 이용 종료
        print("이용해주셔서 감사합니다.")
        break

    else: # 잘못 되었을때 출력
        print("잘못 입력하셨습니다. 다시 입력하세요.")

        
    

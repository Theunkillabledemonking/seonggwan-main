# while True:
#     # 사용자 입력 받기
#     numbers_str = input("숫자를 쉼표로 구분하여 입력")

#     # 문자열을 숫자 리스트로 변환
#     numbers = numbers_str.split(',')
#     #초기화 값
#     count = 0
#     total_list=[]

#     # 정수형으로 형변환
#     for num_str in numbers:
#         num = int(num_str)
#         count += num
#         total_list.append(num)

#         if count> 100:
#             print("총합이 100을 초과하였습니다..")
#             print("현재까지의 입력값들:", total_list)
#             print("현재까지의 총합",count)
#             break
    
#     # 100 초과하지 않을 경우 반복
#     if 100 > count :
#         print("총합이 100을 초과하지 않았습니다.")
#         print("입력된 모든 숫자들:", numbers)
#         print("최종 총합",count)
#     # 100 초과했을 경우 탈출
    

while True:
    # 사용자 입력 받기
    numbers_str = input("숫자를 쉼표로 구분하여 입력: ")

    # 문자열을 숫자 리스트로 변환
    numbers = numbers_str.split(',')
    
    # 입력된 모든 숫자들을 정수로 변환하여 출력
    #  print("입력된 모든 숫자들:", [int(num) for num in numbers])

    # 초기화 값
    count = 0
    total_list = []
    
    # 정수형으로 형변환하여 총합 계산
    for num_str in numbers:
        num = int(num_str)
        count += num
        total_list.append(num)
        
        # 100 초과했을 경우 탈출
        if count > 100:
            print("총합이 100을 초과하였습니다..")
            print("현재까지의 입력값들:", [int(num) for num in total_list])
            print("현재까지의 총합", count)
            break
    
    # 100 초과하지 않을 경우 반복
    if count <= 100:
        print("총합이 100을 초과하지 않았습니다.",[int(num) for num in numbers])
        print("최종 총합", count)


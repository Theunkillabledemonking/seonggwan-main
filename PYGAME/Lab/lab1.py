

import random
print("난수를 생성할 범위와 개수를 입력하세요")
while True:
    start = int(input("Start (0 이상의 정수) : "))
    if not start >= 0:
        print("0이상 숫자를 써주세요")
        continue
    # start보다 큰 입력 값
    while True:
        end = int(input(f"End는 start보다 큰 정수: "))
        if not start < end :
            print(f"End는 start({start})보다 커야 합니다.")
            continue
    # start와 end 사이의 정수
        number = int(input("N (생성할 난수의 개수)"))
        if not 1 <= number <= (end - start) :
            print(f"N은 {start}부터 {end - 1}사이의 정수여야 합니다.")
            continue
        
        index_list = []
        
        while len(index_list) < number :
            index = random.randint(start,end)
            if index not in index_list:
                index_list.append(index)
        print("생성된 난수 리스트 :")
        print(index_list)
        break
    break
    # 나중에 추후 구현
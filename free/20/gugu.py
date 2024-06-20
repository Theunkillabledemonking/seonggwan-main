import random
# 사용자에게 메뉴를 출력 1~3 범위 값 에러메세지 출력 후 재입력 요구
while True:
    print("-" * 20)
    print("1. 구구단 출력 \n2. 랜덤값 삼각형 출력\n3. 종료")
    print("-" * 20)
    input_value = int(input("원하는 메뉴 번호를 입력하세요: "))
    if not 1 <= input_value <= 3:
        print("1~3 사이의 값을 입력하세요")
        
# 지정된 범위 구구단 출력 
    if input_value == 1:
        gugudan_list = []
        while True:
            # 2~9까지의 입력만 받음
            gugudan = (input("출력할 구구단을 아래 형식으로 입력하세요 (예: 2, 2~5)\n"))
            
            # "~" 표시 지워주고 리스트로 다시 받기
            if "~" in gugudan:
                start, end = gugudan.split("~")
                start = int(''.join(start.split()))
                end = int(''.join(end.split()))
                #start, end = int(start), int(end)
                gugudan_list = [index for index in range(start, end + 1)]
                
                #예외처리
                if not (2 <= start <= 9 and 2 <= end <= 9):
                    print("2~9 사이의 값을 입력하세요.")
                    continue
            else:
                gugudan = int(gugudan)
                #예외처리
                if not 2 <= (gugudan) <= 9:
                    print("2~9 사이의 값을 입력하세요. ")
                    continue
                gugudan_list.append(gugudan)
            
            # 출력
            for i in gugudan_list:
                for j in range(1, 10):
                    print(f"{i} * {j} = {i * j}")
            break
        
# 랜덤값 숫자로 삼각형 출력
    elif input_value == 2:
        while True:
            try_value = int(input("삼각형의 높이 줄 수를 입력하세요(2 이상 3 이하) \n"))
            if not 2 <= try_value <= 3:
                print("다시 입력해주세요")
                continue
            
            # 필요한 숫자 개수
            total_number = sum(range(1, try_value + 1))
            # 중복되지 않는 숫자 생성
            rand_com = random.sample(range(10), total_number)
            index = 0
            
            #삼각형
            for i in range(try_value):
                line = ""
                for j in range(i + 1):
                    line += str(rand_com[index])
                    index += 1
                print(f" " * (try_value - i - 1) + line)
            break
        
# # 종료
    elif input_value == 3:
        print("프로그램을 종료합니다.")
        break
    
    

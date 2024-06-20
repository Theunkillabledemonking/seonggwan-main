import random
# 입력

              
    
while True:
# 메뉴 출력
    weith = 15
    print("-" * weith)
    print("1. 구구단 출력\n2. 랜덤값 삼각형 출력 \n3. 종료")
    print("-" * weith)
    input_value = int(input("원하는 메뉴 번호를 입력하세요:"))
    
# 1. 구구단 출력
    if input_value == 1:
        while True:
            gugu_list = []
            gugudan_value = input("출력할 구구단을 아래 형식으로 입력하세요. (예: 2, 2~5)")
            if "~" in gugudan_value:
                start, end = gugudan_value.split("~")
                start = int(''.join(start.split()))
                end = int(''.join(end.split()))
                if not (2 <= start <= 9 or 2 <= end <= 9):
                    print("2~9 사이의 입력값 입력")
                    continue
                gugu_list = [index for index in range(start, end + 1)]
            else:
                gugudan_value = int(gugudan_value)
                if not 2 <= gugudan_value <= 9:
                    print("2~9사이의 입력값 입력")
                    continue
                gugu_list.append(gugudan_value)  
            
            for gugu in (gugu_list):
                for i in range(1, 10):
                    print(f"{gugu} * {i} = {gugu * i}")
            break
        
# 2. 랜덤값 삼각형 출력
    elif input_value == 2:
        while True:
            try_value = int(input("삼각형의 높이 줄 수를 입력하세요."))
            index = 0
            if not 2 <= try_value <= 3:
                print("다시 입력")
                continue
            total_numbers = sum(range(1, try_value + 1))
            rand_select = random.sample(range(10), total_numbers)
            
            for i in range(try_value):
                lines = ""
                for j in range(i + 1):
                    lines += str(rand_select[index])
                    index += 1
                print(" " * (try_value - i - 1) + lines)
            break
                
# 3. 종료
    elif input_value == 3:
        print("종료")
        break
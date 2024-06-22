import random

def print_menu():
    # 프로그램 메뉴를 출력
    weith = 15
    print("-" * weith)
    print("1. 구구단\n2. 삼각형\n3. 종료")
    print("-" * weith)

def is_valid(argStart, argEnd, *num):
    # 입력한 숫자들이 주어진 범위 내에 있는지 확인한다.
    for value in (num):
        if not (argStart <= value <= argEnd):
            return False
    return True
    
def print_multiplication_talbe():
    # 사용자가 입력한 범위의 구구단으 출력한다.
    while True:
        num_value = input("2 ~ 9 까지의 숫자를 입력해주세요.")
        
        num_list = [int(value) for value in num_value.split("~")]
        
        # 입력한 숫자가 2와 9 사이의 유효한 숫자인지 확인
        
        if is_valid(2, 9, *num_list):
            break
        print("2~9")
        
    start = num_list[0]
    end = num_list[1] if len(num_list) > 1 else num_list[0]
    
    # 구구단 출력
    for gugu in range(start, end + 1):
        for j in range(1, 10):
            print(f"{gugu} * {j} = {gugu * j}")
        print()
        
def print_tryangle():
    # 사용자가 입력한 높이의 삼각형 출력 각 줄에 랜덤한 숫자가 출력
    while True:
        try_value = int(input("삼가형 높이를 입력해주세요."))
        # 높이가 2~3 사이의 유효한 숫자인지 확인
        if is_valid(2, 3, try_value):
            break
        print("2~3")
        
    index = 0
    total_num = sum(range(1, try_value + 1)) # 삼각형에 필요한 총 숫자 개수
    rand_list = random.sample(range(10), total_num) # 랜덤 숫자 리스트 생성
    
    # 삼각형 출력
    for i in range(try_value):
        lines = ""
        for j in range(i + 1):
            lines += str(rand_list[index])
            index += 1
        print(" " * (try_value - i - 1) + lines)

def print_triangle1():
    
    while True:
        row_num = int(input("삼각형의 높이를 입력하세요: "))
        
        if is_valid(2, 3, row_num):
            break
        
        print("2~3 값을 입력 하세요")
    
    # rand_list = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    rand_list = [value for value in range(10)]
    
    for rnum in range(row_num):
        # 공백 출력
        print(" " * (row_num - rnum - 1), end="")
         
        # 난수 값 출력
        for _ in range(rnum + 1):
            rand_num = rand_list[random.randint(0, len(rand_list) - 1)]
            rand_list.remove(rand_num)
            
            print(rand_num, end="")
            
        # 개행 문자
        print()
        
# 메뉴 출력
while True:
    print_menu()
    input_value = int(input("메뉴를 선택해 주세요."))
# 1. 구구단
    if input_value == 1:
        print_multiplication_talbe()

# 2. 삼각형 
    elif input_value == 2:
        print_tryangle1()

# 3. 종료
    elif input_value == 3:
        break
    
    else:
        print("올바른 메뉴 입력 구다사이")
        continue
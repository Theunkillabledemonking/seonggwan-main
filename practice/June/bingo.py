import random

# n*n 크기의 빙고 보드를 생성하는 함수
def generate_board(n):
    # 1부터 36까지의 숫자를 리스트로 생성
    numbers = []
    for i in range(1, 37):
        numbers.append(i)
    
    # 빈 보드 리스트 생성
    board = []
    # n*n개의 숫자를 보드에 채우기
    for i in range(n * n):
        # 무작위로 인덱스를 선택
        idx = random.randint(0, len(numbers) - 1)
        # 선택한 숫자를 보드에 추가
        board.append(numbers[idx])
        # 선택한 숫자를 리스트에서 제거
        numbers.pop(idx)
    
    return board

# n*n 크기의 빙고 보드를 출력하는 함수
def print_board(board, n):
    # 보드의 각 행을 출력
    for i in range(n):
        # 보드의 각 열을 출력
        for j in range(n):
            # '*'이면 '*'를 출력, 아니면 숫자를 출력
            if board[i * n + j] == '*':
                print(" *", end=" ")
            else:
                print(f"{board[i * n + j]:2}", end=" ")
        print()
    print()

# 보드에서 주어진 숫자를 '*'로 대체하는 함수
def find_and_replace(board, number):
    # 보드의 각 요소를 검사
    for i in range(len(board)):
        # 주어진 숫자를 찾으면 '*'로 대체
        if board[i] == number:
            board[i] = '*'
            break

# 빙고가 몇 줄 완성되었는지 확인하는 함수
def check_bingo(board, n):
    # 완성된 라인의 수를 저장할 변수
    lines = 0
    
    # 행을 검사
    for i in range(n):
        complete = True
        for j in range(n):
            if board[i * n + j] != '*':
                complete = False
                break
        if complete:
            lines += 1

    # 열을 검사
    for j in range(n):
        complete = True
        for i in range(n):
            if board[i * n + j] != '*':
                complete = False
                break
        if complete:
            lines += 1

    # 첫 번째 대각선을 검사
    complete = True
    for i in range(n):
        if board[i * n + i] != '*':
            complete = False
            break
    if complete:
        lines += 1
    
    # 두 번째 대각선을 검사
    complete = True
    for i in range(n):
        if board[i * n + (n - 1 - i)] != '*':
            complete = False
            break
    if complete:
        lines += 1
    
    return lines

# 사용자로부터 3 이상 6 이하의 정수를 입력받음
n = 0
while n < 3 or n > 6:
    n = int(input("Enter a number between 3 and 6: "))

# n * n 크기의 빙고 보드를 생성
board = generate_board(n)

# 초기 빙고 보드를 출력
print("Initial Bingo Board:")
print_board(board, n)

# 난수 발생 및 게임 진행
generated_numbers = []

while True:
    # 엔터 키를 눌러 난수 생성
    input("Press Enter to draw a number...")
    rand_number = random.randint(1, 36)
    # 중복되지 않는 난수를 생성
    while rand_number in generated_numbers:
        rand_number = random.randint(1, 36)
    generated_numbers.append(rand_number)
    
    # 생성된 난수를 출력
    print(f"Generated number: {rand_number}")
    # 보드에서 난수를 찾아 '*'로 대체
    find_and_replace(board, rand_number)
    # 업데이트된 빙고 보드를 출력
    print_board(board, n)
    
    # 빙고가 두 줄 이상 완성되었는지 검사
    if check_bingo(board, n) >= 2:
        print("Bingo! You have at least two completed lines. You win!")
        break

    # 모든 숫자가 생성되면 게임 종료
    if len(generated_numbers) == 36:
        print("All numbers have been drawn. Game over!")
        break

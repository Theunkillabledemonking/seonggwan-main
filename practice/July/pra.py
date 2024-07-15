# 빙고 게임
import random

# 빙고 판 개수 입력
while True:
    n = int(input("빙고판판 입력"))
    if 3 <= n <= 6:
        break
elementray_num = n *n
bingo_list = []

# 핑고 출력
def print_bingoboard(arg_nums, A=n):
    for index in range(elementray_num):
        print(arg_nums[index], "\t", end="")
        if (index + 1) % A == 0 :
            print()
 
# 빙고 리스트에 중복되지 않는 정수값 집어넣기
while len(bingo_list) < elementray_num:
    rand_num = random.randint(1, 9)
    if rand_num not in bingo_list:
        bingo_list.append(rand_num)

bingo_count = 0
# 빙고 맞추기 시작
while bingo_count < 2:
    bingo_count = 0
    print_bingoboard(bingo_list)
    
    input("엔터키를 입력해주세요")
    # 빙고 별
    rand_bingo = random.randint(1, 9)
    for i in range(elementray_num):
        if bingo_list[i] == rand_bingo:
            bingo_list[i] = "*"
            break
    
# col 로직 (세로)
    for col in range(n):
        for row in range(n):
            if bingo_list[col + (row * n)] != "*":
                    break
        else:
            bingo_count += 1
# row 로직 (가로)
    for row in range(n):
        for col in range(n):
            if bingo_list[col + (row * n)] != "*":
                break
        else:
            bingo_count += 1

# ->corss
    for index in range(n):
        if bingo_list[index * n + 1] != "*":
            break
    else:
        bingo_count += 1
# <-corss            
    for index in range(n):
        if bingo_list[index + 1 * (n - 1)] != "*":
            break
    else:
        bingo_count += 1
            
    print_bingoboard(bingo_list)
    print()


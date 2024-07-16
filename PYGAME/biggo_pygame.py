import pygame
import random

# pygame 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# 색상 정의
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
light_blue = (173, 216, 230)
yellow = (255, 255, 0)

# 빙고 판 크기 입력 받기
# while True:
#     n = int(input("빙고판 크기 입력 (3~6)"))
#     if 3 <= n <= 6:
#         break

# 빙고 판의 총 셀 수 계산


# 빙고 리스트 초기화
bingo_list = []

# 빙고 리스트 생성함수
def generate_bingo_list():
    global bingo_list
    elementary_num = n * n
    # 빙고 리스트를 빈 리스트로 초기화
    bingo_list = []
    while len(bingo_list) < elementary_num:
        rand_num = random.randint(1, 36) 
        if rand_num not in bingo_list: # 중복되지 않으면 추가
            bingo_list.append(rand_num)
            
# 빙고 리스트 생성
generate_bingo_list()

# 폰트 설정
font = pygame.font.SysFont("monospace", 50)
small_font = pygame.font.SysFont("monospace", 30)

# 빙고 보드를 그리는 함수
def draw_bingo_board(bingo_list, n):
    # 셀 크기 계싼
    cell_size = screen.get_width() // n
    for i in range(n):
        for j in range(n):
            # 셀의 x, y 좌표 계산
            
            x = j * cell_size
            y = i * cell_size
            # 셀의 사각형(Rect) 객체 생성
            rect = pygame.Rect(x, y, cell_size, cell_size)
            # 샐의 배경 색상 설정
            if bingo_list[i * n + j] == "*":
                pygame.draw.rect(screen, yellow, rect)
            else:
                pygame.draw.rect(screen, light_blue, rect)
            # 셀의 테두리 그리기
            pygame.draw.rect(screen, white, rect, 3)
            # 셀의 숫자 가져오기
            number =bingo_list[i * n + j]
            # 숫자를 텍스트로 렌더링
            text = font.render(str(number), True, black)
            # 텍스트의 중앙 위치 계산
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            # 화면에 텍스트 그리기
            screen.blit(text, text_rect)
            
# 빙고를 체크하는 함수
def check_bingo(bingo_list, n):
    bingo_count = 0
    # 세로 방향 빙고 체크
    for col in range(n):
        for row in range(n):
            if bingo_list[col + (n * row)] != "*":
                break
        else:
            bingo_count += 1
        
    # 가로 방향 빙고 체크
    for row in range(n):
        for col in range(n):
            if bingo_list[col + (n * row)] != "*":
                break
        else:
            bingo_count += 1
    
    # 대각선 왼쪽
    for index in range(n):
        if bingo_list[index * (n + 1)] != "*":
            break
    else:
        bingo_count += 1
        
    # 대각선 오른쪽
    for index in range(n):
        if bingo_list[(index + 1) * (n - 1)] != "*":
            break
    else:
        bingo_count += 1
        
    return bingo_count

# 텍스트 입력 함수
def get_bingo_size():
    input_active = True
    user_input = ""
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        size = int(user_input)
                        if 3<= size <= 6:
                            return size
                    except ValueError:
                        pass
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode
                
            screen.fill(white)
            prompt_text =small_font.rencer("Enter Bingo Size (3 ~ 6): ", True, black)
            input_text = small_font.render(user_input, True, black)
            screen.blit(prompt_text, (20, 20))
            screen.blit(input_text, (20, 60))
            pygame.display.flip()
            clock.tick(30)
            
n = get_bingo_size()
generate_bingo_list(n)

# 게임 루프
running = True
bingo_count = 0

while running:
    # 화면 지우기
    screen.fill(white)
    # 빙고 보드 그리기
    draw_bingo_board(bingo_list, n)
     
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # 엔터키가 눌리면 무작위로 한 셀을 "*"
                while True:
                    rand_index = random.randint(0, n * n - 1)
                    if bingo_list[rand_index] != "*":
                        bingo_list[rand_index] = "*"
                        break
                    
                    # 빙고 개수 체크
                    bingo_count = check_bingo(bingo_list, n)
                    
            elif event.key == pygame.K_F5:
                generate_bingo_list(n)
                bingo_count = 0
    
    # 빙고 3개 이상이면 binggo 메세지 표시
    if bingo_count >= 3:
        text = small_font.render("Bingo!", True, red)
        screen.blit(text, (20, 20))
        
    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
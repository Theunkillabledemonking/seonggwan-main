import pygame
import random

# pygame 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Falling Squares Example')

# 색상 정의
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# 사각형 크기와 속도 설정
square_size = 50
falling_speed = 200

# 사각형 리스트
falling_squares = []

# 사용자 정의 이벤트 설정
SPAWN_SQUARE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_SQUARE, 1000)  # 1초마다 사각형 생성

# fps 제어를 위한 clock 객체 생성
clock = pygame.time.Clock()

def spawn_square():
    global falling_squares  # 전역 변수 falling_squares에 접근
    num_squares = random.randint(1, 10)  # 1에서 10개의 사각형 랜덤 생성
    for _ in range(num_squares):
        x_position = random.randint(0, screen_width - square_size)
        new_square = pygame.Rect(x_position, 0, square_size, square_size)
        falling_squares.append(new_square)

new_square = pygame.Rect(screen_width / 2 - square_size, screen_height - square_size, square_size, square_size)
speed = 300

# 폰트 설정 ((폰트크기 36))
font = pygame.font.Font(None, 36)

# 게임 시작 시점의 시간을 밀리초 단위로 저장
start_time = pygame.time.get_ticks()

# 게임 루프
running = True

while running:
    # 델타 타임 계산
    dt = clock.tick(60) / 1000.0  # 60 fps로 제한
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_SQUARE:
            spawn_square()
    
    # <- -> key를 누를 때 사각형을 좌우로 이동한다.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        new_square.x -= speed * dt
    if keys[pygame.K_RIGHT]:
        new_square.x += speed * dt
    
    # 사각형 이동
    for square in falling_squares[:]:
        square.y += falling_speed * dt
        if square.top > screen_height:
            falling_squares.remove(square)
            
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # 초 단위로 변환
    
    # 화면 초기화
    screen.fill(white)
    
    # 사각형 그리기
    for square in falling_squares:
        pygame.draw.rect(screen, blue, square)
        
    # 움직이는 사각형   
    pygame.draw.rect(screen, red, new_square)
    
    break_position = new_square.collidelist(falling_squares)
    if break_position != -1:
        print("Game Over")
        running = False
    
    # 타이머 텍스트 생성
    timer_text = font.render(f"Time : {elapsed_time:.2f} seconds", True, black)
    
    # 타이머 텍스트 화면에 출력
    screen.blit(timer_text, (10, 10))
    
    # 게임 종료
    if elapsed_time > 30.0:
        game_text = font.render("You Win!", True, red)
        screen.blit(game_text, (screen_width / 2, screen_height / 2))
        running = False
        
    # 화면 업데이트
    pygame.display.flip()
    
# 게임 종료
pygame.quit()

import pygame
import random

# pygame 초기화
pygame.init()

# 사운드 로드
sound_fire = pygame.mixer.Sound("fire.mp3") # 총알 발사 사운드
sound_explosion = pygame.mixer.Sound("explosion.mp3") # 폭발 사운드
pygame.mixer.music.load("background.mp3") # 배경음악
pygame.mixer.music.play(-1)

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Falling Squares')

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0) # 총알 색상

# 폰트 설정
font = pygame.font.Font(None, 36)

# 사용자 정의 이벤트 설정
SPAWN_SQUARE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_SQUARE, 1000) # 1초마다 사각형 생성

# 게임 변수 초기화

# 플레이어 설정
player_width = 50 # 플레이어의 너비 (픽셀)
player_height = 50 # 플레이어의 높이 (픽셀)
player_speed = 300 # 플레이어의 이동 속도 (픽셀/초)
# 플레이어 위치 설정 : 화면의 하단 가운데에서 10픽셀 위
player = pygame.Rect((screen_width - player_width) // 2,\
            screen_height - player_height -10, player_width, player_height)

# 총알 설정
bullets = [] # 발사된 총알을 저장하는 리스트
bullet_speed = 500 # 총알의 이동 속도 (픽셀/초)

# 떨어지는 사각형 설정
falling_squares = [] # 떨어지는 사각형을 저장하는 리스트
falling_speed = 200 # 사각형의 떨어지는 속도 (픽셀 / 초)

# 게임 지속 시간 설정
game_duration = 30 # 게임이 지속되는 총 시간 (초)

# 지속시간 측정을 위한 현재 시간 저장
start_time = pygame.time.get_ticks()

# fps 제어를 위한 clock 객체 생성
clock = pygame.time.Clock()

# 게임 루프 시작
running = True
while running:
    dt = clock.tick(60) / 1000.0 # 게임 속도를 초당 60프레임으로 제한
    
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_SQUARE: # 떨어지는 사각형 생성 이벤트 처리
            for _ in range(random.randint(1, 5)):
                x_position = random.randint(0, screen_width - player_width)
                new_square = pygame.Rect(x_position, 0, player_width, player_height)
                falling_squares.append(new_square)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # 스페이스바를 누를 경우 총알 발사
                bullet = pygame.Rect(player.centerx - 5, player.top, 10, 20)
                bullets.append(bullet)
                sound_fire.play() # 총알 발사 사운드 재생

    # 플레이어 이동 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0: # 왼쪽 이동
        player.x -= player_speed * dt
    if keys[pygame.K_RIGHT] and player.right < screen_width: # 오른쪽으로 이동
        player.x += player_speed * dt

    # 총알 이동 및 화면 밖으로 나간 총알 제거
    for bullet in bullets[:]: # 총알 리스트를 복사하여 반복
        bullet.y -= bullet_speed * dt
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # 떨어지는 사각형 이동 및 충돌 검사
    for square in falling_squares[:]: # 사각형 리스트를 복사하여 반복
        square.y += falling_speed * dt
        if square.colliderect(player): # 플레이어와 충돌 시 게임 종료
            pygame.mixer.music.fadeout(2000) # 배경음악 서서히 종료
            print("충돌! 게임 종료")
            running = False
        for bullet in bullets[:]:
            if bullet.colliderect(square):
                sound_explosion.play() # 폭발 사운드 재생
                falling_squares.remove(square) # 사각형 삭제
                bullets.remove(bullet) # 총알 삭제
        if square.top > screen_height: # 화면 하단을 넘어간 사각형 제거
            falling_squares.remove(square)

    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

    # 게임 승리 조건 확인
    if elapsed_time >= game_duration:  
        pygame.mixer.music.fadeout(2000) # 승리 시 배경음악 서서히 종료
        print("30초 동안 생존! 승리!")
        running = False

    # 화면 그리기
    screen.fill(WHITE) # 화면을 백색으로 채움

    # 타이머 그리기 
    timer_text = font.render(f"Time: {elapsed_time:.2f} seconds", True, BLACK)
    screen.blit(timer_text, (10, 10)) # 타이머 텍스트를 화면에 그림

    # 플레이어 사각형 그리기
    pygame.draw.rect(screen, RED, player)

    # 떨어지는 사각형 그리기
    for square in falling_squares:
        pygame.draw.rect(screen, BLUE, square)

    # 총알 그리기
    for bullet in bullets:
        pygame.draw.rect(screen, YELLOW, bullet)

    # 변경사항을 화면에 출력
    pygame.display.flip()

pygame.quit()

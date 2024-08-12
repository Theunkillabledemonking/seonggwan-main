import pygame

# pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Timer Display Example')

# 사용자 정의 이벤트 생성
# spawn_enemy는 pygame.userevent에 1을 더하여 고유한 이벤트로 정의
SPAWN_ENEMY = pygame.USEREVENT + 1

# 타이머 설정 : 2초마다 SAPWN_ENEMY 이벤트가 발생하도록 설정
pygame.tiem.set_timer(SPAWN_ENEMY, 2000)

for event in pygame.event.get():
    # 발생한 이벤트가 spawnenemy인 경우 처리
    if event.type == SPAWN_ENEMY:
        #주기적으로 수행할 작업
        print("Spawn new enemy!")


# 색상 정의
White = (255, 255, 255)
Black = (0, 0, 0)

# 폰트 설정 (폰트 크기 36)
font = pygame.font.Font(None, 36) # none은 기본 시스템 폰트를 의미

# 타이머 시작 시간
start_time = pygame.time.get_ticks()

# 게임 루프
running = True

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 # 초 단위로 변환
    
    # 화면 초기화
    screen.fill(White)
    
    # 타이머 텍스트 생성
    timer_text = font.render(f"Time: {elapsed_time:.2f} seconds", True, Black)
    
    # 타이머 텍스트 화면에 출력
    screen.blit(timer_text, (10, 10)) # 왼쪽 상단 (10, 10)위치에 출력
    
    # 화면 업데이트
    pygame.display.flip()
    
pygame.quit()
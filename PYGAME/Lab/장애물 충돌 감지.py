import pygame

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Collidelist Example')

# 색상 정의
White = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0 ,0)

# rect 리스트 생성
obstacles = [
    pygame.Rect(150, 100, 100, 100), # 첫번째 150 10
    pygame.Rect(300, 300, 150, 50), # 두번째 300 300
    pygame.Rect(500, 200, 50, 150), # 세번째 500 200
    pygame.Rect(400, 400, 200, 50) # 네번째 400 400
]

# 이동하는 Rect 생성
moving_rect = pygame.Rect(50, 50, 50, 50)

# 이동 속도 설정 
velocity = 300 # 초당 300 픽셀 이동

# fps 제어를 위한 clock 객체 생성
clock = pygame.time.Clock()

#게임 루프
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 이전 위치 저장
    previous_position = moving_rect.topleft # 충돌 시 이동 준인 사각형을 멈추기 위해 이전 좌표 저장
    
    # 델타 타임 계산
    dt = clock.tick(60) / 1000.0 # 프레임 계싼
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= velocity * dt
    if keys[pygame.K_RIGHT]:
        moving_rect.x += velocity * dt
    if keys[pygame.K_UP]:
        moving_rect.y -= velocity * dt
    if keys[pygame.K_DOWN]:
        moving_rect.y += velocity * dt
    
    # 충돌 감지
    collision_index = moving_rect.collidelist(obstacles)
    if collision_index != -1:
        print(f"Collision with obstacle {collision_index}")
        # 충돌이 발생한 경우 이전 위치로 되돌리기
        moving_rect.topleft = previous_position
        
    # 화면 최화
    screen.fill(White)
    
    # 장애물 그리기
    for obs in obstacles:
        pygame.draw.rect(screen, blue, obs)
    
    # 이동하는 rect 그리기
    pygame.draw.rect(screen, red, moving_rect)
    
    # 화면 업데이트
    pygame.display.flip()
    
# 파이게임 종료
pygame.quit()
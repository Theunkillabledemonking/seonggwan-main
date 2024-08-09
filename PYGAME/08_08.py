# 장애물 및 아이템 생성
# 주어진 수의 파란색 장애물을 화면에 랜덤하게배치
# 장애물은 서로 겹치지 않아야 한다
# 주어진 수의 노란색 아이템을 화면에 랜덤하게 배치한다
# 아이템은 장애물 및 다른 아이템과 겹치지 않아야 한다

# 플레이어 조작 사각형 생성
# 사용자가 조작할 빨간색 사각형을 생성 후 화면에 랜덤하게 배치
# 이사각형은 초기 위치에서 장애물 및 아이템과 겹치지 않아야 한다

# 키보드 입력 처리

# 충돌 감지 및 처리
# 빨간색 사각형이 파란색 장애물과 충돌하면 이전 위치로 되돌린다
# 빨간색 사각형이 노란색 아이템과 충돌하면 해당 아이템을 수집하여 제거

# 게임 종료 조건
# 모든 아이템을 수집하면 모든 아이템을 수집했습니다! 승리! 메시지를 출력하고 게임을 종료


import pygame
import random

pygame.init()

screen_widht, screen_height = 800, 600
screen = pygame.display.set_mode((screen_widht, screen_height))
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
light_blue = (173, 216, 230)
green = (0, 255, 0)
yellow = (255, 255, 0)

def create_Obstacle(obstacle, size ,screen_widht, screen_height):
    obstacles = []
    for _ in range(obstacle):
        while True:
            rects = pygame.Rect(random.randint(0, screen_widht - size), \
                    random.randint(0, screen_height - size), size, size)
            if not any(rects.colliderect(o) for o in obstacles):
                obstacles.append(rects)
                break
    return obstacles

def create_items(obstacles, size, screen_widht, screen_height, block):
    items = []
    for _ in range(obstacles):
        while True:
            rects = pygame.Rect(random.randint(0, screen_widht - size), \
                                random.randint(0, screen_height - size), size, size)
            if not any(rects.colliderect(o)for o in items) and \
               not any(rects.colliderect(i) for i in block):
                    items.append(rects)
                    break
    return items
obstacles = create_Obstacle(5, 50, screen_widht, screen_height)
items = create_items(10, 10, screen_widht, screen_height, obstacles) 

# 이동하는 rect 생성
w_widht = w_height = 50

while True:
    # 이동하는 사각형을 랜덤 위치에 생성
    m_x, m_y = random.randint(0, screen_widht - w_widht), random.randint(0, screen_height - w_height)
    moving_rect =pygame.Rect(m_x, m_y, w_widht, w_height)
    # 장애물과 겹치지 않는 위치를 찾기
    if moving_rect.collidelist(obstacles) == -1 and moving_rect.collidelist(obstacles) == -1 :
        break
    

# 객체 이동 속도
speed = 300 # 300 pixel / second
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 이전 데이터 저장
    previous_data = moving_rect.topleft
    
    dt = clock.tick(60) / 1000 # dt 프로그램 실행 멈춤    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= speed * dt
    if keys[pygame.K_RIGHT]: 
        moving_rect.x += speed * dt
    if keys[pygame.K_UP]:
        moving_rect.y -= speed * dt
    if keys[pygame.K_DOWN]:
        moving_rect.y += speed * dt
    
    collision_index = moving_rect.collidelist(obstacles)
    if collision_index != -1:
        # 장애물과 충돌시 복원
        print(f"장애물 {collision_index}와 충돌! 위치 복원")
        moving_rect.topleft = previous_data
        
    item_index = moving_rect.collidelist(items)
    if item_index != -1:
        print(f"남은 아이템 {len(items) - 1}")
        del items[item_index]
    
    if not items:
        print("모두 수집완료")
        running = False
        
    screen.fill(white)
    
    for obs in obstacles:
        pygame.draw.rect(screen, light_blue, obs)
        
    for item in items:
        pygame.draw.rect(screen, yellow, item)
        
        
    pygame.draw.rect(screen, red, moving_rect)
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
pygame.quit()
 
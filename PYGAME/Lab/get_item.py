# import pygame
# import random

# pygame.init()

# # 화면 크기
# screen_width, screen_height = 800, 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Collect Items Games')

# # 색상 정의
# white = (255, 255, 255)
# Blue = (0, 0, 255)
# Red = (255, 0, 0)
# Green = (0, 255, 0)
# Yellow = (255, 255, 0)

# def create_obstacles(num_obstacles, size, screen_width, screen_height):
#     """주어진 수만큼 장애물을 생성하고, 서로 겹치치 않도록 위치를 설정"""
#     obstacles = []
#     for _ in range(num_obstacles):
#         while True:
#             rect = pygame.Rect(random.randint(0, screen_width - size), \
#                                random.randint(0, screen_height - size), size, size)
#             if not any(rect.colliderect(o) for o in obstacles): # 다른 장애물과 겹치지 않음
#                 obstacles.append(rect)
#                 break
#     return obstacles

# # 아이템 생성 함수
# def create_items(num_items, size, screen_width, screen_height, obstacles):
#     """주어진 수만큼 아이템을 생성하고, 쟁애물 및 다른 아이템과 겹치지 않도록 위치를 설정"""
#     items = []
#     for _ in range(num_items):
#         while True:
#             rect = pygame.Rect(random.randint(0, screen_width - size), \
#                                 random.randint(0, screen_height - size), size, size)
#             if not any(rect.colliderect(o) for o in obstacles) and \
#                 not any(rect.colliderect(i) for i in items):
#                     items.append(rect)
#                     break
#     return items

# # 장애물 및 아이템 생성
# obstacles = create_obstacles(5, 50, screen_width, screen_height)
# items = create_items(10, 20, screen_width, screen_height, obstacles)

# # 이동하는 Rect 생성
# m_width = m_height = 50
# while True:
#     # 이동하는 사각형을 랜덤 위치에 생성
#     m_x, m_y = random.randint(0, screen_width - m_width), random.randint(0, screen_height - m_height)
#     moving_rect = pygame.Rect(m_x, m_y, m_width, m_height)
#     # 장애물 및 아이템과 겹치지 않는 위치를 찾기
#     if moving_rect.collidelist(obstacles) == -1 and moving_rect.collidelist(items) == -1:
#         break
    
# # 이동속도 설정
# velocity = 300 # 초당 300픽셀 이동

# # fps 제어를 위한 clock 객체 생성
# clock = pygame.time.Clock()

# # 게임 루프
# running = True

# while running:
#     # 이벤트 처리
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
        
#         # 이전 위치 저장
#         previous_position = moving_rect.topleft
        
#         # 델타 타임 계산
#         dt = clock.tick(60) / 1000.0 # 초단위로 변환된 프레임당 시간
        
#         # 키 입력 처리
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT]:
#             moving_rect.x -= velocity * dt
#         if keys[pygame.K_RIGHT]:
#             moving_rect.x += velocity * dt
#         if keys[pygame.K_UP]:
#             moving_rect.y -= velocity * dt
#         if keys[pygame.K_DOWN]:
#             moving_rect.y += velocity * dt
            
#         # 충돌 감지 
#         collision_index = moving_rect.collidelist(obstacles)
#         if collision_index != -1:
#             # 장애물과 충돌 시 위치 복원
#             print(f"장애물 {collision_index}와 충돌! 위치 복원.")
#             moving_rect.topleft = previous_position
        
#         # 아이템 수집
#         item_index = moving_rect.collidelist(items)
#         if item_index != -1:
#             # 아이템 수집 후 제거
#             print(f"아이템 수집! 남은 아이템 : {len(items)-1}")
#             del items[item_index]
        
#         # 모든 아이템 수집 시 게임 종료
#         if not items:
#             print("모든 아이템을 수집했씁니다. 승리!")
#             running = False
            
#         # 화면 초기화
#         screen.fill(white)
        
#         # 장애물 그리기
#         for obs in obstacles:
#             pygame.draw.rect(screen, Blue, obs)
            
#         # 아이템 그리기
#         for item in items:
#             pygame.draw.rect(screen, Yellow, item)
        
#         # 이동하는 rect 그리기
#         pygame.draw.rect(screen, Red, moving_rect)
        
#         # 화면 업데이트
#         pygame.display.flip()
        
# # 파이게임 종료
# pygame.quit()

import pygame
import random

# 게임 초기화
pygame.init()

# 화면 크기 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Collect Items game')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
light_blue = (173, 216, 230)
green = (0, 255, 0)
yellow = (255, 255, 0)

def create_obstacles(num_obstacles, size, screen_width, screen_height):
    """주어진 장애물을 생성하고, 서로 겹치지 않도록 위치를 설정"""
    obstacles = []
    for _ in range(num_obstacles):
        while True:
            rect = pygame.Rect(random.randint(0, screen_width - size), \
                               random.randint(0, screen_height - size), size, size )
            if not any(rect.colliderect(o) for o in obstacles):
                obstacles.append(rect)
                break
    return obstacles

def create_items(num_items, size, screen_width, screen_height, obstacles):
    """주어진 수만큼 아이템을 생성하고, 장애물 및 다른 아이템과 겹치지 않도록 위치를 설정"""
    items = []
    for _ in range(num_items):
        while True:
            rect = pygame.Rect(random.randint(0, screen_width - size) , \
                                random.randint(0, screen_height - size), size, size)
            if not any(rect.colliderect(o) for o in obstacles) and \
                not any(rect.colliderect(i) for i in items):
                    items.append(rect)
                    break
    return items

# 장애물 및 아이탬 생성
obstacles = create_obstacles(5, 50, screen_width, screen_height)
items = create_items(10, 20, screen_width, screen_height, obstacles)

# 이동하는 rect 생성
m_width = m_height = 50

while True:
    # 이동하는 사각형을 랜덤 위치에 생성,
    m_x, m_y = random.randint(0, screen_width - m_width), random.randint(0, screen_height - m_height)
    moving_rect = pygame.Rect(m_x, m_y, m_width, m_height)
    # 장애물 및 아이템과 겹치치 않는 위치를 찾기
    if moving_rect.collidelist(obstacles) == -1 and moving_rect.collidelist(items) == -1 :
        break
    
# 이동속도 
speed = 300


clock = pygame.time.Clock()
running = True

while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 이전 위치 저장
    previous_position = moving_rect.topleft
    
    # 델타 타임 계산
    dt = clock.tick(60) / 1000.0
    
    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= speed * dt
    if keys[pygame.K_RIGHT]:
        moving_rect.x += speed * dt
    if keys[pygame.K_UP]:
        moving_rect.y -= speed * dt
    if keys[pygame.K_DOWN]:
        moving_rect.y += speed * dt
    
    # 충돌 감지
    collision_index = moving_rect.collidelist(obstacles)
    if collision_index != -1:
        # 장애물 충돌 시 위치 복원
        print(f"장애물 {collision_index}와 충돌! 위치 복원,")
        moving_rect.topleft = previous_position
        
    # 아이템 수집
    item_index = moving_rect.collidelist(items)
    if item_index != -1 :
        print(f"아이템 겟또 남은 아이템 : {len(items) -1}")
        
        del items[item_index]
    
    # 모든 아이템 수집시 게임 종료
    if not items:
        print("모든 아템을 수집했슴돠 승리")
        running = False
        
    # 화면 초기화
    screen.fill(white)
    
    # 장애물 그리기
    for obs in obstacles:
        pygame.draw.rect(screen, light_blue, obs)
    
    # 아이템 그리기
    for item in items:
        pygame.draw.rect(screen, yellow, item)
        
    # 이동하는 rect 그리기 
    pygame.draw.rect(screen, red, moving_rect)
    
    # 화면 업데이트
    pygame.display.flip()
    
pygame.quit()
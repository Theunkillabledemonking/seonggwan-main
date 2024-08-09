import pygame
import random


import pygame

pygame.init() # 파이게임 초기화
screen_widht, screen_height = 800, 600
screen = pygame.display.set_mode((screen_widht, screen_height)) # 화면 사이즈

# 장애물 생성
obstacles = []
x = 100
y = 50
obstacles_a = 20

for _ in range(obstacles_a):
    while True:
       obstacles_widht, obstacles_height = random.randint(0, screen_widht - x),\
           random.randint(0, screen_height- y)
       rect = pygame.Rect(obstacles_widht, obstacles_height, x, y)
       if rect.collidelist(obstacles) == -1:
           obstacles.append(rect)
           break
## ->>

# 아이템 생성
items = []
item_x = item_y = 50
item_a = 10

for _ in range(item_a):
    while True:
        item_widht, item_height = random.randint(0, screen_widht - item_x), \
            random.randint(0, screen_height - item_y)
        item_rect = pygame.Rect(item_widht, item_height, item_x, item_y)
        if item_rect.collidelist(obstacles) == -1 and item_rect.collidelist(items) == -1:
            items.append(item_rect)
            break
## ->>

# 부딪히는 플레이어 객체 생성
while True:
    player_x, player_y = 30, 30
    plyaer_widht, plyaer_height = random.randint(0, screen_widht - player_x), \
                                random.randint(0, screen_height - player_y) 
    plyaer_rect = pygame.Rect(plyaer_widht, plyaer_height, player_x, player_y)
    if plyaer_rect.collidelist(obstacles) == -1 and plyaer_rect.collidelist(items) == -1:
        break

## -->

# << -- fps 적용을 위한 시간 객체 생
clock = pygame.time.Clock()
speed = 300
## ->>
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # 이벤트가 발생할 때 실행된다.
    
    # 이벤트 처리가 끝난 후 실행
    dt = clock.tick(60) / 1000.0

    # 이전 정보를 저장
    previous_count = plyaer_rect.topleft
    
    # <- -> key를 누를 때 사각형을 좌우로 이동한다.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        plyaer_rect.x -= speed * dt
    if keys[pygame.K_RIGHT]:
        plyaer_rect.x += speed * dt
    if keys[pygame.K_UP]:
        plyaer_rect.y -= speed * dt
    if keys[pygame.K_DOWN]:
        plyaer_rect.y += speed * dt
    
    if plyaer_rect.collidelist(obstacles) != -1:
        plyaer_rect.topleft = previous_count
        
    # 코인 먹방
    coin_index = plyaer_rect.collidelist(items)
    if coin_index != -1 :
        del items[coin_index]
    
    screen.fill((255, 255, 255))
    
    for obs in obstacles:
        pygame.draw.rect(screen, (255,0,0), obs)
        
    for item in items:
        pygame.draw.rect(screen, (255, 255, 0), item)
    
    pygame.draw.rect(screen, (0, 0, 255), plyaer_rect)
    
    if not items:
        running = False
        
    
    pygame.display.flip()
    
    # pygame fps 설정

    
pygame.quit()
				# while 문 한번을 돌면 그림(사진)이 한장이 나온다.
				# 알고리즘 실행하는 순서가 그림을 그리는 순서가 된다.
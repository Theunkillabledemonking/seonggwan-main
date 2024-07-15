import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

# 화면 초기화
screen.fill((255, 255, 255)) # 배경을 흰색으로 설정
pygame.display.flip()

# 원 그리기
red = (255, 0, 0)
# rand_color = random.randint(0, 0, 0)
for _ in range(random.randint(5, 20)):
    rand_col, rand_row = random.randint(0, 799), random.randint(0, 599)
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.circle(screen, rand_color, (rand_col, rand_row), random.randint(0,40))

# 작업한 내용을 화면에 그리기
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
pygame.quit()

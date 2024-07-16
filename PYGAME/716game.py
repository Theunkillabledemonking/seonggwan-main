import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)

x1, y1 = screen.get_width() / 2, screen.get_height() / 2
x2, y2 = screen.get_height() / 2, screen.get_height() /2
radius = 40
speed1, speed2 = 20, 20


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 255)) # 배경을 흰색으로 설정
    
    # pygame.draw.circle(screen, green, (100, 200), 40)
    pygame.draw.circle(screen, red,(x1, y1), radius)
    x1 += speed1
    if x1 + radius >= screen.get_width() or x1 - radius <= 0:
        speed1 = -speed1

    pygame.draw.circle(screen,green, (x2,y2), radius)
    if y2 + radius >= screen.get_height() or y2 - radius <= 0:
        speed2 = -speed2
    y2 += speed2
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()

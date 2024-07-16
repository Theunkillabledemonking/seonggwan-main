import pygame

# 파이게임 초기화
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

x = 50
y = 240

speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 화면을 흰색으로 채운다
    screen.fill((255, 255, 255))
    
    # 원의 위치를 업데이트
    x += speed
    if x > 640 or x < 0 :
        speed = -speed
        
    # 원을 그림
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 20)
    
    # 화면 업데이트
    pygame.display.flip()
    
    # fps 설정
    clock.tick(60) # 여기에서 fps를 30 또는 60으로 변경하여 테스트

# 파이게임 종료
pygame.quit()



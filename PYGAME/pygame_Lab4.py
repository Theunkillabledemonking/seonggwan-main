import pygame
import random

# 파이게임 초기화
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True
pygame.display.flip()
        
# 게임 루프
while running:
    # 이벤트 큐에서 이벤트를 모두 가져와 순차적으로 처리
    for event in pygame.event.get():
        # 마우스 버튼을 클릭하면 발생하는 이벤트
        # 클릭된 위치에서 랜덤한 크기의 원을 그림
        if event.type == pygame.MOUSEBUTTONDOWN:
            random_color = ((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)))
            pygame.draw.circle(screen, random_color, (event.pos), random.randint(0,40))
            pygame.display.flip()
            print(f"Mouse button {event.button} clicked at positon {event.pos}")
        elif event.type == pygame.QUIT:
            running = False
        


# 파이 게임 종료
pygame.quit()
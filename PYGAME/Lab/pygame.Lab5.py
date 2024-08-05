import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

# 무작위 색상 생성
random_color = ((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)))
# 시작점 (화면 중앙) 400, 300으로 설정
start_pos = [400, 300]

clock = pygame.time.Clock()

running = True
# 방향키 입력에 따라 시작점에서 시작하여 직선을 해당 방향으로 10픽셀씩 연장
# 각 직선의 끝점은 새로운 시작점
# 직선의 색상은 프로그램 시작시 무작위로 결정되며, 이후에는 동일한 색생알 유지
while running:
     # 이벤트 큐에서 이벤트 가져오기
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    new_pos = start_pos.copy()
     
    if keys[pygame.K_LEFT]:
         new_pos[0] -= 10
    if keys[pygame.K_RIGHT]:
         new_pos[0] += 10
    if keys[pygame.K_UP]:
         new_pos[0] -= 10
    if keys[pygame.K_DOWN]:
         new_pos[0] += 10
    
    # 직선 그리기
    pygame.draw.line(screen, random_color, start_pos, new_pos, 5)
    
    # 새로운 시작점 설정
    start_pos = new_pos
    
    # 화면 업데이트
    pygame.display.flip()
    
    clock.tick(30)
    
pygame.quit()
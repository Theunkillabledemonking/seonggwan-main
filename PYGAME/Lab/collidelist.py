import pygame

pygame.init()

# 3개의 rect 객체를 생성
# (x, y, width, height)
rects = [
    pygame.Rect(20, 20, 40, 40), 
    pygame.Rect(100, 100, 50, 50),
    pygame.Rect(200, 200, 60, 60)
]

moving_rect = pygame.Rect(120, 130, 100, 100) 

# moving_rect가 rect 리스트의 어떤 rect와 충돌하는지 확인
# collidelist 메서드는 충돌한 Rect의 인데스를 반환. 충돌이 없으면 -1을 반환다.
index = moving_rect.collidelist(rects)

if index != -1:
    # 충돌이 발생한 경우, 충돌한 rect의 인덱스를 출력
    print(f"moving_rect가 rects[{index}와 충돌 했습니다.]")
else:
    # 충돌이 발생하지 않은 경우, 해당 메세지를 출력
    print("충돌이 없습니다.")
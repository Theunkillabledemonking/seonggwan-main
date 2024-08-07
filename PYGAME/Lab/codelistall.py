import pygame

pygame.init()

# 여러개의 ract 객체를 생성
# (x, y, width, height)
obstacles = [
    pygame.Rect(350, 150, 100, 100), # 첫번째 장애물 : (150, 100) 위치, 100x100 크기
    pygame.Rect(300, 300, 150, 50), # 두번째 장애물 : (300, 300) 위치, 150x50 크기
    pygame.Rect(500, 200, 50, 150), # 세번째 장애물 : (500, 200) 위치, 50x150 크기
    pygame.Rect(400, 400, 200, 50) # 네번째 장애물 : (400, 400) 위치, 200x50 크기
]

# 충돌 감지를 수행할 대상 rect 객체 생성 : 파란색
moving_rect = pygame.Rect(420, 220, 100, 100) 

# moving_rect가 obstacles 리스트 어떤 rect와 충돌하는지 확인
# collidelistall 메서드는 충돌한 모든 rect의 인덱스 리스트로 반환
# 충돌이 없으면 빈 리스트를 반환한다.
collision_indices = moving_rect.collidelistall(obstacles)

if collision_indices:
    # 충돌이 발생한 경우, 충돌한 모든 rect의 인덱스를 출력
    print(f"moving_rect가 obstacles[{collision_indices}]와 충돌했습니다. ")
else:
    # 충돌이 발생한 경우, 해당 메시지를 출력
    print(f"충돌이 없습니다.")
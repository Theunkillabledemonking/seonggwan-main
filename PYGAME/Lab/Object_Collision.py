import pygame

# pygame 초기화

# 화면 설정
screen = pygame.display.set_mode((640, 480)) # 창 생성
pygame.display.set_caption("Rectangle Collision Example") # 창의 제목 설정

# 색상 정의
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# 사각형 초기화
rect1 = pygame.Rect(300, 200, 60, 60) # (300, 200) 위치에 60x60 크기의 사각형
rect2 = pygame.Rect(100, 100, 60, 60) # (100, 100) 위치에 60x60 크기의 사각형
rect1_speed = [10, 10] #rect1 의 속동 (x, y)
rect2_speed = [10, 10] #rect2 속도 (x, y)

# fps 설정
fps = 30
clock = pygame.time.Clock()

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(fps) # 설정된 
    
    # 사각형 움직임
    rect1 = rect1.move(rect1_speed)
    rect2 = rect2.move(rect2_speed)
    
    # 화면 경계에 충돌 처리 (rect1)
    if rect1.left < 0 or rect1.right > 640 : # 화면 좌우 경계에 충돌하면
        rect1_speed[0] = -rect1_speed[0] # 방향 속도 반전
    if rect1.top < 0 or rect1.bottom > 480 : # 화면 상하에 경계에 충돌하면
        rect1_speed[1] = -rect1_speed[1] # y 방향 속도 반전
        
    # 화면 경계에 충돌 처리 (rect1)
    if rect2.left < 0 or rect2.right > 640 : # 화면 좌우 경계에 충돌하면
        rect2_speed[0] = -rect2_speed[0] # 방향 속도 반전
    if rect2.top < 0 or rect2.bottom > 480 : # 화면 상하 경계에 충돌하면
        rect2_speed[1] = -rect2_speed[1] # y 방향 속도 반전
    
    # 충돌 감지
    if rect1.colliderect(rect2):
        print("Collision Detected!") # 콘솔에 충돌 메세지 입력
    
    # 화면 그리기
    screen.fill(black) # 화면을 검정색을 ㅗ채움
    pygame.draw.rect(screen, blue, rect1)
    pygame.draw.rect(screen, red, rect2)
    pygame.display.flip() # 화면 업데이트
    
pygame.quit()
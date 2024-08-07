import pygame

pygame.init() # 파이게임 초기화

screen = pygame.display.set_mode((800, 600)) # 화면 사이즈

# << -- fps 적용을 위한 시간 객체 생
clock = pygame.time.Clock() 
## ->>

# 색상 정의
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

# 사각형 정의 ( tkrk)
rect1 = pygame.Rect(100, 50, 80, 60)
rect2 = pygame.Rect(200, 150, 120, 90)

print(rect1)
print(rect2)

speed = 50 # 사각형의 x 축 이동 속도 : 5pixel / sec
x = 0 # 사각형의 현재 x 축 좌표 값
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # 이벤트가 발생할 때 실행된다.
    
    dt = clock.tick(120) / 1000
    
    # 이벤트 처리가 끝난 후 실행
    screen.fill(white)
    
    # 사각형 그리기
    pygame.draw.rect(screen, blue, rect1) # rect 객체 이용
    pygame.draw.rect(screen, red, rect2) # tuple 자료형
    #                                x   y  가로 세로
    
    rect1.x += speed * dt
    rect2.x += speed * dt
    # pygame fps 설정
  
    
    pygame.display.flip()
    
    

# 종료
pygame.quit()

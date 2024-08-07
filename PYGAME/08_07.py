import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# 사각형 정의
rect1 = pygame.Rect(50, 100, 80, 40)
rect2 = pygame.Rect(screen.get_width()/2 - 40, 0, 80, 40)

count1 = 0
count = 0
# 객체 이동 속도
speed = 100 # 100 pixel / 1 sec
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 한번씩 눌릴때마다  event를 써야하고, 특정기간동안 입력해야된다면 key를 써야한다.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect1.x -= speed * dt
                print("왼쪽 화살표 클릭:", count)
                count += 1

    dt = clock.tick(30) / 1000

    # <- -> key를 누를 때 사각형을 좌우로 이동한다.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect1.x -= speed * dt
    elif keys[pygame.K_RIGHT]:
        rect1.x += speed * dt
        count1 +=1
        print("오른쪽 화살표 클릭",count1)
    if keys[pygame.K_UP]:
        rect1.y -= speed * dt
        print("위쪽 화살표 클릭")
    elif keys[pygame.K_DOWN]:
        rect1.y += speed * dt
        print("아래쪽 화살표 클릭")

    min(1, 10, 0, -2 ,200)
    
    # rect1.x += speed * dt
    
    # if rect1.x + rect1.width > screen.get_width():
    #     rect1.x = screen.get_width() - rect1.width
    #     speed = -speed 

    # if rect1.x < 0:
    #     rect1.x = 0
    #     speed = -speed
    
    # rect2.y += speed * dt
    
    # # if rect1.x + rect1.width 값이 > screen.width
    # #    rect1.x = screen.width - rect1.width
    
    # if rect2.bottom > screen.get_height():
    #     rect2.y = screen.get_height() - rect2.height
    #     speed = -speed
    
    # if rect2.y < 0:
    #     rect2.y = 0
    #     speed = -speed 

    
    
    
    # 화면을 흰색으로 칠한다.
    screen.fill((255, 255, 255))

    pygame.draw.rect(screen, (0, 0, 255), rect1) # Rect 객체 이용
    pygame.draw.rect(screen, (255, 0, 255), rect2) # Rect 객체 이용
    
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    
pygame.quit()



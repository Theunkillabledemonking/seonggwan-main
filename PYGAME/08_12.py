import pygame
import random

pygame.init()
screen_width, screen_hegiht = 800, 600
screen = pygame.display.set_mode((screen_width, screen_hegiht))
clock = pygame.time.Clock()
running = True

# 게임 변수
fall_rect_width = 80
fall_rect_height = 40
movingrect_width = 30
movingrect_height = 30

# 폰트 설정
font = pygame.font.Font(None, 36) #컴퓨터에서 그림을 그릴려면 폰트가 필요하다.

# 게임 시작 시점의 시간을 밀리초 단위로 저장
start_time = pygame.time.get_ticks()

# 떨어지는 사각형9599
fall_rect_list = []
def generate_fall_rect():
    for _ in range(random.randint(1, 5)):
        while True:
            rect_x = random.randint(0, screen_width - fall_rect_height)
            rect = pygame.Rect(rect_x , 0,fall_rect_width, fall_rect_height)
            
            # 기존 사각형과 충돌이 발생하지 않을 경우
            if rect.collidelist(fall_rect_list) == -1 :
                fall_rect_list.append(rect) # 현재 사각형을 리스트에 추가
                break
mov_rect_x = screen_width / 2 - movingrect_width /2
mov_rect_y = screen_hegiht /2 - movingrect_height
a_rect = pygame.Rect(screen_width/2, screen_hegiht - movingrect_height, movingrect_width, movingrect_height)


# 객체 이동 속도
speed = 100 # 300 pixel / second
rect_speed = 300
# 사용자 정의 이벤트 생성
# SPAWN_ENEMY는 pygame.USEREVENT에 1을 더하여 고유한 이벤트로 정의 
SPAWN_RECT = pygame.USEREVENT + 1

# 타이머 설정 2초마다 SPAWN_RECT 이벤트가 발생하도록 설정
pygame.time.set_timer(SPAWN_RECT, 1000) # 2000밀리초(2초)마다 이벤트 발생



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPAWN_RECT:
            generate_fall_rect()
            print("떨어지는 사각형 이벤트 발생")
             
    dt = clock.tick(60) / 1000  

    previous_top = a_rect.topleft
    elpased_time = (pygame.time.get_ticks() - start_time) /1000
    
        # <- -> key를 누를 때 사각형을 좌우로 이동한다.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        a_rect.x -= rect_speed * dt
    if keys[pygame.K_RIGHT]:
        a_rect.x += rect_speed * dt
    
    # 떨어지는 사각형의 y값 증가
    for rect in fall_rect_list:
        rect.y += speed * dt
        
    # 화면 아래이면 리스트에 삭제
    for rect in fall_rect_list[:]:
        if rect.y > screen_hegiht:
            fall_rect_list.remove(rect)   
    
    # 화면 그리기
    screen.fill((255, 255, 255))
    
    # 타이머 텍스트 생성
    timer_text = font.render(f"Time :{elpased_time:.2f} seconds", True, (0, 0, 0))
    
    # 타이머 텍스트 화면에 출력
    screen.blit(timer_text, (10, 10))
    
    # 장애물 그리기
    for rect in fall_rect_list:
        pygame.draw.rect(screen, (0, 0 ,255), rect)

    # 플레이어 객체 그리기
    pygame.draw.rect(screen,(255, 0, 0), a_rect)
    
    # 충도 감지
    qu_rect = a_rect.collidelist(fall_rect_list)
    if qu_rect != -1:
        print("장애물 충돌! 게임 종료")
        running = False
    
    if elpased_time > 30:
        print("승리! 게임종료")
        running = False
    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    
    print(len(fall_rect_list))
pygame.quit()



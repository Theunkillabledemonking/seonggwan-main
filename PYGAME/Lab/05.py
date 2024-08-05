
import pygame

pygame.init() # 파이게임 초기화

screen = pygame.display.set_mode((800, 600)) # 화면 사이즈

# << -- fps 적용을 위한 시간 객체 생
clock = pygame.time.Clock()
## ->>
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
light_blue = (173, 216, 230)
green = (0, 255, 0)
yellow = (255, 255, 0)

# 이미지 로드
blue_image = pygame.image.load(".\\blue_rect.png")
red_image = pygame.image.load(".\\red_rect.png")

# 이미지 초기 위치 설정
blue_rect = blue_image.get_rect()
blue_rect.topleft = (100, 100)

red_rect = red_image.get_rect()
red_rect.topleft = (200, 200)

# 이동 속도 설정
speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # 이벤트가 발생할 때 실행된다.
    
    clock.tick(60)
    # 이벤트 처리가 끝난 후 실행
    screen.fill((white))
    
    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        blue_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        blue_rect.x += speed
    if keys[pygame.K_UP]:
        blue_rect.y -= speed
    if keys[pygame.K_DOWN]:
        blue_rect.y += speed
    if keys[pygame.K_a]:
        red_rect.x -= speed
    if keys[pygame.K_d]:
        red_rect.x += speed
    if keys[pygame.K_w]:
        red_rect.y -= speed
    if keys[pygame.K_s]:
        red_rect.y += speed
    
    # 이미지 그리기
    screen.blit(blue_image, blue_rect)
    screen.blit(red_image, red_rect)

    pygame.display.flip()
    # pygame fps 설정

    
pygame.quit()
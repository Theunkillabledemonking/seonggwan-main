import pygame

# pygame 초기화
pygame.init()

# 배경음악 파일 로드 (background.mp3 파일을 로드)
background_music = pygame.mixer.music.load("background.mp3")

# 배경음악 무한 반복 재생 시작(-1은 무한 반복을 의미)
pygame.mixer.music.play(-1)

# 게임 화면 설정 (640 x 480 픽셀 크기의 화면 생성)
screen = pygame.display.set_mode((640, 480))
running = True # 게임루프 제어를 위한 변수 설정

# 게임 루프 시작
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # 종료 이벤트 발생 시 게임 루프 종료
        elif event.type == pygame.KEYDOWN:
            # "s" 키를 누르면 배경음악 정지
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
                print("음악 정지")
            # "p" 키를 누르면 배경음악 재생 (이전에 정지된 경우 처음부터 재생)
            elif event.key == pygame.K_p:
                pygame.mixer.music.play()
                print("음악 재생")
            # "i" 키를 누르면 페이드인(fade-in) 효과로 배경음악 재생 (3초 동안 서서히 볼륨 증가)
            elif event.key == pygame.K_i:
                pygame.mixer.music.play(fade_ms=3000)
                print("음악 재생 - fade-in mode")
            # "o" 키를 누르면 페이드아웃(fade-out) 효과로 배경음악 정지 (3초 동아 서서히 볼륨 감소)
            elif event.key == pygame.K_o:
                pygame.mixer.music.fadeout(3000)
                print("음악 종료 - fade-out made")
            # "u" 키를 누르면 현재 볼륨을 0.1 만큼 증가
            elif event.key == pygame.K_u:
                current_vol = pygame.mixer.music.get_volume() # 현재 볼륨 가져오기 (0.0에서 1.0 사이)
                current_vol += 1 # 볼륨을 0.1 만큼 증가
                pygame.mixer.music.set_volume(current_vol)
            # 'd' 키를 누르면 현재 볼륨을 0.1만큼 감소 (최소 볼륨은 0.0)
            elif event.key == pygame.K_d:
                current_vol = pygame.mixer.music.get_volume() # 현재 볼륨 가져오기
                current_vol = max(0.0, current_vol - 0.1) # 볼륨을 0.1 만큼 감소시키되, 최소 0.0으로 설정
                pygame.mixer.music.set_volume(current_vol)
                print(f"볼륨 감소 : {current_vol}")
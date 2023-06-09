import pygame
##########################################################################
pygame.init()  # 초기화 (반드시)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()
##########################################################################

#1.사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 폰트, 속도 등)

# 이벤트 루프
running = True  # 게임이 진행중 인지
while running:
    dt = clock.tick(30)

    #2. 이벤트 처리 (키보드 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. 게임 캐릭터 위치값 처리

    # 4. 충돌 처리

    # 5. 화면에 그리기

    pygame.display.update()  # 게임화면 다시 그리기

# pygame 종료
pygame.quit()

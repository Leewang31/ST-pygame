import pygame

pygame.init()  #초기화 (반드시)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 이벤트 루프
running = True # 게임이 진행중 인지
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # x버튼을 눌렀을 때
            running = False

# pygame 종료
pygame.quit()
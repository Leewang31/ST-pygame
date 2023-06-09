import pygame

pygame.init()  # 초기화 (반드시)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# 배경이미지 불러오기
background = pygame.image.load("D:/Code/ST-pygame/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("enemy.png")
character_size = character.get_rect().size  # 이미지 크기를 구해옴
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - character_width / 2  # 화면 가로 절반
character_y_pos = screen_height - character_height  # 화면 세로 가장 아래

# 이벤트 루프
running = True  # 게임이 진행중 인지
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # x버튼을 눌렀을 때
            running = False

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()  # 게임화면 다시 그리기

# pygame 종료
pygame.quit()

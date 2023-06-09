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

# 이동할 좌표
to_x = 0
to_y = 0

# 이벤트 루프
running = True  # 게임이 진행중 인지
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # x버튼을 눌렀을 때
            running = False

        if event.type == pygame.KEYDOWN:  # 키가 눌러 졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= 1
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += 1
            elif event.key == pygame.K_UP:  # 캐릭터를 윗쪽으로
                to_y -= 1
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래쪽으로
                to_y += 1

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춘다
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos + character_width > screen_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos + character_height > screen_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()  # 게임화면 다시 그리기

# pygame 종료
pygame.quit()

import pygame

pygame.init()  # 초기화 (반드시)

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")

# FPS
clock = pygame.time.Clock()
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

# 이동 속도
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load("/character.png")
enemy_size = enemy.get_rect().size  # 이미지 크기를 구해옴
enemy_width = enemy_size[0]  # 캐릭터의 가로 크기
enemy_height = enemy_size[1]  # 캐릭터의 세로 크기
enemy_x_pos = screen_width / 2 - enemy_width / 2  # 화면 가로 절반
enemy_y_pos = screen_height / 2 - enemy_height / 2  # 화면 세로 가장 아래

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (폰트,크기)

# 시작 시간
total_time = 10

# 시간 계산
start_ticks = pygame.time.get_ticks()  # 시작 tick을 가져옴

# 이벤트 루프
running = True  # 게임이 진행중 인지
while running:
    dt = clock.tick(60)  # 게임 화면의 초당 프레임 수를 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # x버튼을 눌렀을 때
            running = False

        if event.type == pygame.KEYDOWN:  # 키가 눌러 졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:  # 캐릭터를 윗쪽으로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터를 아래쪽으로
                to_y += character_speed

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춘다
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 캐릭터 화면 안에만 존재하게
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos + character_width > screen_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos + character_height > screen_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 층돌 체크
    if character_rect.colliderect(enemy_rect):
        print('출동했어요 !!!')
        running = False

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 색상
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print('타임아웃')
        running = False

    pygame.display.update()  # 게임화면 다시 그리기

# 잠시 대기
pygame.time.delay(2000)

# pygame 종료
pygame.quit()


import pygame
import random
import math

pygame.init()

blanco = (255, 255, 255)
amarillo = (255, 255, 102)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Snake Cexar")

head_img = pygame.image.load("assets/head.png").convert_alpha()
head_img = pygame.transform.scale(head_img, (40, 40))

head_mouth_open_img = pygame.image.load("assets/head_mouth_open.png").convert_alpha()
head_mouth_open_img = pygame.transform.scale(head_mouth_open_img, (40, 40))

body_img = pygame.image.load("assets/body.png").convert_alpha()
body_img = pygame.transform.scale(body_img, (40, 40))

curve_ur = pygame.image.load("assets/curve_ur.png").convert_alpha()
curve_ur = pygame.transform.scale(curve_ur, (40, 40))

curve_ul = pygame.image.load("assets/curve_ul.png").convert_alpha()
curve_ul = pygame.transform.scale(curve_ul, (40, 40))

curve_dr = pygame.image.load("assets/curve_dr.png").convert_alpha()
curve_dr = pygame.transform.scale(curve_dr, (40, 40))

curve_dl = pygame.image.load("assets/curve_dl.png").convert_alpha()
curve_dl = pygame.transform.scale(curve_dl, (40, 40))

tail_img = pygame.image.load("assets/tail.png").convert_alpha()
tail_img = pygame.transform.scale(tail_img, (40, 40))

apple_img = pygame.image.load("assets/apple.png").convert_alpha()
apple_img = pygame.transform.scale(apple_img, (40, 40))

python_img = pygame.image.load("assets/python.png").convert_alpha()
python_img = pygame.transform.scale(python_img, (40, 40))

body_food_img = pygame.image.load("assets/body_food.png").convert_alpha()
body_food_img = pygame.transform.scale(body_food_img, (40, 40))

fondo_img = pygame.image.load("assets/fondo.png").convert_alpha()
fondo_img = pygame.transform.scale(fondo_img, (width, height))

block_size = 20
snake_speed = 6

font = pygame.font.SysFont("comicsansms", 25)
big_font = pygame.font.SysFont("comicsansms", 70)

def draw_snake(snake_pos, snake_direction, last_food_coord, food_position):
    for i in range(1, len(snake_pos) - 1):
        prev = snake_pos[i - 1]
        curr = snake_pos[i]
        next_ = snake_pos[i + 1]

        dir1 = (curr[0] - prev[0], curr[1] - prev[1])
        dir2 = (next_[0] - curr[0], next_[1] - curr[1])

        if dir1 != dir2:
            if dir1 == (0, -block_size) and dir2 == (block_size, 0) or dir2 == (0, block_size) and dir1 == (-block_size, 0):
                img = curve_dr
            elif dir1 == (0, -block_size) and dir2 == (-block_size, 0) or dir2 == (0, block_size) and dir1 == (block_size, 0):
                img = curve_dl
            elif dir1 == (0, block_size) and dir2 == (-block_size, 0) or dir2 == (0, -block_size) and dir1 == (block_size, 0):
                img = curve_ul
            elif dir1 == (0, block_size) and dir2 == (block_size, 0) or dir2 == (0, -block_size) and dir1 == (-block_size, 0):
                img = curve_ur
            else:
                img = body_img
        else:
            angle = math.degrees(math.atan2(-dir2[1], dir2[0])) + 90
            if curr in last_food_coord:
                img = pygame.transform.rotate(body_food_img, angle)
            else:
                img = pygame.transform.rotate(body_img, angle)

        rect = img.get_rect(center=curr)
        screen.blit(img, rect)

    if len(snake_pos) >= 2:
        tail_dir = (snake_pos[0][0] - snake_pos[1][0], snake_pos[0][1] - snake_pos[1][1])
        tail_angle = math.degrees(math.atan2(-tail_dir[1], tail_dir[0])) + 90
        rotated_tail = pygame.transform.rotate(tail_img, tail_angle)
        tail_rect = rotated_tail.get_rect(center=snake_pos[0])
        screen.blit(rotated_tail, tail_rect)

    head = snake_pos[-1]
    if tuple(head) == food_position: 
        head_final_img = head_mouth_open_img
    else:
        head_final_img = head_img
    angle = math.degrees(math.atan2(-snake_direction[1], snake_direction[0])) + 90
    rotated_head = pygame.transform.rotate(head_final_img, angle)
    head_rect = rotated_head.get_rect(center=head)
    screen.blit(rotated_head, head_rect.topleft)

def show_score(score):
    value = font.render(f"Score: {score}", True, negro)
    screen.blit(value, [0, 0])

def game_loop():
    last_food_coord = []
    game_over = False
    game_close = False
    snake_direction = [1, 0]

    x = width // 2
    y = height // 2
    dx = 0
    dy = 0

    snake_list = []
    snake_length = 1
    score = 0

    def random_position():
        return round(random.randrange(0, width - block_size) / block_size) * block_size, \
               round(random.randrange(0, height - block_size) / block_size) * block_size

    food_x, food_y = random_position()
    is_special = random.choice([False, False, False, True])

    clock = pygame.time.Clock()

    while not game_over:

        screen.blit(fondo_img, (0, 0))


        while game_close:
            screen.fill(negro) # Fondo

            # --- MENSAJE DE GAME OVER (Letras Grandes) ---
            game_over_msg = big_font.render("GAME OVER", True, rojo)
            game_over_rect = game_over_msg.get_rect(center=(width / 2, height / 3))
            screen.blit(game_over_msg, game_over_rect)

            
            instructions_msg = font.render("Presiona Q para SALIR o C para CONTINUAR", True, blanco)
            instructions_rect = instructions_msg.get_rect(center=(width / 2, height / 3 + 100))
            screen.blit(instructions_msg, instructions_rect)

            show_score(score) 
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_direction = [-1, 0]
                    dx = -block_size
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    snake_direction = [1, 0]
                    dx = block_size
                    dy = 0
                elif event.key == pygame.K_UP:
                    snake_direction = [0, -1]
                    dy = -block_size
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    snake_direction = [0, 1]
                    dy = block_size
                    dx = 0

        x += dx
        y += dy

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        if is_special:
            screen.blit(python_img, python_img.get_rect(center=(food_x, food_y)).topleft)
        else:
            screen.blit(apple_img, apple_img.get_rect(center=(food_x, food_y)).topleft)

        head = [x, y]
        snake_list.append(head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == head:
                game_close = True

        draw_snake(snake_list, snake_direction, last_food_coord, (food_x, food_y))
        show_score(score)
        pygame.display.update()

        if x == food_x and y == food_y:
            if is_special:
                score += 5
                snake_length += 5
                for i in range(5):
                    if len(snake_list) >= i + 1:
                        last_food_coord.append(snake_list[-(i + 1)])
            else:
                score += 1
                snake_length += 1
                last_food_coord.append(snake_list[-1]) 

            food_x, food_y = random_position()
            is_special = random.choice([False, False, False, False, False, True])

        last_food_coord = [coord for coord in last_food_coord if coord in snake_list]
        clock.tick(snake_speed)

    pygame.quit()
    quit()

def intro_screen():
    intro = True
    while intro:
        screen.fill(negro)
        text = font.render("LA SERPIENTE MORIBUNDA", True, rojo)
        screen.blit(text, [width/2 - text.get_width()/2, height/2 - 50])

        press_text = font.render("Presione C para continuar", True, blanco)
        screen.blit(press_text, [width/2 - press_text.get_width()/2, height/2 + 10])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False


def menu_inicio():
    menu = True
    while menu:
        screen.fill(azul)
        msg = font.render("Presiona C para iniciar su partida crick", True, blanco)
        screen.blit(msg, [width/2 - msg.get_width()/2, height/2 - 10])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    menu = False


intro_screen()
menu_inicio()
game_loop()

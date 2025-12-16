
import pygame
import random
import math

# Inicializo la librería Pygame para empezar a usar sus funciones.
pygame.init()

# 1. CONFIGURACIÓN DE COLORES Y PANTALLA
# Yo defino los colores que voy a usar en el juego.
blanco = (255, 255, 255)
amarillo = (255, 255, 102)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Yo configuro el tamaño de mi ventana de juego.
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Cexar")

# 2. CARGA DE ASSETS (IMÁGENES)
# Yo cargo y escalo todas las imágenes que uso para el renderizado detallado.
# Esto mejora la Experiencia de Usuario frente a usar solo colores.

# Imágenes de la cabeza, cuerpo y cola
head_img = pygame.image.load("assets/head.png").convert_alpha()
head_img = pygame.transform.scale(head_img, (40, 40))

head_mouth_open_img = pygame.image.load("assets/head_mouth_open.png").convert_alpha()
head_mouth_open_img = pygame.transform.scale(head_mouth_open_img, (40, 40))

body_img = pygame.image.load("assets/body.png").convert_alpha()
body_img = pygame.transform.scale(body_img, (40, 40))

# Imágenes de las curvas para una renderización suave
curve_ur = pygame.image.load("assets/curve_ur.png").convert_alpha()
curve_ur = pygame.transform.scale(curve_ur, (40, 40))
# y así con el resto de las curvas (ul, dr, dl)
curve_ul = pygame.image.load("assets/curve_ul.png").convert_alpha()
curve_ul = pygame.transform.scale(curve_ul, (40, 40))

curve_dr = pygame.image.load("assets/curve_dr.png").convert_alpha()
curve_dr = pygame.transform.scale(curve_dr, (40, 40))

curve_dl = pygame.image.load("assets/curve_dl.png").convert_alpha()
curve_dl = pygame.transform.scale(curve_dl, (40, 40))

tail_img = pygame.image.load("assets/tail.png").convert_alpha()
tail_img = pygame.transform.scale(tail_img, (40, 40))

# Imágenes de la comida
apple_img = pygame.image.load("assets/apple.png").convert_alpha()
apple_img = pygame.transform.scale(apple_img, (40, 40))

python_img = pygame.image.load("assets/python.png").convert_alpha()
python_img = pygame.transform.scale(python_img, (40, 40))

# Imagen para el cuerpo que ha comido (barriga llena)
body_food_img = pygame.image.load("assets/body_food.png").convert_alpha()
body_food_img = pygame.transform.scale(body_food_img, (40, 40))

# Imagen de fondo y configuración de parámetros de juego
fondo_img = pygame.image.load("assets/fondo.png").convert_alpha()
fondo_img = pygame.transform.scale(fondo_img, (width, height))

block_size = 20 # Tamaño de la cuadrícula
snake_speed = 6 # Velocidad base del juego

# Configuración de fuentes de texto
font = pygame.font.SysFont("comicsansms", 25)
big_font = pygame.font.SysFont("comicsansms", 70) # Fuente para el título 'GAME OVER'

# 3. FUNCIONES DE DIBUJO Y RENDERIZADO
# Mi función para dibujar la serpiente, usando curvas, cabeza y cola.
def draw_snake(snake_pos, snake_direction, last_food_coord, food_position):

    # Bucle 'For' para dibujar el cuerpo (excluyendo cabeza y cola, que se dibujan aparte).
    for i in range(1, len(snake_pos) - 1): 
        prev = snake_pos[i - 1] # Coordenada anterior
        curr = snake_pos[i] # Coordenada actual (segmento que dibujó)
        next_ = snake_pos[i + 1] # Coordenada siguiente

# Yo calculo la dirección de entrada (dir1) y salida (dir2) para saber si hay curva.
        dir1 = (curr[0] - prev[0], curr[1] - prev[1])
        dir2 = (next_[0] - curr[0], next_[1] - curr[1])

# Condicionales para renderizar curvas o segmentos rectos:
        if dir1 != dir2:
# Si las direcciones son diferentes, es una curva. Uso Condicionales extensos (if/elif) 
# Para decidir cuál de las 4 imágenes de curva debo usar.
            if dir1 == (0, -block_size) and dir2 == (block_size, 0) or dir2 == (0, block_size) and dir1 == (-block_size, 0):
                img = curve_dr
            elif dir1 == (0, -block_size) and dir2 == (-block_size, 0) or dir2 == (0, block_size) and dir1 == (block_size, 0):
                img = curve_dl
# (continúa con las otras dos curvas)
            elif dir1 == (0, block_size) and dir2 == (-block_size, 0) or dir2 == (0, -block_size) and dir1 == (block_size, 0):
                img = curve_ul
            elif dir1 == (0, block_size) and dir2 == (block_size, 0) or dir2 == (0, -block_size) and dir1 == (-block_size, 0):
                img = curve_ur
            else:
                img = body_img # Si por alguna razón no detecta curva, dibuja cuerpo normal
        else:
 # Si dir1 == dir2, el segmento es recto.
            angle = math.degrees(math.atan2(-dir2[1], dir2[0])) + 90
# Condicional para dibujar la barriga llena (si ese segmento acaba de comer comida especial)
            if curr in last_food_coord:
                img = pygame.transform.rotate(body_food_img, angle)
            else:
                img = pygame.transform.rotate(body_img, angle)

        rect = img.get_rect(center=curr)
        screen.blit(img, rect)
# Lógica para dibujar la COLA (snake_pos[0])
    if len(snake_pos) >= 2:
# Calculo la dirección de la cola para saber cómo rotar la imagen.
        tail_dir = (snake_pos[0][0] - snake_pos[1][0], snake_pos[0][1] - snake_pos[1][1])
        tail_angle = math.degrees(math.atan2(-tail_dir[1], tail_dir[0])) + 90
        rotated_tail = pygame.transform.rotate(tail_img, tail_angle)
        tail_rect = rotated_tail.get_rect(center=snake_pos[0])
        screen.blit(rotated_tail, tail_rect)

# Lógica para dibujar la CABEZA (snake_pos[-1])
    head = snake_pos[-1]
# Condicional para abrir la boca si la cabeza está sobre la comida.
    if tuple(head) == food_position: 
        head_final_img = head_mouth_open_img
    else:
        head_final_img = head_img
# Roto la cabeza basándome en la dirección de la serpiente.
    angle = math.degrees(math.atan2(-snake_direction[1], snake_direction[0])) + 90
    rotated_head = pygame.transform.rotate(head_final_img, angle)
    head_rect = rotated_head.get_rect(center=head)
    screen.blit(rotated_head, head_rect.topleft)

# Función simple para dibujar la puntuación.
def show_score(score):
    value = font.render(f"Score: {score}", True, negro)
    screen.blit(value, [0, 0])

# 4. EL BUCLE PRINCIPAL DEL JUEGO (GAME LOOP) 
# Mi función principal, el corazón del programa.
def game_loop():
    # Variables de estado iniciales.
    last_food_coord = [] # Lista para manejar el dibujo de la barriga llena.
    game_over = False
    game_close = False # Indica el estado 'Game Over' (pero el bucle sigue activo).
    snake_direction = [1, 0] # Dirección inicial (derecha)

# Posición inicial de la serpiente (centro) y cambio (dx, dy).
    x = width // 2
    y = height // 2
    dx = 0
    dy = 0

# Estructura de Datos clave.
    snake_list = []
    snake_length = 1
    score = 0

# Función para generar la posición aleatoria de la comida.
    def random_position():
        # Yo redondeo al múltiplo de block_size para asegurar que la comida caiga en la cuadrícula.
        return round(random.randrange(0, width - block_size) / block_size) * block_size, \
               round(random.randrange(0, height - block_size) / block_size) * block_size

    food_x, food_y = random_position()
    is_special = random.choice([False, False, False, True]) # Lógica para comida especial.

    clock = pygame.time.Clock() # Objeto para controlar el tiempo y la velocidad.

# Bucle 'While' principal: Mantiene el juego activo.
    while not game_over:

        screen.blit(fondo_img, (0, 0))

# Bucle 'While': Se activa cuando el juego termina (game_close = True).
# Este bucle pausa la lógica del juego y solo maneja el menú de Game Over.
        while game_close:
        
         while game_close:
            screen.fill(negro) # Fondo negro o el color que quieras

            # MENSAJE DE GAME OVER grande
            game_over_msg = big_font.render("GAME OVER", True, rojo)
            # Centrar el texto en la pantalla (verticalmente en height/3)
            game_over_rect = game_over_msg.get_rect(center=(width / 2, height / 3))
            screen.blit(game_over_msg, game_over_rect)

            # INSTRUCCIONES
            instructions_msg = font.render("Presiona Q para SALIR o C para CONTINUAR", True, blanco)
            # Posicionar las instrucciones debajo del título
            instructions_rect = instructions_msg.get_rect(center=(width / 2, height / 3 + 100))
            screen.blit(instructions_msg, instructions_rect)

            show_score(score) 
            pygame.display.update()

# Bucle 'For' para manejar eventos de tecla en el menú de Game Over.
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:

# Condicionales para decidir qué hacer al presionar 'Q' o 'C'.
                    if event.key == pygame.K_q:
                        game_over = True # Sale del bucle principal
                        game_close = False # Sale de este bucle anidado
                    if event.key == pygame.K_c:
                        game_loop() # Modularidad: Yo reinicio el juego llamando a la función principal de nuevo.
        
# Bucle 'For' principal: Procesa la entrada del usuario (movimiento).
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:

# Condicionales (if/elif) para determinar la dirección de la serpiente.
# Yo actualizo tanto snake_direction (para dibujar la cabeza) como dx/dy (para moverla).
                if event.key == pygame.K_LEFT:
                    snake_direction = [-1, 0]
                    dx = -block_size
                    dy = 0
# y así sucesivamente para RIGHT, UP y DOWN.                    
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

# Lógica de Movimiento: Yo actualizo las coordenadas de la cabeza.
        x += dx
        y += dy

# Condicional para la Colisión con el Borde.
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

# Renderizado de la Comida (Manzana o Especial)
# Condicional para dibujar el asset correspondiente (python_img si es especial).
        if is_special:
            screen.blit(python_img, python_img.get_rect(center=(food_x, food_y)).topleft)
        else:
            screen.blit(apple_img, apple_img.get_rect(center=(food_x, food_y)).topleft)

# Lógica de la Lista (Estructura de Datos) para el movimiento:
        head = [x, y]
        snake_list.append(head) # 1. Añade la nueva cabeza.
        if len(snake_list) > snake_length:
            del snake_list[0] # 2. Elimina la cola (simula el movimiento).

# Bucle 'For' para Colisión con el Propio Cuerpo.
# Yo itero sobre el cuerpo (excluyendo la cabeza) para ver si la cabeza chocó consigo misma.
        for segment in snake_list[:-1]:
            if segment == head:
                game_close = True

# Dibujo final de los elementos en pantalla.
        draw_snake(snake_list, snake_direction, last_food_coord, (food_x, food_y))
        show_score(score)
        pygame.display.update()

# Lógica de Crecimiento (Condicional de Colisión con Comida)
        if x == food_x and y == food_y:

# Condicional anidado para la Comida Especial.
            if is_special:
                score += 5
                snake_length += 5 # Crezco 5 bloques
            
# Lógica para marcar los 5 segmentos que acaban de crecer (para el asset de barriga).
                for i in range(5):
                    if len(snake_list) >= i + 1:
                        last_food_coord.append(snake_list[-(i + 1)])
            else:
                score += 1
                snake_length += 1 # Crezco 1 bloque
                last_food_coord.append(snake_list[-1]) # Marco el último segmento que creció.

            food_x, food_y = random_position() # Llamo a mi función para generar nueva comida.
            # Lógica para que la comida especial aparezca con baja probabilidad.
            is_special = random.choice([False, False, False, False, False, True])

# Comprensión de Listas: Yo limpio las coordenadas de barriga que ya no están en la serpiente.
        last_food_coord = [coord for coord in last_food_coord if coord in snake_list]
       # Control de Velocidad (Rendimiento): Limito los FPS al valor de snake_speed.
        clock.tick(snake_speed)

# Finalización del Juego (cuando game_over es True).
    pygame.quit()
    quit()

# 5. MENU INICIAL.
# Función para la pantalla de inicio (muestra el título del creador).
def intro_screen():
    intro = True
    while intro:
        # Bucle 'While' para manejar la interfaz del menú de inicio.
        screen.fill(negro)
        text = font.render("Snake por Cexar", True, verde)
        # Yo centro el texto en la pantalla.
        screen.blit(text, [width/2 - text.get_width()/2, height/2 - 50])

        press_text = font.render("Presione C para continuar", True, blanco)
        screen.blit(press_text, [width/2 - press_text.get_width()/2, height/2 + 10])

        pygame.display.update()

# Bucle 'For' para manejar la entrada del usuario en el menú.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:

                # Condicional: Si presiono 'C', salgo del bucle de intro.
                if event.key == pygame.K_c:
                    intro = False

# Función para el menú previo al inicio del juego.
def menu_inicio():
    menu = True
    while menu:
        screen.fill(azul)
        msg = font.render("Presione C para iniciar su partida", True, blanco)
        screen.blit(msg, [width/2 - msg.get_width()/2, height/2 - 10])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:

                # Condicional: Si presiono 'C', salgo del bucle de menú.
                if event.key == pygame.K_c:
                    menu = False

# Llamada inicial de las funciones para arrancar el juego.
intro_screen()
menu_inicio()
game_loop()
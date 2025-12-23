Hola gente, este es un proyecto del juego de la Serpiente, hecho en Python usando la libreria de Pygame.
El objetivo principal del desarrollo fue crear un sistema visualmente detallado.

1. El codigo usa un sistema de estados que controla las diferentes pantallas:

Pantalla de Introducción: Muestra el título

Menú Principal: Da inicio al juego

Estado de Juego: Donde ocurre la jugabilidad principal

Pantalla de Game Over: Muestra resultados y opciones

2. RENDERIZADO DINÁMICO DE LA SERPIENTE

La función central draw_snake maneja toda la complejidad visual:

Detección de Curvas: El código determina automáticamente si la serpiente está girando 90 grados y utiliza las imágenes de curvas predefinidas (curve_ur, curve_dl, etc.), 
en lugar de segmentos rectos, para garantizar una transición suave en las esquinas.

<img width="539" height="218" alt="image" src="https://github.com/user-attachments/assets/324c6ee6-c35b-4aa4-95ee-42c3408eb1f8" />

Rotación de Segmentos: Los segmentos rectos del cuerpo y la cola se rotan mediante pygame.transform.rotate para alinearse 
con precisión en las direcciones horizontal o vertical.

<img width="325" height="14" alt="image" src="https://github.com/user-attachments/assets/02bc4294-6be4-4655-b074-677ae1370873" />

Animación de Comida: La cabeza de la serpiente cambia a la imagen de "boca abierta" 
(head_mouth_open_img) exactamente cuando colisiona con la comida, ofreciendo una respuesta visual inmediata al jugador.

<img width="535" height="22" alt="image" src="https://github.com/user-attachments/assets/b1a25f53-6327-40ab-8a8d-80fa4e1e68a1" />

.

3. ELEMENTO DE JUGABILIDAD

Detección de Curvas: Análisis vectorial entre segmentos.

Path Smoothing: Uso de sprites de curva para transiciones.

Collision: Optimización mediante alineación.

4. Alimentos:

El juego incluye dos tipos de alimento:

Manzana Estándar: Incrementa la longitud en 1 segmento y otorga 1 punto.

<img width="68" height="61" alt="image" src="https://github.com/user-attachments/assets/0764dbb5-5c6a-4d5e-8350-6ab2489d17ca" />

Comida Especial (Ícono de Python): 

<img width="44" height="63" alt="image" src="https://github.com/user-attachments/assets/9834fa5c-746a-4c5e-84ce-fa5a7c1eded2" />

Aparece con baja probabilidad. Al consumirla, la serpiente crece 5 segmentos y el jugador obtiene 5 puntos,
introduciendo un riesgo/recompensa.

.

5. REQUISITOS Y EJECUCIÓN:
Para poder correr este juego, se requiere lo siguiente:

Python 3

La librería Pygame instalada (use pip install pygame).

La carpeta assets/ debe contener todas las imágenes requeridas (cuerpo, curvas, cabeza, cola, alimentos y fondo).

<img width="306" height="286" alt="image" src="https://github.com/user-attachments/assets/68ec77cf-7872-4306-aadd-0a29b230dde6" />

CONTROLES:
El juego se controla usando las teclas de flecha (Arriba, Abajo, Izquierda, Derecha).

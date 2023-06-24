import pygame
import turtle


# Configuración del tablero
ANCHO = 480
ALTO = 480
TAM_CASILLA = 60
FILAS = 8
COLUMNAS = 8

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Inicializar Pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))

# Dibujar casillas del tablero
for fila in range(FILAS):
    for columna in range(COLUMNAS):
        x = columna * TAM_CASILLA
        y = fila * TAM_CASILLA
        color = BLANCO if (fila + columna) % 2 == 0 else NEGRO
        pygame.draw.rect(ventana, color, (x, y, TAM_CASILLA, TAM_CASILLA))

# Actualizar pantalla
pygame.display.update()

# Esperar hasta que el usuario cierre la ventana
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()



wn = turtle.Screen()
wn.title("Wumpus")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"



def mov():
    if cabeza.direction =="up":
        y = cabeza.ycor()
        cabeza.sety(y + 20 )

    if cabeza.direction =="down":
        y = cabeza.ycor()
        cabeza.sety(y - 20 )

    if cabeza.direction =="right":
        x = cabeza.xcor()
        cabeza.setx(x + 20 )

    if cabeza.direction =="left":
        x = cabeza.xcor()
        cabeza.setx(x - 20 )




while True:
    wn.update()
    mov()

    time.sleep(posponer)


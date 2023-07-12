import pygame
from classNivelUno import *
ANCHO = 1600#X
ALTO = 900#y
FPS = 80
DERECHA  = 1
IZQUIERDA = 0
direccion = DERECHA
screen_size =(ANCHO,ALTO)

PANTALLA = pygame.display.set_mode(screen_size)
pygame.display.set_caption("JUEGO")
pygame.init()

nivel_actual = NivelUno(PANTALLA)
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    #print(len(lista_enemigos))
    lista_eventos = pygame.event.get()
    pantalla_lvl_1(PANTALLA,screen_size)
    nivel_actual.update(lista_eventos)
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update() 

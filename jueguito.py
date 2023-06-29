import pygame
import sys
from frutas import *
VERDE  = (153,255,51)
CELESTE = (153,204,255)
COLOR = (250,250,250)
BLACK = (0,0,0)
ANCHO = 1200#X
ALTO = 770#y
FPS = 60
DERECHA  = 1
IZQUIERDA = 0
direccion = DERECHA
pygame.init()
screen_size =(ANCHO,ALTO)


PANTALLA = pygame.display.set_mode(screen_size)
pygame.display.set_caption("RUSTIC PACMAN")
#ICONO
#icono = pygame.image.load("PYGAME\pygame intro\subirarchivos\Recursos\pacmanicono.png")
#FONDO
fondo = pygame.image.load("PROGRA 1\PYGAME\pygame intro\subirarchivos\Recursos\pacmanfondo.jpg")
fondo = pygame.transform.scale(fondo, screen_size)

lista_fruta = crear_lista_fruta(50)

imagen_pacman = pygame.image.load("PROGRA 1\PYGAME\pygame intro\subirarchivos\Recursos\pngwing.com.png")
imagen_pacman = pygame.transform.scale(imagen_pacman, (200,250))
imagen_pacman = pygame.transform.rotate(imagen_pacman, 90)
imagen_pacman_izquierda = pygame.transform.flip(imagen_pacman,True,False)
imagen_pacman_derecha = imagen_pacman
rectangulo =  imagen_pacman.get_rect()
rectangulo.x = 400
rectangulo.y = 570
rectangulo.width = 200
rectangulo.height = 200
personaje = {'superficioe':imagen_pacman,'rectangulo': '', 'score' : 0}
fuente = pygame.font.SysFont('Arial',30)
texto = fuente.render('SCORE: ',False,VERDE)

clock = pygame.time.Clock()
while True:
    clock.tick(FPS)
    texto = fuente.render(f"SCORE: {personaje['score']} ",False,BLACK,CELESTE)
    PANTALLA.blit(texto,(0,0))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        imagen_pacman = imagen_pacman_derecha
        direccion = DERECHA
        nueva_x = rectangulo.x + 10
        if nueva_x < ANCHO - rectangulo.width:
            rectangulo.x += 10
    if key[pygame.K_LEFT]:
        direccion = IZQUIERDA
        imagen_pacman = imagen_pacman_izquierda
        nueva_x = rectangulo.x - 10
        if nueva_x > 0:
            rectangulo.x -= 10
    for dona in lista_fruta:
        PANTALLA.blit(dona['superficie'], dona['rectangulo'])
    PANTALLA.blit(fondo,(0,0))
    PANTALLA.blit(imagen_pacman,rectangulo)
    
    

    pygame.display.flip() 


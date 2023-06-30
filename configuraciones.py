import pygame
import sys
from animacion_personaje import *
from funciones import *
from classPersonaje import *
from modo import * 
from fondos import *
from pisos import *
from classEnemigo import Enemigos
from classObjeto import Objeto_game
from hud import crear_hud
from classTrampa import Trampa
VERDE  = (153,255,51)
CELESTE = (153,204,255)
COLOR = (250,250,250)
BLACK = (0,0,0)
ANCHO = 1600#X
ALTO = 900#y
FPS = 80
DERECHA  = 1
IZQUIERDA = 0
direccion = DERECHA
screen_size =(ANCHO,ALTO)

PANTALLA = pygame.display.set_mode(screen_size)
pygame.display.set_caption("JUEGO")
fondo = crear_fondo("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/fondo_completo.jpg",screen_size)

reescalar_imagenes(lista_animaciones_personaje,170/2,250/2)
reescalar_imagenes(lista_animaciones_enemigo_1,170/1.6, 250/1.6)
reescalar_imagenes(lista_trampas,50,50)


personaje1= Personaje(600,665,PANTALLA)

#PISO
plataforma = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/plataforma_chica.png",(400,75),1200,500,20)
plataforma_arriba = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/plataforma_chica.png",(400,75),600,200,20)
plataforma_izquierda = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/plataforma_chica.png",(400,75),0,500,20)
piso = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/plataforma_grande.png",(ANCHO,200),0,personaje1.rect.bottom,25)
piso.top = personaje1.rect.bottom
lista_plataformas = [piso,plataforma,plataforma_izquierda,plataforma_arriba]
#piso = pygame.Rect(0,personaje1.rect.bottom,ANCHO,200)#COORDENADAS left,top DONDE EMPIEZA, ANCHO Y ALTO
#ENEMIGOS
enemigo_1 = Enemigos(0,665,70)
enemigo_2 = Enemigos(0,plataforma_izquierda.rect.top - 130,70)
enemigo_3 = Enemigos(plataforma.rect.x,665,70)
###OBJETOS
carne = Objeto_game(plataforma_arriba.rect.centerx,plataforma_arriba.rect.top - 25)
carne2 = Objeto_game(plataforma.rect.centerx,plataforma.rect.top - 25)
lista_enemigos = [enemigo_1,enemigo_2,enemigo_3]
lista_objetos = [carne,carne2]
###TRAMPAS

trampa_1 = Trampa(plataforma_arriba.rect.left,plataforma_arriba.rect.top - 20,50,50)
trampa_2 = Trampa(trampa_1.rect.right,trampa_1.rect.y,70,70)
lista_trampas = [trampa_1,trampa_2]

def dibujar_hitbox():
    pygame.draw.rect(PANTALLA, CELESTE, personaje1.rect ,2 )
    pygame.draw.rect(PANTALLA, CELESTE, piso ,2 )
    pygame.draw.rect(PANTALLA, CELESTE,plataforma,2)
    pygame.draw.rect(PANTALLA, CELESTE,plataforma_izquierda,2)
    pygame.draw.rect(PANTALLA, CELESTE,plataforma_arriba,2)
    pygame.draw.rect(PANTALLA, CELESTE,enemigo_1.rect,2)
    pygame.draw.rect(PANTALLA, CELESTE,enemigo_2.rect,2)
    pygame.draw.rect(PANTALLA,CELESTE,carne.rect,2)

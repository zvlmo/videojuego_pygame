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
fondo = crear_fondo("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/FONDONIVEL2.png",screen_size)

reescalar_imagenes(lista_animaciones_personaje,170/2,250/2)
reescalar_imagenes(lista_animaciones_enemigo_volador,170/1.3, 250/2)
reescalar_imagenes(lista_animaciones_trampas,50,50)


personaje1= Personaje(1000,665,170/2,250/2,PANTALLA)

#PISO
plataforma = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/2.png",(400,75),1000,840,10)
plataforma_2 = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/2.png",(400,75),300,840,10)
plataforma_izquierda = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/3.png",(400,75),0,500,20)
plataforma_derecha = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/3.png",(400,75),1200,500,20)
plataforma_arriba = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/4.png",(200,75),700,200,20)
plataforma_arriba_2 = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/4.png",(200,75),700,400,20)

lista_plataformas = [plataforma,plataforma_2,plataforma_izquierda,plataforma_arriba,plataforma_derecha,plataforma_arriba,plataforma_arriba_2]
#piso = pygame.Rect(0,personaje1.rect.bottom,ANCHO,200)#COORDENADAS left,top DONDE EMPIEZA, ANCHO Y ALTO
#ENEMIGOS
enemigo_1 = Enemigos(0,500,70,170/1.6, 250/2)
enemigo_2 = Enemigos(0,500,70,170/1.6, 250/2)
enemigo_3 = Enemigos(plataforma.rect.x,500,70,170/1.6, 250/2)
###OBJETOS
carne = Objeto_game(plataforma_izquierda.rect.centerx - 15,plataforma_izquierda.rect.top - 35,"C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/Ribs.png")
carne2 = Objeto_game(plataforma_derecha.rect.centerx,plataforma_derecha.rect.top - 35,"C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/Ribs.png")
carne3 = Objeto_game(plataforma_arriba.rect.centerx,plataforma_arriba.rect.top - 35,"C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/Ribs.png")
sombrero = Objeto_game(500,350,"C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/sombrero.png")
sombrero2 = Objeto_game(1000,350,"C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/sombrero.png")

lista_enemigos = [enemigo_1,enemigo_2,enemigo_3]
lista_carnes = [carne,carne2,carne3,sombrero,sombrero2]
lista_sombreros = [sombrero,sombrero2]
###TRAMPAS

trampa_1 = Trampa(plataforma_izquierda.rect.right - 100,plataforma_izquierda.rect.top - 30,50,50)
trampa_2 = Trampa(trampa_1.rect.right,trampa_1.rect.y,70,70)
lista_trampas = [trampa_1,trampa_2]
lista_boss = []
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/SONIDOS/musicanivel2.mp3")
pygame.mixer.music.set_volume(0.2)

pygame.mixer.music.play(-1)

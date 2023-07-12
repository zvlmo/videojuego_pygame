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
from classBoss import Boss
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
fondo = crear_fondo("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/Enjl-Dream Ship Tileset/preview.png",screen_size)

reescalar_imagenes(lista_animaciones_personaje,170/2,250/2)
reescalar_imagenes(lista_animaciones_trampas,50,50)
reescalar_imagenes(lista_animaciones_boss,150,200)
reescalar_imagenes(lista_animaciones_enemigo_ultimo,170/1.3, 250/2)


#PISO
plataforma = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/ultimo nivel/1.png",(400,75),1200,840,10)
plataforma_2 = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/ultimo nivel/1.png",(400,75),0,840,10)
plataforma_medio_chica = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/ultimo nivel/0.png",(150,75),700,800,10)
plataforma_izquierda = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/ultimo nivel/2.png",(400,75),0,400,20)
plataforma_derecha = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/ultimo nivel/2.png",(400,75),1200,500,20)
plataforma_arriba = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/ultimo nivel/0.png",(400,75),700,300,20)

lista_plataformas = [plataforma,plataforma_2,plataforma_medio_chica,plataforma_izquierda,plataforma_arriba,plataforma_derecha,plataforma_arriba]
#plataforma = pygame.Rect(0,personaje1.rect.bottom,ANCHO,200)#COORDENADAS left,top DONDE EMPIEZA, ANCHO Y ALTO
personaje1= Personaje(plataforma_arriba.rect.x,plataforma_arriba.rect.y - 10,170/2,250/2,PANTALLA)
#ENEMIGOS
enemigo_2 = Enemigos(plataforma_izquierda.rect.x,plataforma_izquierda.rect.top - 100,70,170/1.5, 250/2)
enemigo_3 = Enemigos(plataforma_derecha.rect.x,400,70,170/1.5, 250/2)
enemigo_4 = Enemigos(plataforma_2.rect.x,plataforma_2.rect.top - 100,70,170/1.5, 250/2)
boss = Boss(plataforma.rect.x,plataforma.rect.y - 170,150,150,200,PANTALLA)
lista_boss = [boss]
###OBJETOS
carne = Objeto_game(plataforma_izquierda.rect.centerx - 25,plataforma_izquierda.rect.top - 35,"C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/Ribs.png")
carne2 = Objeto_game(plataforma_derecha.rect.centerx,plataforma_derecha.rect.top - 35,"C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/Ribs.png")
carne4 = Objeto_game(plataforma_2.rect.centerx -70 ,plataforma.rect.top - 35,"C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/Ribs.png")
carne5 = Objeto_game(plataforma_arriba.rect.centerx ,plataforma_arriba.rect.top - 35,"C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/Ribs.png")


sombrero = Objeto_game(plataforma_2.rect.centerx,plataforma_2.rect.top - 25,"C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/sombrero.png")
sombrero2 = Objeto_game(400,350,"C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/sombrero.png")
sombrero3 = Objeto_game(plataforma_medio_chica.rect.x,plataforma_medio_chica.rect.top - 200,"C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/sombrero.png")

lista_enemigos = [enemigo_2,enemigo_3,enemigo_4]
lista_carnes = [carne,carne2,carne4,carne5]
lista_sombreros = [sombrero,sombrero2,sombrero3]
###TRAMPAS

trampa_1 = Trampa(plataforma_arriba.rect.centerx - 400 ,850,50,50)
#trampa_2 = Trampa(plataforma_arriba.rect.centerx + 200 ,850,50,50)
lista_trampas = [trampa_1]
if personaje1.rect.top >= 900:
    personaje1.hp = 0
pygame.mixer.init()
pygame.mixer.music.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/SONIDOS/musicanivel3.mp3")
pygame.mixer.music.set_volume(0.2)

pygame.mixer.music.play(-1)

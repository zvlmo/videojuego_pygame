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
from classNivel import Nivel

class NivelUno(Nivel):
    def __init__(self, pantalla):
        
        
        fondo = crear_fondo("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/fondo_completo.jpg", (1600,900))
        reescalar_imagenes(lista_animaciones_personaje, 170/2, 250/2)
        reescalar_imagenes(lista_animaciones_enemigo_1, 170/1.3, 250/1.6)
        reescalar_imagenes(lista_animaciones_trampas, 50, 50)

        personaje1 = Personaje(600, 665, 170/2, 250/2, pantalla)

        plataforma = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/plataforma_chica.png", (400, 75), 1200, 500, 20)
        plataforma_arriba = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/plataforma_chica.png", (400, 75), 600, 200, 20)
        plataforma_izquierda = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/plataforma_chica.png", (400, 75), 0, 500, 20)
        piso = Plataformas("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/plataforma_grande.png", (1600, 200), 0, personaje1.rect.bottom-35, 65)
        piso.top = personaje1.rect.bottom
        lista_plataformas = [piso, plataforma, plataforma_izquierda, plataforma_arriba]

        enemigo_1 = Enemigos(0, 665, 70, 170/1.3, 250/1.6)
        enemigo_2 = Enemigos(0, plataforma_izquierda.rect.top - 130, 70, 170/1.3, 250/1.6)
        enemigo_3 = Enemigos(plataforma.rect.x, 665, 70, 170/1.3, 250/1.6)
        lista_enemigos = [enemigo_1, enemigo_2, enemigo_3]

        carne = Objeto_game(plataforma_arriba.rect.centerx, plataforma_arriba.rect.top - 25, "C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/Ribs.png")
        carne2 = Objeto_game(plataforma.rect.centerx, plataforma.rect.top - 25, "C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/Ribs.png")
        lista_carnes = [carne, carne2]

        trampa_1 = Trampa(plataforma_arriba.rect.left, plataforma_arriba.rect.top - 20, 50, 50)
        trampa_2 = Trampa(trampa_1.rect.right, trampa_1.rect.y, 70, 70)
        lista_trampas = [trampa_1, trampa_2]
        lista_sombreros = []
        lista_boss = []

        super().__init__(pantalla, personaje1, lista_plataformas, lista_enemigos, lista_carnes, lista_sombreros, lista_trampas, lista_boss, fondo)

    def update(self, lista_eventos):
        super().update(lista_eventos)
        # Agrega aquí la lógica específica del nivel uno si es necesario

    def dibujar_hitbox(self):
        super().dibujar_hitbox()
        # Agrega aquí la lógica específica del nivel uno si es necesario

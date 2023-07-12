import pygame
from funciones import *
from animacion_personaje import *
from modo import *
class Proyectil():
    def __init__(self,x,y,direc,surface,lista_proyectil):
        self.objeto = 'proyectil'
        self.imagen = lista_proyectil[0][0]
        self.rect = self.imagen.get_rect()
        self.rect.center = (x,y)
        self.velocidad = 9
        self.direc = direc
        self.pantalla = surface
        self.flag_proyectil = False
        self.animaciones= lista_proyectil
        self.pasos = 0
        self.dmg = 15
        self.hacer_dmg_enemigo= pygame.mixer.Sound("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/SONIDOS/recibedmgenemigo.wav")


    def animar_proyectil(self,lista_proyectil):
        largo  = len(lista_proyectil)
        if self.pasos >= largo:
            self.pasos = 0
        self.pantalla.blit(lista_proyectil[self.pasos],self.rect)
        self.pasos += 1
        
    def update(self,target,proyectil_derecha,proyectil_izquierda):
        if self.direc:
            self.rect.x -= self.velocidad
            self.animar_proyectil(proyectil_derecha)
        else:
            self.rect.x += self.velocidad
            self.animar_proyectil(proyectil_izquierda)
        if self.rect.colliderect(target.rect):
            if self.flag_proyectil == False:
                self.hacer_dmg_enemigo.play()
                target.hp -= 15
                if target.hp <= 0:
                    target.esta_vivo = False
                print(target.hp)
                self.flag_proyectil = True

        if get_mode():
            pygame.draw.rect(self.pantalla,'blue',self.rect,2)
            
    
        
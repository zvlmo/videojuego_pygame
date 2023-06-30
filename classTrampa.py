import pygame
from animacion_personaje import *
import random
class Trampa():
    def __init__(self,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.velocidad = random.randint(2,4)
        self.imagen= animaciones_trampa_1[0]
        self.flag = False
        
    def animar_personaje(self,acciones_peronaje):
        largo  = len(acciones_peronaje)
        if self.pasos >= largo:
            self.pasos = 0
        self.imagen = (acciones_peronaje[self.pasos])
        self.pasos += 1
        
    def realizar_dmg(self,target):
        if self.rect.colliderect(target.rect):
            if self.flag == False:
                target.hp -= 5
                target.que_hace = 'recibe_dmg'
                self.flag = True
                print(target.hp)
        else:
            self.flag = False
    def update_pantalla(self,animacion):
        self.animar_personaje(animacion)
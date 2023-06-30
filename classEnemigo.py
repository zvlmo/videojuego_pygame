import pygame
import random
from animacion_personaje import *

class Enemigos:
    def __init__(self,x,y,hp):
        # Inicializar Pygame y crear la ventana

        # Crear un rectángulo inicial
        self.hp = hp
        #self.imagen = pygame.image.load("")
        self.rect = pygame.Rect(x,y, 170/1.6, 250/1.6)

        # Configurar la velocidad y la dirección inicial del movimiento
        self.velocidad = random.randint(3,6)
        self.direccion_x = 1
        self.direccion_y = 1
        self.imagen = lista_animaciones_enemigo_1[0][0]
        self.pasos = 0
        self.delay = 0
        self.esta_vivo = True
        self.flag = False
        
    def blit(self,screen):
        screen.blit(self.imagen,self.rect)
        
    def animar_personaje(self,acciones_peronaje):
        largo  = len(acciones_peronaje)
        if self.pasos >= largo:
            self.pasos = 0
        self.imagen = (acciones_peronaje[self.pasos])
        self.pasos += 1

    def movimiento_enemigo(self,right_range,left_range):


        # Actualizar la posición del rectángulo
        self.rect.x += self.velocidad * self.direccion_x

        # Cambiar de dirección si el rectángulo llega a los límites de la pantalla
        if self.rect.right >= right_range:
            self.direccion_x = -1
        elif self.rect.left <= left_range:
            self.direccion_x = 1
    def realizar_dmg(self,target):
        if self.rect.colliderect(target.rect):
            if self.flag == False:
                target.hp -= 10
                self.flag = True
                print(target.hp)
        else:
            self.flag = False
        
    def update_pantalla(self,camina, camina_izquierda):
        self.tiempo_transcurrido = self.delay 
        self.delay += 1
        if self.tiempo_transcurrido >= 3:
            self.delay = 0
            if self.direccion_x == 1:
                self.animar_personaje(camina)
            else:
                self.animar_personaje(camina_izquierda)
            # if self.direccion_y == 1:
            #     self.animar_personaje()
            # else:
            #     self.animar_personaje()
    def muere_enemigo(self):
        if self.hp <= 0:
            self.esta_vivo = False
    def movimiento_enemigo_volador(self,right_range,left_range,top_range,bottom_range):


        # Actualizar la posición del rectángulo
        self.rect.x += self.velocidad * self.direccion_x
        self.rect.y += self.velocidad * self.direccion_y
        # Cambiar de dirección si el rectángulo llega a los límites de la pantalla
        if self.rect.right >= right_range:
            self.direccion_x = -1
        elif self.rect.left <= left_range:
            self.direccion_x = 1
        if self.rect.top >= top_range:
            self.direccion_y = -1
        elif self.rect.bottom <= bottom_range:
            self.direccion_y = 1
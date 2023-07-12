import pygame
import random
from animacion_personaje import *
from classProyectil import Proyectil
class Boss:
    def __init__(self,x,y,hp,ancho,alto,pantalla):
        pygame.mixer.init()
        self.hp = hp
        self.rect = pygame.Rect(x,y,ancho,alto)
        self.velocidad = random.randint(3,6)
        self.direccion_x = 1
        self.direccion_y = 1
        self.imagen = lista_animaciones_boss[0][0]
        self.pasos = 0
        self.delay = 0
        self.esta_vivo = True
        self.flag = False
        self.hacer_dmg= pygame.mixer.Sound("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/SONIDOS/recibedmg.wav")
        self.que_hace = 'nada'
        self.disparo = False
        self.direc = 1
        self.proyectiles = []
        self.pantalla= pantalla
        self.recibe_dmg = False
        self.direccion = 1
        self.flag_attack = False
        self.disparar = pygame.mixer.Sound("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/SONIDOS/BOSSDISPARA.wav")
        self.recibe_dolor = pygame.mixer.Sound("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/SONIDOS/recibe_dmg_boss.wav")
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
            
            
    def realizar_dmg(self,target,pantalla):
        if self.rect.colliderect(target.rect):
            if self.flag == False:
                target.hp -= 10
                self.flag = True
                print(target.hp)
                self.hacer_dmg.play()

        else:
            self.flag = False
            
        try:
            if self.disparo == False:
                if self.flag_attack:
                    if self.direccion_x == 1:
                        self.disparo_enemigo(target,pantalla)
                        self.que_hace = 'dispara_izquierda'
                        self.disparo = True    
                else:
                    self.flag_attack = False
                    self.disparo = False
        except Exception as e:
            print('Error')
            print(e)
        if self.hp <= 0:
            self.esta_vivo = False
            
    def update_pantalla(self,camina, camina_izquierda,dispara_derecha,dispara_izquierda,recibe_dmg_boss,recibe_dmg_boss_izquierda,target):
        for proyectil in self.proyectiles:
            proyectil.update(target,animacion_proyectil_enemigo,animacion_proyectil_enemigo)
        self.recibe_dmg_boss(target)
        self.disparo_si_colisiona(target.proyectiles,target)
        self.tiempo_transcurrido = self.delay 
        self.delay += 1
        if self.tiempo_transcurrido >= 3:
            self.delay = 0
            match self.que_hace:
                case 'nada':
                    if self.direccion_x == 1:
                        self.animar_personaje(camina)
                    else:
                        self.animar_personaje(camina_izquierda)
                case'dispara_izquierda':
                    self.animar_personaje(dispara_izquierda)
                    self.que_hace = 'nada'
                case'recibe_dmg_boss':
                    self.animar_personaje(recibe_dmg_boss)
                    self.que_hace = 'nada'
                    
    def muere_enemigo(self):
        if self.hp <= 0:
            self.esta_vivo = False
    
    def disparo_enemigo(self,target):
        if self.esta_vivo == True:
            proyectil = Proyectil(self.rect.x,self.rect.y + 70, self.direccion_x ,self.pantalla,lista_animacion_proyectil_boss)
            if self.disparo == False:
                if self.direccion_x:
                    proyectil.rect.x += self.rect.width
                    self.que_hace = 'dispara_izquierda'
                else:
                    proyectil.rect.x += proyectil.rect.width
                if proyectil.rect.colliderect(target.rect):
                    print("hit proyectil enemigo")
                    self.disparo = True
                self.proyectiles.append(proyectil)
            else:
                self.disparo = False
        else:
            self.esta_vivo = False
        
            
    def recibe_dmg_boss(self, personaje):
        for shoot in personaje.proyectiles:
            if  self.recibe_dmg == False:
                if self.rect.colliderect(shoot.rect):
                    self.hp -= 15
                    self.recibe_dolor.play()
                    print(self.hp)
                    self.recibe_dmg = True
                else:
                    self.recibe_dmg = False
        
        if self.hp <= 0:
            self.esta_vivo = False
                    
    def disparo_si_colisiona(self, proyectiles_personaje,target):
        for proyectil in proyectiles_personaje:
            if self.rect.colliderect(proyectil.rect):
                self.que_hace = 'recibe_dmg_boss'
                self.disparo_enemigo(target)
                self.disparar.play()
                proyectiles_personaje.remove(proyectil)
                self.hp -= 15
                print(self.hp)
            
                
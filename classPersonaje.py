from funciones import *
import pygame
from animacion_personaje import *
from modo import *
from classProyectil import Proyectil
class Personaje ():
    def __init__(self,x,y,pantalla):
        
        self.rect = pygame.Rect((x,y,170/2,250/2))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_tipe = 0
        self.hp = 50
        self.pasos = 0
        self.que_hace = 'quieto'
        self.direccion = 'izquierda'
        self.tiempo_transcurrido = 0
        self.direc = False
        self.delay = 0
        self.lados = obtener_rectangulos(self.rect)
        self.imagen = lista_animaciones_personaje[0][0]
        self.pantalla = pantalla
        self.flag = False
        self.disparos = 5
        self.proyectiles = []
        self.puntos = 0
        self.esta_vivo = True
    def animar_personaje(self,acciones_peronaje,pantalla):
        largo  = len(acciones_peronaje)
        if self.pasos >= largo:
            self.pasos = 0
        self.imagen = (acciones_peronaje[self.pasos])
        self.pasos += 1
                
    def blit(self,screen):
        screen.blit(self.imagen,self.rect)
        
    def aplicar_gravedad(self,lista_plataforma):
        for piso in lista_plataforma:
            if self.rect.colliderect(piso):
                self.rect.bottom = piso.get_top()
                self.vel_y = 0
                self.jump = False
            
            # if self.rect.top.colliderect(piso):
            #     self.rect.y = piso.rect.top
            else:
                pass
    def movimiento(self, ancho,alto,surface,lista_enemigo,lista_plataforma):
            contador_pasos = 0
            posicion_actual_x = 0
            VELOCIDAD = 10
            GRAVEDAD = 2
            coord_x = 0
            coord_y  = 0
            #presionar teclas
            key = pygame.key.get_pressed()
            #SOLO PUEDE HACER UNA ACCION Y NO ATACAR
            #movimiento
            if self.esta_vivo ==True:
                if self.attacking == False:
                    if self.jump == False:
                        self.que_hace = "quieto"
                    else:
                        self.que_hace = "salta"
                        
                    if key[pygame.K_a]:
                        coord_x = -VELOCIDAD
                        self.direccion = 'izquierda'
                        self.direc = True
                        if self.jump == False:
                            self.que_hace = "izquierda"
                        
                    elif key[pygame.K_d]:
                        self.direccion = 'derecha'
                        coord_x = VELOCIDAD
                        self.direc = False
                        if self.jump == False:
                            self.que_hace = "derecha"
                        
                                                        
                    if key[pygame.K_w] and self.jump  == False:
                        self.vel_y = -30
                        self.jump = True
                        self.que_hace = "salta"
                    for plataforma in lista_plataforma:
                        if self.rect.colliderect(plataforma.rect):
                            if key[pygame.K_s]:
                                    self.rect.y += plataforma.rect.height

                    if self.disparos > 0:
                        if key[pygame.K_e]:
                            print("dispara")
                            self.attacking = True
                            self.que_hace= 'ataque_range'
                    else:
                        print("No hay balas")
                    #ATAQUES
                    if key[pygame.K_r] :
                        self.attack_mele(lista_enemigo,surface)
                        self.que_hace= 'ataca'
                        self.attacking = True
                        
                else:
                    self.attacking = False
                self.vel_y += GRAVEDAD
                coord_y += self.vel_y

                if self.rect.left + coord_x < 10:
                    coord_x = 0 
                    
                if self.rect.right + coord_x > ancho:
                    coord_x = coord_x - 10
                for enemigo in lista_enemigo:
                    if enemigo.rect.colliderect(self.rect):
                        self.que_hace = 'recibe_dmg'
            self.aplicar_gravedad(lista_plataforma)
            
            #ACTUALIZAMOS POSICIONES DE JUGADOR
            self.rect.x += coord_x
            self.rect.y +=coord_y
    

            

    def muere_personaje(self,tiempo):
        if self.hp <= 0 or tiempo == 0:
            self.esta_vivo = False
            self.que_hace = 'muere'
                
    def update_pantalla(self,pantalla,lista_enemigos,correr,saltar,quieto,atacar_mele, correr_izquierda,saltar_izquierda,mirar_izquierda,atacar_izquierda,recibe_dmg,recibe_dmg_izquierda,dispara,dispara_izquierda,muere,muere_derecha):
        for proyectil in self.proyectiles:
            for enemigo in lista_enemigos:
                proyectil.update(enemigo)
        self.tiempo_transcurrido = self.delay 
        self.delay += 1
        if self.tiempo_transcurrido >= 3:
            self.delay = 0
            
            match self.que_hace:
                case 'izquierda':
                    self.animar_personaje(correr_izquierda,pantalla)
                case 'derecha':
                    self.animar_personaje(correr,pantalla)
                case 'salta':
                    if self.direccion == 'izquierda':
                        self.animar_personaje(saltar_izquierda,pantalla)
                    else:
                        self.animar_personaje(saltar,pantalla)
                case 'quieto':
                    if self.direccion == 'izquierda':
                        self.animar_personaje(mirar_izquierda,pantalla)
                    else:
                        self.animar_personaje(quieto,pantalla)
                case 'ataca':
                    if self.direccion == 'izquierda':
                        self.animar_personaje(atacar_izquierda,pantalla)
                    else:
                        self.animar_personaje(atacar_mele,pantalla)
                case 'ataque_range':
                    if self.disparos > 0:
                        if self.direccion == 'izquierda':
                            self.animar_personaje(dispara_izquierda,pantalla)
                        else:
                            self.animar_personaje(dispara,pantalla)
                case 'recibe_dmg':
                    if self.direccion == 'izquierda':
                        self.animar_personaje(recibe_dmg_izquierda,pantalla)
                    else:
                        self.animar_personaje(recibe_dmg,pantalla)
                case 'muere':
                        self.animar_personaje(muere,pantalla)
                    
    def attack_mele(self,lista,surface):
        #pygame.draw.rect(surface,(153,204,255), self.attack)
        for target in lista:
            if self.flag == False:
                if self.direccion == 'izquierda':
                    attack = pygame.Rect(self.rect.x , self.rect.y, self.rect.width - 20, self.rect.height )
                else:
                    attack = pygame.Rect(self.rect.x * -1, self.rect.y, self.rect.width+20, self.rect.height )
                if attack.colliderect(target.rect):
                    target.hp -= 10
                    if target.hp <= 0:
                        target.esta_vivo = False
                    self.flag = True
                    print(target.hp)
                    print("Hit")
            else:
                self.flag = False
        
            
    def attack_range(self,target):
        proyectil = Proyectil(self.rect.x,self.rect.y + 20, self.direc,self.pantalla,lista_animacion_proyectil)
        if self.direc:
            proyectil.rect.x += self.rect.width
        else:
            proyectil.rect.x += proyectil.rect.width
        self.proyectiles.append(proyectil)
        for enemigo in target:
            if proyectil.rect.colliderect(enemigo.rect):
                self.puntos+= 5
                print("hit proyectil")


import pygame
import sys
from animacion_personaje import *
from hud import crear_hud
from modo import *
class Nivel:
    def __init__(self,pantalla,personaje,lista_plataformas,lista_enemigos,lista_carnes, lista_sombreros,lista_trampas,lista_boss,fondo):
        self._slave = pantalla
        self.jugador = personaje
        self.plataformas = lista_plataformas
        self.img_fondo = fondo
        self.enemigos = lista_enemigos
        self.objetos = lista_carnes
        self.sombreros = lista_sombreros
        self.trampas = lista_trampas
        self.boss = lista_boss
        
    def update(self,lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
                if self.jugador.disparos > 0:
                    if evento.key == pygame.K_e:
                        self.jugador.disparos -= 1
                        self.jugador.attack_range(self.enemigos)
        self.actualizar_pantalla(enemigo1_caminar,enemigo1_caminar_izquierda,personaje_correr,personaje_saltando,personaje_quieto,personaje_ataque_mele,personaje_correr_derecha,personaje_salta_derecha,personaje_mira_derecha,personaje_ataca_derecha,personaje_golpeado,personaje_golpeado_izquierda,personaje_dispara,personaje_dispara_izquierda,personaje_muere,personaje_muere_derecha,animaciones_caminando_boss,animaciones_caminar_boss_izquierda,animaciones_disparando_boss,animaciones_disparando_boss_izquierda,recibe_dmg_boss,recibe_dmg_boss_izquierda)

        if get_mode() == True:
            self.dibujar_hitbox()
        
        
        
    def actualizar_pantalla(self, enemigo_camina, enemigo_camina_izquierda,personaje_correr, personaje_saltando, personaje_quieto, personaje_ataque_mele, personaje_correr_derecha, personaje_salta_derecha, personaje_mira_derecha, personaje_ataca_derecha, personaje_golpeado, personaje_golpeado_izquierda, dispara, dispara_izquierda, personaje_morir, personaje_morir_derecha,animaciones_caminando_boss,animaciones_caminar_boss_izquierda,animaciones_disparando_boss,animaciones_disparando_boss_izquierda,recibe_dmg_boss,recibe_dmg_boss_izquierda):
        for plataforma in self.plataformas:
            self._slave.blit(plataforma.imagen,plataforma.rect)
        for objeto in self.objetos:
            self._slave.blit(objeto.imagen,objeto.rect)
            if self.jugador.rect.colliderect(objeto):
                self.objetos.remove(objeto)
        for enemigo in self.enemigos:
            if enemigo.esta_vivo == True:
                enemigo.blit(self._slave)
                enemigo.update_pantalla(enemigo_camina,enemigo_camina_izquierda)
            else:
                self.jugador.puntos += 50
                self.enemigos.remove(enemigo)
                
        for sombrero in self.sombreros:
            self._slave.blit(sombrero.imagen, sombrero.rect)
            # sombrero.animar_objeto(animacion_sombrero)
            if self.jugador.rect.colliderect(sombrero):
                self.sombreros.remove(sombrero)
        for boss in self.boss:
            boss.blit(self._slave)
            boss.update_pantalla(animaciones_caminando_boss,animaciones_caminar_boss_izquierda,animaciones_disparando_boss,animaciones_disparando_boss_izquierda,self.jugador)

        self.jugador.blit(self._slave)
        self.jugador.update_pantalla(self._slave,personaje_correr,personaje_saltando,personaje_quieto,personaje_ataque_mele,personaje_correr_derecha,personaje_salta_derecha,personaje_mira_derecha,personaje_ataca_derecha,personaje_golpeado,personaje_golpeado_izquierda,dispara,dispara_izquierda,personaje_morir,personaje_morir_derecha,self.boss)
        for trampa in self.trampas:
            self._slave.blit(trampa.imagen,trampa.rect)
    
    def dibujar_hitbox(self):
            pygame.draw.rect(self._slave, 'green', self.jugador.rect ,2 )
            for plataforma in self.plataformas:
                pygame.draw.rect(self._slave, 'green', plataforma ,2 )
            for enemigo in self.enemigos:
                pygame.draw.rect(self._slave, 'green',enemigo.rect,2)
            for objeto in self.objetos:
                pygame.draw.rect(self._slave,'green',objeto.rect,2)
            for trampa in self.trampas:
                pygame.draw.rect(self._slave,'green',trampa.rect,2)
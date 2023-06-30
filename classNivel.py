import pygame,sys
from configuraciones import*
class Nivel:
    def __init__(self,pantalla,personaje,lista_plataformas,lista_enemigos,lista_objetos,fondo):
        self._slave = pantalla
        self.jugador = personaje
        self.plataformas = lista_plataformas
        self.img_fondo = fondo
        self.enemigos = lista_enemigos
        self.objetos = lista_objetos
        
    def update(self,lista_eventos):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
                if self.jugador.disparos > 0:
                    if evento.key == pygame.K_e:
                        self.jugador.disparos -= 1
                        self.jugador.attack_range(self.enemigos)
        self.leer_imputs()
    def actualizar_pantalla(self,lista_trampas,enemigo_camina,enemigo_camina_izquierda,lista_plataformas,personaje,personaje_correr,personaje_saltando,personaje_quieto,personaje_ataque_mele,personaje_correr_derecha,personaje_salta_derecha,personaje_mira_derecha,personaje_ataca_derecha,personaje_golpeado,personaje_golpeado_izquierda,dispara,dispara_izquierda,personaje_morir,personaje_morir_derecha):
        bandera = False
        self._slave.blit(fondo,(0,0))
        self._slave.blit(lista_plataformas[0].imagen,(0,750))
        self._slave.blit(lista_plataformas[1].imagen,(1200,500))
        self._slave.blit(lista_plataformas[2].imagen,(600,200))
        self._slave.blit(lista_plataformas[3].imagen,(0,500))
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
                    

        self.jugador.blit(self._slave)
        self.jugador.update_pantalla(self._slave,self.enemigos,personaje_correr,personaje_saltando,personaje_quieto,personaje_ataque_mele,personaje_correr_derecha,personaje_salta_derecha,personaje_mira_derecha,personaje_ataca_derecha,personaje_golpeado,personaje_golpeado_izquierda,dispara,dispara_izquierda,personaje_morir,personaje_morir_derecha)
        for trampa in lista_trampas:
            self._slave.blit(trampa.imagen,trampa.rect)
    def leer_imputs(self):
        pass
        
import pygame
from animacion_personaje import *
def actualizar_pantalla(pantalla,fondo,lista_objetos,lista_enemigos,enemigo_camina,enemigo_camina_izquierda,lista_plataformas,personaje,personaje_correr,personaje_saltando,personaje_quieto,personaje_ataque_mele,personaje_correr_derecha,personaje_salta_derecha,personaje_mira_derecha,personaje_ataca_derecha,personaje_golpeado,personaje_golpeado_izquierda,dispara,dispara_izquierda):
    bandera = False
    pantalla.blit(fondo,(0,0))
    pantalla.blit(lista_plataformas[0].imagen,(0,750))
    pantalla.blit(lista_plataformas[1].imagen,(1200,500))
    pantalla.blit(lista_plataformas[2].imagen,(600,200))
    pantalla.blit(lista_plataformas[3].imagen,(0,500))
    for objeto in lista_objetos:
        pantalla.blit(objeto.imagen,objeto.rect)
        if personaje.rect.colliderect(objeto):
            lista_objetos.remove(objeto)
    for enemigo in range(len(lista_enemigos)):
        if lista_enemigos[enemigo].esta_vivo == True:
            lista_enemigos[enemigo].blit(pantalla)
            lista_enemigos[enemigo].update_pantalla(enemigo_camina,enemigo_camina_izquierda)
        else:
            lista_enemigos.remove(lista_enemigos[enemigo])
                #lista_enemigos[enemigo].rect.x = -2000
                

    if personaje.hp > 0:
        personaje.blit(pantalla)
        personaje.update_pantalla(pantalla,lista_enemigos,personaje_correr,personaje_saltando,personaje_quieto,personaje_ataque_mele,personaje_correr_derecha,personaje_salta_derecha,personaje_mira_derecha,personaje_ataca_derecha,personaje_golpeado,personaje_golpeado_izquierda,dispara,dispara_izquierda)

def obtener_rectangulos(principal)->dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom -10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
    return diccionario

    #IF INVEL ACTUAL ES IGUAL A UNO, CUANDO SE CUMPLAN TODAS LAS CONDICIONES CAMBIAS EL VALOR DE NIVEL ACTUAL, UNA VEZ COMPLETADO EL NIVEL 3, AGREGAR QUE SE PUEDA ELEGIR EL VALOR DE NIVEL ACTUAL
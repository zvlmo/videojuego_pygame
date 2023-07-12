import pygame
from animacion_personaje import *


def actualizar_pantalla(pantalla, fondo, lista_trampas, lista_sombreros, lista_carnes, lista_enemigos, lista_jefe, enemigo_camina, enemigo_camina_izquierda, lista_plataformas, personaje, personaje_correr, personaje_saltando, personaje_quieto, personaje_ataque_mele, personaje_correr_derecha, personaje_salta_derecha, personaje_mira_derecha, personaje_ataca_derecha, personaje_golpeado, personaje_golpeado_izquierda, dispara, dispara_izquierda, personaje_morir, personaje_morir_derecha,animaciones_caminando_boss,animaciones_caminar_boss_izquierda,animaciones_disparando_boss,animaciones_disparando_boss_izquierda,recibe_dmg_boss,recibe_dmg_boss_izquierda):
    bandera = False
    pantalla.blit(fondo, (0, 0))
    for plataforma in lista_plataformas:
        pantalla.blit(plataforma.imagen, plataforma.rect)
    for objeto in lista_carnes:
        pantalla.blit(objeto.imagen, objeto.rect)
        if personaje.rect.colliderect(objeto):
            lista_carnes.remove(objeto)
    for sombrero in lista_sombreros:
        pantalla.blit(sombrero.imagen, sombrero.rect)
        # sombrero.animar_objeto(animacion_sombrero)
        if personaje.rect.colliderect(sombrero):
            lista_sombreros.remove(sombrero)
    for trampa in lista_trampas:
        pantalla.blit(trampa.imagen, trampa.rect)
    for enemigo in lista_enemigos:
        if enemigo.esta_vivo == True:
            enemigo.blit(pantalla)
            enemigo.update_pantalla(enemigo_camina, enemigo_camina_izquierda)
        else:
            personaje.puntos += 50
            lista_enemigos.remove(enemigo)
    for jefe in lista_jefe:
        if jefe.esta_vivo == True:
            jefe.blit(pantalla)
            jefe.update_pantalla(animaciones_caminando_boss,animaciones_caminar_boss_izquierda,animaciones_disparando_boss,animaciones_disparando_boss_izquierda,recibe_dmg_boss,recibe_dmg_boss_izquierda,personaje)
        else:
            personaje.puntos += 200
            lista_jefe.remove(jefe)
            
            
    personaje.update_pantalla(pantalla, lista_enemigos, personaje_correr, personaje_saltando, personaje_quieto, personaje_ataque_mele, personaje_correr_derecha, personaje_salta_derecha,
                            personaje_mira_derecha, personaje_ataca_derecha, personaje_golpeado, personaje_golpeado_izquierda, dispara, dispara_izquierda, personaje_morir, personaje_morir_derecha,lista_jefe)
    personaje.blit(pantalla)


def dibujar_hitbox(pantalla, personaje, lista_plataformas, lista_enemigos, lista_carnes, lista_sombreros,lista_trampas):
    pygame.draw.rect(pantalla, 'green', personaje.rect, 2)
    for plataforma in lista_plataformas:
        pygame.draw.rect(pantalla, 'green', plataforma, 2)
    for enemigo in lista_enemigos:
        pygame.draw.rect(pantalla, 'green', enemigo.rect, 2)
    for objetos in lista_carnes:
        pygame.draw.rect(pantalla, 'green', objetos.rect, 2)
    for objetos in lista_sombreros:
        pygame.draw.rect(pantalla, 'green', objetos.rect, 2)
    for trampas in lista_trampas:
        pygame.draw.rect(pantalla, 'green', trampas.rect, 2)

def obtener_rectangulos(principal) -> dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(
        principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["right"] = pygame.Rect(
        principal.right - 2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(
        principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(
        principal.left, principal.top, principal.width, 10)
    return diccionario

    # IF INVEL ACTUAL ES IGUAL A UNO, CUANDO SE CUMPLAN TODAS LAS CONDICIONES CAMBIAS EL VALOR DE NIVEL ACTUAL, UNA VEZ COMPLETADO EL NIVEL 3, AGREGAR QUE SE PUEDA ELEGIR EL VALOR DE NIVEL ACTUAL

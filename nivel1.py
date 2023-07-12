from configuraciones import *
def nivel_1():
    bandera =  False
    key = pygame.key.get_pressed()
    
    personaje1.movimiento(ANCHO,ALTO,PANTALLA,lista_enemigos,lista_plataformas,lista_boss)
    enemigo_1.movimiento_enemigo(800,0)
    enemigo_2.movimiento_enemigo(plataforma_izquierda.rect.right,0)
    enemigo_3.movimiento_enemigo(plataforma.rect.right,plataforma.rect.left)
    
    for enemy in lista_enemigos:
        enemy.realizar_dmg(personaje1)
    
    for objeto in lista_carnes:
        objeto.brindar_buff_carne(personaje1)
    for trampa in lista_trampas:
        trampa.realizar_dmg(personaje1)
        
    if len(lista_enemigos) == 0:
        pass


    actualizar_pantalla(PANTALLA,fondo,lista_trampas,lista_sombreros,lista_carnes,lista_enemigos,lista_boss,enemigo1_caminar,enemigo1_caminar_izquierda,lista_plataformas,personaje1,personaje_correr,personaje_saltando,personaje_quieto,personaje_ataque_mele,personaje_correr_derecha,personaje_salta_derecha,personaje_mira_derecha,personaje_ataca_derecha,personaje_golpeado,personaje_golpeado_izquierda,personaje_dispara,personaje_dispara_izquierda,personaje_muere,personaje_muere_derecha,animaciones_caminando_boss,animaciones_caminar_boss_izquierda,animaciones_disparando_boss,animaciones_disparando_boss_izquierda,recibe_dmg_boss,recibe_dmg_boss_izquierda)
    crear_hud(PANTALLA,personaje1.puntos,ANCHO,ALTO,personaje1)
import pygame 

#temporizador
tiempo_actual = 0
temporizador = 60
def crear_hud(pantalla,puntos,ancho,alto,personaje):
    guardar_tiempo = 0
    vidas = ""
    fuente_puntos = pygame.font.Font('C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/retro_computer_personal_use.ttf', 30)
    puntos_surf = fuente_puntos.render(f"SCORE: {puntos}", True, "whitesmoke")
    puntos_rect= puntos_surf.get_rect(topright = (ancho - 20,20))

    tiempo_actual = pygame.time.get_ticks()
    tiempo_restante = temporizador - tiempo_actual//1000
    
    personaje.muere_personaje(tiempo_restante)

    #temporizador
    if tiempo_restante >= 10:
        mensaje_temporizador = f"00:{tiempo_restante}"
    else:
        mensaje_temporizador = f"00:0{tiempo_restante}"
    temporizador_surf = pygame.font.Font('C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/retro_computer_personal_use.ttf', 30)
    temporizador_text = temporizador_surf.render(mensaje_temporizador, False, "whitesmoke")
    temporizador_rect = temporizador_text.get_rect(midtop = (ancho//2, 20))
    
    mensaje_ammo = f'Air shoots : {personaje.disparos}'
    ammo_text = pygame.font.Font("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/retro_computer_personal_use.ttf",20)
    ammo_surf= ammo_text.render(mensaje_ammo,False,"whitesmoke")
    ammo_rect = ammo_surf.get_rect()
    ammo_rect.x = ancho- 250
    ammo_rect.y = alto - 40
    
    vidas = personaje.hp / 10
            
    vidas_surf = pygame.font.Font('C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/retro_computer_personal_use.ttf', 30)
    vidas_text = vidas_surf.render(f"Vidas: {vidas}", False, "whitesmoke")
    vidas_rect = vidas_text.get_rect(topleft = (20, 20))
    
    
    
    pantalla.blit(ammo_surf,ammo_rect)
    pantalla.blit(puntos_surf,puntos_rect)
    pantalla.blit(temporizador_text,temporizador_rect)
    pantalla.blit(vidas_text,vidas_rect)
    
    
    # corazon_3 = pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/FULL.png").convert_alpha()
    # corazon_2 =pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/2.png").convert_alpha()
    # corazon_1=pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/1.png").convert_alpha()
    # corazon_25=pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/2.5.png").convert_alpha()
    # corazon_15=pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/1.5.png").convert_alpha()
    # corazon_0=pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/0.png").convert_alpha()
    # corazon_05=pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/0.5.png").convert_alpha()
    
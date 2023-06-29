import pygame 

#temporizador
tiempo_actual = 0
temporizador = 60
def crear_hud(pantalla,puntos,ancho,personaje):
    fuente_puntos = pygame.font.Font('C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/retro_computer_personal_use.ttf', 15)
    puntos_surf = fuente_puntos.render(f"SCORE: {puntos}", True, "whitesmoke")
    puntos_rect= puntos_surf.get_rect(topright = (ancho - 20,20))
    pygame.draw.rect(pantalla,'blue',puntos_rect,2)

    tiempo_actual = pygame.time.get_ticks()
    tiempo_restante = temporizador - tiempo_actual//1000
    if tiempo_restante <= 0:
        tiempo_restante = 0

    #temporizador
    if tiempo_restante >= 10:
        mensaje_temporizador = f"00:{tiempo_restante}"
    else:
        mensaje_temporizador = f"00:0{tiempo_restante}"
    temporizador_surf = pygame.font.Font('C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/retro_computer_personal_use.ttf', 15)
    temporizador_text = temporizador_surf.render(mensaje_temporizador, False, "whitesmoke")
    temporizador_rect = temporizador_text.get_rect(midtop = (ancho//2, 20))
    pygame.draw.rect(pantalla,'blue',temporizador_rect,2)
    
    pantalla.blit(puntos_surf,puntos_rect)
    pantalla.blit(temporizador_text,temporizador_rect)
    
    # corazon_3 = pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/FULL.png")
    # corazon_2 =pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/2.png")
    # corazon_1=pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/1.png")
    # corazon_25=pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/2.5.png")
    # corazon_15=pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/1.5.png")
    # corazon_0=pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/0.png")
    # corazon_05=pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/corazones/0.5.png")
    # match personaje.hp:
    #     case 30:
    #         pantalla.blit(corazon_3,0,0)
    

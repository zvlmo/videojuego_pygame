#from nivel3 import *
from nivel1 import *
from gui.GUI_form_settings import FormSettings
from SQL import *
from pantallas_carga import *
#from nivel3 import *

pygame.init()
pygame.display.set_caption("JUEGO")
bandera = False
bandera_pantallas =False
form_principal = FormSettings(PANTALLA, ANCHO/2-400, ALTO/2-200, 800,400, "dodgerblue4", "cyan3", 5, True)
clock = pygame.time.Clock()
crear_base()
pausado = False

while True:
    
    clock.tick(FPS)
    #print(len(lista_enemigos))
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:            
            if evento.key == pygame.K_ESCAPE:
                bandera = not bandera
            if evento.key == pygame.K_TAB:#
                cambiar_modo()
            if evento.key == pygame.K_p:  # Tecla 'P' para pausar/reanudar
                pausado = not pausado
            if personaje1.disparos > 0:
                if evento.key == pygame.K_e:
                    personaje1.disparos -= 1
                    print('pium')
                    personaje1.attack_range()
    if not pausado:
        if len(lista_enemigos) == 0 and len(lista_boss) == 0 or personaje1.hp <= 0 :
            editar_score(personaje1.puntos)
        else:
            nivel_1()
    if bandera == True:
        PANTALLA.blit(pygame.transform.scale(pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/BACKGROUND/El-fondo-de-pantalla-de-One-Piece-que-se-merece-tu-PC.jpg"), (ANCHO, ANCHO)), (0,0))
        form_principal.update(lista_eventos)
    

    if get_mode() == True:
        dibujar_hitbox(PANTALLA,personaje1,lista_plataformas,lista_enemigos,lista_carnes,lista_sombreros,lista_trampas)



    pygame.display.flip() 

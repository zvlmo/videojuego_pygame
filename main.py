from nivel1 import *
pygame.init()

clock = pygame.time.Clock()
while True:
    clock.tick(FPS)
    nivel_1()
    #print(len(lista_enemigos))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
            if personaje1.disparos > 0:
                if evento.key == pygame.K_e:
                    personaje1.disparos -= 1
                    personaje1.attack_range(lista_enemigos)
    if get_mode() == True:
        dibujar_hitbox()



    pygame.display.flip() 

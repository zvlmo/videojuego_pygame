import pygame
import sys



personaje_quieto  =     [pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/0.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/0.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/1.png")

                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/1.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/2.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/2.png")

                        ]

personaje_saltando =  [pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/15.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/16.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/17.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/18.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/19.png")

                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/19.png")






                        ]

personaje_correr = [    pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/3.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/4.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/5.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/6.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/7.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/8.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/9.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/10.png")
                    ]

personaje_ataque_mele = [
                        pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/12.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/13.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/13.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/14.png")
                        ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/15.png")
]

personaje_golpeado = [pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/RECIBE DANIO/0,5.png"),
                      pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/RECIBE DANIO/0,5.png"),
                      pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/RECIBE DANIO/1.png"),
                      pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/RECIBE DANIO/1.png"),
                      pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/RECIBE DANIO/1.png"),
                      pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/RECIBE DANIO/2.png"),
                      pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/RECIBE DANIO/2.png"),
                      pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/RECIBE DANIO/2.png"),
                      ]
personaje_dispara = [
                        pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/DISPARA/2.png"),
                        pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/DISPARA/3.png"),
                        
]
personaje_muere = [pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/muere/0.png"),
                    pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/muere/3.png")]
animacion_proyectil = [
                        pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/DISPARA/0.png"),
                        pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/DISPARA/0.png"),
                        pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/DISPARA/0.png"),
                        pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/DISPARA/4.png"),
                        pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/DISPARA/4.png"),
                        pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/LUFFY/DISPARA/4.png"),


]

enemigo1_caminar = [
                    pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/KUMA/0.png")
                    ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/KUMA/1.png")
                    ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/KUMA/2.png")
                    ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/KUMA/3.png")
                    ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/KUMA/4.png")
                    ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/KUMA/5.png")
                    ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/KUMA/6.png")
                    ,pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/KUMA/7.png")]

animaciones_trampa_1 = [
                        pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/TRAPS/trap1/image.png"),
                        pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/TRAPS/trap1/image.png"),
                        pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/TRAPS/trap1/image.png"),
                        pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/TRAPS/trap1/image.png")
]
def girar_imagenes(lista_imagen,flip_x,flip_y):
    lista_girada = []
    for imagen in lista_imagen:
        lista_girada.append(pygame.transform.flip(imagen,flip_x,flip_y))
    return lista_girada

animacion_proyectil_derecha = girar_imagenes(animacion_proyectil,True,False)
enemigo1_caminar_izquierda = girar_imagenes(enemigo1_caminar,True,False)
personaje_correr_derecha = girar_imagenes(personaje_correr,True,False)
personaje_salta_derecha= girar_imagenes(personaje_saltando,True,False)
personaje_mira_derecha = girar_imagenes(personaje_quieto,True,False)
personaje_ataca_derecha = girar_imagenes(personaje_ataque_mele,True,False)
personaje_golpeado_izquierda = girar_imagenes(personaje_golpeado,True,False)
personaje_dispara_izquierda = girar_imagenes(personaje_dispara,True,False)
personaje_muere_derecha = girar_imagenes(personaje_muere,True,False)


def reescalar_imagenes(lista_imagenes, anchura , altura):
    for lista in lista_imagenes:
        for i in range(len(lista)):
            lista[i] = pygame.transform.scale(lista[i],(anchura,altura))
lista_trampas=[animaciones_trampa_1]
lista_animacion_proyectil = [animacion_proyectil,animacion_proyectil_derecha]
lista_animaciones_enemigo_1 = [enemigo1_caminar,enemigo1_caminar_izquierda]
lista_animaciones_personaje = [personaje_quieto,personaje_saltando,personaje_correr,personaje_correr_derecha,personaje_salta_derecha,personaje_mira_derecha,personaje_ataque_mele,personaje_ataca_derecha,personaje_golpeado,personaje_golpeado_izquierda,personaje_dispara,personaje_dispara_izquierda,personaje_muere]

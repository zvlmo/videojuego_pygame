import pygame
def crear_fondo(path:str,pantalla_size):
    fondo = pygame.image.load(path)
    fondo = pygame.transform.scale(fondo, pantalla_size)
    return fondo

    
import pygame

class Plataformas():
    def __init__(self,path,size,x,y,pixeles):
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen,size)
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.piso = pixeles
    
    def get_top(self):
        return self.piso + self.rect.top
    
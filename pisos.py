import pygame

class Plataformas():
    def __init__(self,path,size,x,y,pixeles):
        self.imagen = pygame.image.load(path)
        self.imagen = pygame.transform.scale(self.imagen,size)
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.piso = pixeles
        self.velocidad = 3
        self.direccion = 1
    
    def get_top(self):
        return self.piso + self.rect.top
    def movimiento(self,top_range, bottom_range):
        
        # Actualizar la posición del rectángulo
        self.rect.y += self.velocidad * self.direccion
        # Cambiar de dirección si el rectángulo llega a los límites de la pantalla
        if self.rect.top <= top_range:
            self.direccion = 1
        elif self.rect.bottom >= bottom_range:
            self.direccion = -1
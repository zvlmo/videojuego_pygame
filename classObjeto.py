import pygame

class Objeto_game():
    def __init__(self,x,y):
        self.objeto = 'carne'
        self.imagen = pygame.image.load("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/OBJ/Ribs.png").convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen,(60,60))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direccion = 1
        self.velocidad = 1
        self.disparos = 5
        self.hp = 5

    def movimiento (self):
        self.rect.y += self.velocidad * self.direccion
        if self.rect.y >= 3:
            self.direccion = -1
        elif self.rect.y <= self.rect.y:
            self.direccion = 1
    def brindar_buff(self,personaje):
        if self.rect.colliderect(personaje.rect):
            personaje.disparos += self.disparos
            personaje.hp += self.hp
            personaje.puntos += 20
        
        #print(target.disparos)
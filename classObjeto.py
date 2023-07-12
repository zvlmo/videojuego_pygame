import pygame

class Objeto_game():
    def __init__(self,x,y,path):
        pygame.mixer.init()
        self.objeto = 'carne'
        self.imagen = pygame.image.load(path).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen,(60,60))
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direccion = 1
        self.velocidad = 1
        self.disparos = 8
        self.hp = 10
        self.agarrar = pygame.mixer.Sound("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/SONIDOS/agarroobjeto.wav")
        self.agarrar_sombrero = pygame.mixer.Sound("C:/Users/mathm/OneDrive/Escritorio/FACULTAD/PROGRA 1/PYGAME/PNGS/SONIDOS NUEVOS/Monkey D.Luffy29.mp3")
        self.pasos = 0
        
    
    def animar_objeto(self,acciones_peronaje):
            largo  = len(acciones_peronaje)
            if self.pasos >= largo:
                self.pasos = 0
            self.imagen = (acciones_peronaje[self.pasos])
            self.pasos += 1
            
    def movimiento (self):
        self.rect.y += self.velocidad * self.direccion
        if self.rect.y >= 3:
            self.direccion = -1
        elif self.rect.y <= self.rect.y:
            self.direccion = 1
    def brindar_buff_carne(self,personaje):
        
        if self.rect.colliderect(personaje.rect):
            self.agarrar.play()
            personaje.disparos += self.disparos
            personaje.puntos += 20
            personaje.hp += self.hp
    def brindar_puntos(self,personaje):
        if self.rect.colliderect(personaje.rect):
            personaje.puntos += 50
            self.agarrar_sombrero.play()
            #self.animar_personaje()
        #print(target.disparos)
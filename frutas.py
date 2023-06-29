import pygame,random

def crear_dona(anchura,altura,x,y,path):
    imagen_fruta = pygame.image.load(path)
    imagen_fruta = pygame.transform.scale(imagen_fruta,(anchura,altura))
    rectangulo = imagen_fruta.get_rect()
    rectangulo.x = x
    rectangulo.y = y
    
    diccionario_fruta = {}
    diccionario_fruta['superficie'] = imagen_fruta
    diccionario_fruta['rectangulo'] = rectangulo
    diccionario_fruta['velocidad'] = random.radint(10,20,1)
    
    return diccionario_fruta

def crear_lista_fruta(cantidad):
    lista = []
    for i in range(cantidad):
        x = random.randrange(0,740,60)
        y = random.randrange(-1000,0,60)
        dicc = crear_dona(x,y,60,60,"PROGRA 1\PYGAME\pygame intro\subirarchivos\Recursos\pacfrutita.png")
        lista.append(dicc)
    return lista

def update_fruta(lista):
    for fruta in lista:
        rect = fruta['rectangulo']
        rect.y += fruta['velocidad']

def verificar_colision(lista, personaje):
    for fruta in lista:
        rectangulo = pygame.Rect(personaje['rectangulo'])
        if rectangulo.colliderect(fruta['rectangulo']):
            desaparecer_fruta(fruta)
            personaje['score'] += 100
            print('colisiono')
def desaparecer_fruta(fruta):
    fruta['rectangulo'].x = random.randrange(0,740,60)
    fruta['rectangulo'].y = random.randrange(-1000,0,60)
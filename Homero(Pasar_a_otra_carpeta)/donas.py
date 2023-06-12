import pygame

class Dona:
    def __init__(self,size,coordenate,path_imagen):

        self.image = pygame.transform.scale(pygame.image.load(
        "Homero(Pasar_a_otra_carpeta)\homero_archivos\\dona.png").convert_alpha(),(size))
        self.rect = self.image.get_rect()
        self.rect.topleft = coordenate
        self.active = True
        
    def update(self):
        self.rect.y += 5

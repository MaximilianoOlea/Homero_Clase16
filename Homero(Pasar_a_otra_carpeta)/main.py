import pygame
import sys
from config import *
import random
from donas import *
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE_SCREEN)

pygame.display.set_caption("Donuts War")
icono = pygame.image.load(
    "Homero(Pasar_a_otra_carpeta)\homero_archivos\dona.png").convert_alpha()
icono = pygame.transform.scale(icono, (SIZE_ICON))
pygame.display.set_icon(icono)

fondo = pygame.image.load(
    "Homero(Pasar_a_otra_carpeta)\homero_archivos\\background.jpg").convert()
fondo = pygame.transform.scale(fondo, (SIZE_SCREEN))

homero_left = pygame.image.load(
    "Homero(Pasar_a_otra_carpeta)\homero_archivos\\homer_left.png").convert_alpha()
homero_left = pygame.transform.scale(homero_left, (HOMER_SIZE))
rect_homero = homero_left.get_rect()
rect_homero.midbottom = HOMER_POS_INICIAL

rect_homero_boca = pygame.rect.Rect(0,0,50,20)

rect_homero_boca.x = rect_homero.x + 42
rect_homero_boca.y = rect_homero.y + 120


homero_right = pygame.image.load(
    "Homero(Pasar_a_otra_carpeta)\homero_archivos\\homer_right.png").convert_alpha()
homero_right = pygame.transform.scale(homero_right, (HOMER_SIZE))
homero = homero_left

# ------Dona:
donuts = pygame.image.load(
    "Homero(Pasar_a_otra_carpeta)\homero_archivos\\dona.png").convert_alpha()
donuts = pygame.transform.scale(donuts, (DONUT_SIZE))
# rect_donuts = donuts.get_rect()
# rect_donuts.midtop = DISPLAY_MIDTOP
# flag_donuts = True

donas = []

for i in range(10):
    # donuts = pygame.image.load(
    #     "Homero(Pasar_a_otra_carpeta)\homero_archivos\\dona.png").convert_alpha()
    # donuts = pygame.transform.scale(donuts, (DONUT_SIZE))
    x = random.randrange(30,WIDTH-30)
    y = random.randrange(-1000,0)
    dona = Dona (DONUT_SIZE,(x,y),"Homero(Pasar_a_otra_carpeta)\homero_archivos\\dona.png")

    # donuts.get_rect().center = (x,y)
    donas.append(dona)
    # print (donuts.get_rect().center)
    
font = pygame.font.Font ("Homero(Pasar_a_otra_carpeta)\\assets\\fuente_simpson.ttf")
score = 0
# Sonido:
sonido = pygame.mixer.Sound("Homero(Pasar_a_otra_carpeta)\homero_archivos\ouch.mp3")
pygame.mixer.music.load("Homero(Pasar_a_otra_carpeta)\homero_archivos\ouch.mp3")
flag_sound = True
while True:
    clock.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(fondo, ORIGIN)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:

        if rect_homero.left > DISPLAY_LEFT:  # Si no esta del lado izquierdo
            rect_homero.x -= HOMER_SPEED
            homero = homero_left
            rect_homero_boca.x = rect_homero.x + 42
            rect_homero_boca.y = rect_homero.y + 120

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if rect_homero.right < DISPLAY_RIGHT:  # Si no esta del lado derecho
            rect_homero.x += HOMER_SPEED
            homero = homero_right
        rect_homero_boca.x = rect_homero.x + 60
        rect_homero_boca.y = rect_homero.y + 120



    pygame.draw.rect(screen,AZUL,rect_homero_boca)
    screen.blit(homero, rect_homero)

    for dona in donas:
        flag_dona = True
        flag_sound = True
        if dona.active:
            dona.update()
        else:
            dona.rect.y = 0

        if rect_homero_boca.colliderect(dona.rect):
            dona.active = False

            if flag_sound:
                score += 1
                pygame.mixer.music.play()
                pygame.mixer.music.set_pos(0.3)
                flag_sound = False
            else:
                flag_sound = True

        if dona.active:
            screen.blit(dona.image, dona.rect)
    # for donuts in donas:
    #     flag_donuts = True
    #     # rect_donuts = donuts.get_rect()

    #     if rect_donuts.bottom < DISPLAY_BOTTOM+100:
    #         donuts.update()
    #         screen.blit(donuts, rect_donuts)


        # if rect_homero_boca.colliderect (rect_donuts):
        #     flag_donuts = False
        #     if flag_sound:
        #         score += 1
        #         pygame.mixer.music.play()
        #         pygame.mixer.music.set_pos(0.2)
        #     flag_sound = False
        # else:
        #     flag_sound = True

        # if flag_donuts:
        #     screen.blit(donuts, rect_donuts)

    screen.blit(font.render("Score: " + str(score), True, AZUL),(DISPLAY_TOP,DISPLAY_LEFT))

    


        
            
    
    pygame.display.flip()

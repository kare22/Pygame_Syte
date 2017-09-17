##Kodutöö No12.
##Pygame: klaviatuuriga juhtimine 
##Karel Paan
##29.02.2016

#Toon sisse pygame mooduli ja süsteemi funktsioonid
import pygame,sys
pygame.init()

#Defineerin muutujad
laius= 1000
korgus=800

x=laius/2
y=korgus/2

samm=10

#Lisan pildi
pilt = pygame.image.load("Superbunny.jpg")

#Päis
aken = pygame.display.set_mode([laius,korgus])

#Annan nimetuse
pygame.display.set_caption("Jänkupoiss")

#Taust
aken.fill([255,255,255])

#Pildi uuendamine aknas
pygame.display.flip()

pygame.key.set_repeat(50,50)

#Programmi sulgemine, pildi animeerimine
while True:
    aken.fill([255,255,255])
    aken.blit(pilt,(x,y))
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
             if i.key == pygame.K_UP:
                y -= samm
             elif i.key == pygame.K_DOWN:
                y += samm
             elif i.key == pygame.K_LEFT:
                x -= samm
             elif i.key == pygame.K_RIGHT:
                x += samm
             while y==0:
                 False
             while y==670:
                 False
             while x==0:
                 False
             while x==850:
                 False

    
    


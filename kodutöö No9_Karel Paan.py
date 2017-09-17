##Kodutöö No9.
##Rakenduste loomise ja programeerimise alused
##Karel Paan
##01.02.2016


#Toon sisse pygame mooduli ja süsteemi funktsioonid
import pygame,sys
pygame.init()
#Päis
aken = pygame.display.set_mode([800,600])

#Värvid
valge = [255,255,255]
must = [0,0,0]
sinine = [0,0,225]

aken.fill(sinine)
#Kujundid
esimenering = pygame.draw.circle(aken,[255,255,255],[400,500],50)
teinering = pygame.draw.circle(aken,[255,255,255],[400,410],40)
kolmasring = pygame.draw.circle(aken,[255,255,255],[400,340],30)
kaabu = pygame.draw.rect(aken,must,[385,260,30,50])

#Päise kuvamine ekraanil
pygame.display.flip()
#Programmi sulgemine, valikul
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

##Kodutöö No10.
##Pygame: pildid, tekst
##Karel Paan
##08.02.2016


#Toon sisse pygame mooduli ja süsteemi funktsioonid
import pygame,sys
pygame.init()

#Päis
aken = pygame.display.set_mode([1000,800])

#NImi
pygame.display.set_caption("Boby")

#Värv
aken.fill([255,255,255])

#Pildi lisamine
Boby = pygame.image.load("Boby.jpg")
pildisuurus = Boby.get_rect().size

#Kuvan pildi
aken.blit(Boby,(500-pildisuurus[0]/2,400-pildisuurus[1]/2))

#lisan mingi teksti
kirjastiil = pygame.font.Font(None,30)
tekst_aknas = kirjastiil.render("Bobby Fischer",1,[0,0,0])
aken.blit(tekst_aknas,(450,50))

#Päise kuvamine ekraanil
pygame.display.flip()

#Programmi sulgemine, valikul
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

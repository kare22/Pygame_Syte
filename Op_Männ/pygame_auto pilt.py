

"""
Auto pilt

Koostage pygame´iga auto pilt.

"""



#Imporditakse pygame moodul.
import pygame, sys

#Pygame initseerimine
pygame.init()


#Värvid     R   G    B
valge =   [255, 255, 255]
must =    [  0,   0,   0]
sinine =  [  0,   0, 225]



#Mängule antakse pealkiri
pygame.display.set_caption("Auto joonistamine")

#Akna raam ja akna väljastamine
laius=800
korgus=600
aken=pygame.display.set_mode([laius,korgus])

#Aken värvitakse valgeks
aken.fill(valge)

#Joonistamine

#Joonistamisel võtab argument x väärtuse 0-lõpmatus vasakult paremale, argument y võtab väärtuseks 0-lõpmatus, ülevalt alla, kus x on laius ja y on kõrgus.

#Ristküliku objekt võtab argumendid(raam,värv,(laius,kõrgus,laius+x,kõrgus+x))
pygame.draw.rect(aken,sinine,(300,250,150,50))#Auto pealmine osa
pygame.draw.rect(aken,sinine,(250,300,300,100))#Auto kere
pygame.draw.rect(aken,valge,(320,270,30,40))#Auto aken

#Ring objekt võtab argumendid(raam,värv,(laius,kõrgus),ringi raadius)
pygame.draw.circle(aken,must,[300,400],40)#Auto ratas
pygame.draw.circle(aken,must,[500,400],40)#Auto ratas

#Koostatud andmed edastatakse ekraanile
pygame.display.flip()

while True:
    sys.exit()



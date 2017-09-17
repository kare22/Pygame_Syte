##Kodutöö No11.
##Rakenduste loomise ja programmeerimise alused
##Karel Paan
##15.02.2016

#Toon sisse pygame mooduli ja süsteemi funktsioonid
import pygame,sys
pygame.init()

#Päis
aken = pygame.display.set_mode([1000,800])

#Taust
aken.fill([255,255,255])

#Lisan pildi, koostan sellele tsükli ja argumenteering liikumise
pilt = pygame.image.load("Superbunny.jpg")
x = 1000
y = 0
for i in range (50):#tsükkel
    pygame.time.delay(20)
    pygame.draw.rect(aken,must, [x, y, 50, 50], 0) 
    x = x-10   #liikumise argument
    aken.blit(pilt, (x, y))
    pygame.display.flip()

#Programmi sulgemine, valikul
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()



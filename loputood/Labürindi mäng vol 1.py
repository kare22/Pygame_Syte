import pygame, sys

#Pygame initseerimine
pygame.init()

#V‰rvid     R   G    B
valge =   [255, 255, 255]
punane =  [255, 0  ,   0]
must =    [  0,   0,   0]
kollane = [255, 255,   0]
sinine =  [  0,   0, 225]


#Akna raam
laius=800
korgus=600
aken=pygame.display.set_mode([laius,korgus])

#Konsoolile antakse v√§rv- Valge
aken.fill(valge)

#Pıhi raam
pygame.draw.rect(aken, punane, [50, 50, 20, 500], 0) 

pygame.draw.rect(aken, punane, [750, 50, 20, 500], 0) 

pygame.draw.rect(aken, must, [50, 50, 700, 20], 0) 

pygame.draw.rect(aken, must, [100, 530, 650, 20], 0) 

#Teine ring


pygame.draw.rect(aken, punane, [100, 100, 20, 400], 0) 

pygame.draw.rect(aken, punane, [690, 150, 20, 400], 0) 

pygame.draw.rect(aken, must, [100, 100, 610, 20], 0) 

pygame.draw.rect(aken, must, [100, 480,610 , 20], 0)


#Kolmas ring

pygame.draw.rect(aken, punane, [340, 260, 20, 150], 0) 

pygame.draw.rect(aken, punane, [160, 260, 20, 150], 0) 

pygame.draw.rect(aken, punane, [160, 260,200 , 20], 0)

pygame.draw.rect(aken, must, [200, 390,160 , 20], 0)

pygame.display.flip()


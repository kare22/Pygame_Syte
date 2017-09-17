import pygame, sys, random

pygame.init()

##aeg=j
##skoor=i



#Värvid
valge = [255,255,255]
punane = [255,0,0]
must = [0,0,0]
kollane = [255,255,0]
sinine = [0,0,225]

Cv=10
C=60#Ringi raadius
laius=800
korgus=600
x=random.randrange(C,laius-C)
y=random.randrange(C,korgus-C)

teedu = pygame.mixer.Sound("teedu.WAV")
##aadu = pygame.mixer.Sound("aadu.wav")
##peedu = pygame.mixer.Sound("peedu.aif")

pygame.display.set_caption("Noolemäng")

aken=pygame.display.set_mode([laius,korgus])

aken.fill(valge)

pygame.draw.circle(aken,punane,[x,y],C)
pygame.draw.circle(aken,must,[x,y],Cv)

pygame.display.flip()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
                sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            hx,hy=i.pos
            if (hx > x-C and hx < x+C and hy > y-C and hy < y+C):
                teedu.play()
                x=random.randrange(C,laius-C)
                y=random.randrange(C,korgus-C)

                aken.fill(valge)

                pygame.draw.circle(aken,punane,[x,y],C)
                pygame.draw.circle(aken,must,[x,y],Cv)


                pygame.display.flip()

                                


            
                
                

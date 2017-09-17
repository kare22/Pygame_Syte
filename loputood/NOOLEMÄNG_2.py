import pygame, sys, random, time

pygame.init()

##aeg=k
##skoor=i
k=1

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
aadu = pygame.mixer.Sound("aadu.wav")
peedu = pygame.mixer.Sound("peedu.aif")

pygame.display.set_caption("Noolemäng")

aken=pygame.display.set_mode([laius,korgus])

aken.fill(valge)

pygame.draw.circle(aken,punane,[x,y],C)
pygame.draw.circle(aken,must,[x,y],Cv)

pygame.display.flip()

kirjastiil = pygame.font.Font(None,30)
tekst_aknas = kirjastiil.render("Bobby Fischer",1,[0,0,0])




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

                k=k+1


                    

                aken.fill(valge)

                pygame.draw.circle(aken,punane,[x,y],C)
                pygame.draw.circle(aken,must,[x,y],Cv)


                pygame.display.flip()
        if k==4:

            x=1000
            y=1000

            print("OKkki")
            aken.fill(valge)
            aken.blit(tekst_aknas,(laius/2,korgus/2))
            pygame.display.flip()
            if i.type == pygame.KEYDOWN:
                if i.key==pygame.K_c:
                    print("mhm")
                    x=random.randrange(C,laius-C)
                    y=random.randrange(C,korgus-C)
                    k=0
                    aken.fill(valge)

                    pygame.draw.circle(aken,punane,[x,y],C)
                    pygame.draw.circle(aken,must,[x,y],Cv)


                    pygame.display.flip()

                elif i.key==pygame.K_q:
                    sys.exit()
                    quit()



















                    


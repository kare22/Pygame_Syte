#Noolemäng
#Karel Paan, SS

import pygame, sys, random
pygame.init()


#Kordade arvu määraja(-1, menüü väärtus)
k=11

#Värvid
valge = [255,255,255]
punane = [255,0,0]
must = [0,0,0]
kollane = [255,255,0]
sinine = [0,0,225]

#Andmete väärtused
Cv=10#Väikeringi raadius
C=60#Ringi raadius
laius=800
korgus=600
x=random.randrange(C,laius-C)#Raadius arvutatakser maha selleks, et ring ekraani sees poleks
y=random.randrange(C,korgus-C)

#Helifail
teedu = pygame.mixer.Sound("teedu.WAV")

#Pealkiri
pygame.display.set_caption("Noolemäng")

#Ankna raamistik
aken=pygame.display.set_mode([laius,korgus])

#Ekraanile edastava teksti osad
kirjastiil = pygame.font.Font(None,30)
tekst_aknas = kirjastiil.render("Vajutage jätkamiseks C, lahkumiseks Q.",1,[0,0,0])
algtekst = kirjastiil.render("TERE!, selleks, et mängu minna, vajutage nuppu B.",True,[0,0,0])
korrad = kirjastiil.render("Kordi jaanud: "+str(k),True,[0,0,0])
korradalg = kirjastiil.render("Kordi jaanud: "+str(10),True,[0,0,0])

pygame.display.flip()



#Mänguu põhiosa
while True:
    #Menüü
    if k==11:
        aken.fill(valge)       
        aken.blit(algtekst,(140,korgus/2))
        pygame.display.flip()
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_b:
                    k=10
                    #Ringide joonistamine kahe erineva raadiusega
                    aken.fill(valge)
                    pygame.draw.circle(aken,punane,[x,y],C)
                    pygame.draw.circle(aken,must,[x,y],Cv)
                    aken.blit(korradalg,(0,0))
                    pygame.display.flip()
        
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
                sys.exit()
        elif i.type == pygame.MOUSEBUTTONDOWN:
            hx,hy=i.pos#Hiire kliki asukoha määramine
            if (hx > x-C and hx < x+C and hy > y-C and hy < y+C):
                #Loogiline sisu, põhiosa töötamiseks
                teedu.play()
                x=random.randrange(C,laius-C)
                y=random.randrange(C,korgus-C)
                #Iga klikiga läheb k madalamaks
                k=k-1
                aken.fill(valge)
                pygame.draw.circle(aken,punane,[x,y],C)
                pygame.draw.circle(aken,must,[x,y],Cv)
                korrad = kirjastiil.render("Kordi jaanud: "+str(k),True,[0,0,0])
                aken.blit(korrad,(0,0))
                pygame.display.flip()
        if k==0:#Kui k väärtus on 0, ehk kümme korda on ringile vajutatud
            x=1000#Selleks, et ringile klikkida ei saaks, on ring ekraanist välja pandud
            y=1000
            aken.fill(valge)
            aken.blit(tekst_aknas,(200,korgus/2))
            pygame.display.flip()
            if i.type == pygame.KEYDOWN:
                if i.key==pygame.K_c:
                    #Kui soovitakse uuesti mängida, esitatakse andmed uuesti ja k on 10, ehk läheb tagasi algusesse
                    x=random.randrange(C,laius-C)
                    y=random.randrange(C,korgus-C)
                    k=10
                    aken.fill(valge)
                    pygame.draw.circle(aken,punane,[x,y],C)
                    pygame.draw.circle(aken,must,[x,y],Cv)
                    korrad = kirjastiil.render("Kordi jaanud: "+str(k),True,[0,0,0])
                    aken.blit(korrad,(0,0))
                    pygame.display.flip()
                elif i.key==pygame.K_q:
                    sys.exit()
















                    


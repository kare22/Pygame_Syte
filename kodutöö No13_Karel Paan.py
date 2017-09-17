##Kodutöö N013, Hiire kasutamine pygames
##Karel Paan
##14.03.16


#Toon sisse Pygame mooduli
import pygame,sys
pygame.init()

#Defineerin kasutatavad muutujad
laius = 800
korgus = 600
x = laius/2
y = korgus/2

#Määran kasutatavad pildid
pilt1 = pygame.image.load("Boby.jpg")
pilt2 = pygame.image.load("Superbunny.jpg")

#Koostan päise raami
aken = pygame.display.set_mode([laius,korgus])

#Annan üllitisele pealkirja
pygame.display.set_caption("Hiire animatsioonid")

#Defineerin erinevate värvide väärtused
valge = [255,255,255]
punane = [255,0,0]
must = [0,0,0]

#Koostan hiire animatsiooni
while True:
    #Toon moodulisse pildi ja määran selle asukoha
    aken.fill(valge)
    aken.blit(pilt1,(350,250))
    pygame.display.flip()
    #Moodustan lahkumise võimaluse
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        #Moodustan hiire allaklõpsamise käsu    
        elif i.type == pygame.MOUSEBUTTONDOWN:
            x,y = i.pos
            #Määran hiire kordinaatide kriteeriumi, et pilt vahetuks
            if (x > 350 and x < 450 and y > 250 and y <350):
                    #Kui kõik on nii nagu peab, väljastab moodul jänku pildi
                    while True:
                        aken.fill(valge)
                        aken.blit(pilt2,(350,250))
                        pygame.display.flip()

#Tsükklit käima ei saanud. Samuti proovisin MOUSEBUTTONUP-i, aga see ka ei töötand.

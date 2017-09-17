#Uss labürindis mäng
#Daniel Männiste



import pygame, sys

#Pygame initseerimine
pygame.init()


#Värvid     R   G    B
valge =   [255, 255, 255]
punane =  [255, 0  ,   0]
must =    [  0,   0,   0]
kollane = [255, 255,   0]
sinine =  [  0,   0, 225]

#Kella defineerimine
kell=pygame.time.Clock()

#Mängule antakse pealkiri
pygame.display.set_caption("Uss labürindis")

#Akna raam
laius=800
korgus=600
aken=pygame.display.set_mode([laius,korgus])

#Muutuja koguväärtus
lead_x=80
lead_y=560

#Muutuja väärtus noole nuppe vajutades
lead_x_change = 0
lead_y_change = 0

#tsüklile omane väärtus
k=0

kirjastiil = pygame.font.Font(None,30)

pygame.display.flip()





while True:
    
    if k==0:
        aken.fill(valge)
        tekst_aknas2 = kirjastiil.render("Tere! Mängu alustamiseks, vajutage nuppu A.",1,[0,0,0])
        aken.blit(tekst_aknas2,(160,300))
        pygame.display.flip()
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN:
                if i.key==pygame.K_a:
                    k=k+1
        

    if k==1:
        for i in pygame.event.get():
           if i.type == pygame.QUIT:
               sys.exit()
           if i.type == pygame.KEYDOWN:
                if i.key==pygame.K_LEFT:
                    lead_x_change=-10
                if i.key==pygame.K_RIGHT:
                    lead_x_change=10
                if i.key==pygame.K_UP:
                    lead_y_change=-10
                if i.key==pygame.K_DOWN:
                    lead_y_change=10
           if i.type == pygame.KEYUP:
                if i.key==pygame.K_LEFT:
                    lead_x_change=0
                if i.key==pygame.K_RIGHT:
                    lead_x_change=0
                if i.key==pygame.K_UP:
                    lead_y_change=0
                if i.key==pygame.K_DOWN:
                    lead_y_change=0
           print(i)
        #Loogiline sisu, muutujatele
        aken.fill(valge)

        #Õun
        pygame.draw.rect(aken,punane, [290,290,40,40],0)



        #Esimene raam
        pygame.draw.rect(aken, must, [50, 50, 20, 500], 0) 

        pygame.draw.rect(aken, must, [750, 50, 20, 500], 0) 

        pygame.draw.rect(aken, must, [50, 50, 700, 20], 0) 

        pygame.draw.rect(aken, must, [100, 530, 650, 20], 0) 

        #Teine ring


        pygame.draw.rect(aken, must, [100, 100, 20, 400], 0) 

        pygame.draw.rect(aken, must, [690, 150, 20, 400], 0) 
        pygame.draw.rect(aken, must, [100, 100, 610, 20], 0) 

        pygame.draw.rect(aken, must, [100, 480,610 , 20], 0)


        #Kolmas ring

        pygame.draw.rect(aken, must, [340, 260, 20, 150], 0) 

        pygame.draw.rect(aken, must, [160, 260, 20, 150], 0) 

        pygame.draw.rect(aken, must, [160, 260,200 , 20], 0)

        pygame.draw.rect(aken, must, [200, 390,160 , 20], 0)


        #Muutuja muutumise liitmine
        lead_y+=lead_y_change
        lead_x+=lead_x_change

        #Liikuva objekti väljastamine
        pygame.draw.rect(aken,must,[lead_x,lead_y,10,10])
        pygame.display.flip()

        #Pildi muutmise kordade arv sekundis, hetkel 20 pildimmutmist sekundis, kui nool alla vajutatakse
        kell.tick(20)
        if lead_x>40 and lead_x<70 and lead_y<550 and lead_y>40 or lead_x>740 and lead_x<770 and lead_y<550 and lead_y>40:
            lead_x=80
            lead_y=560
            lead_x_change = 0
            lead_y_change = 0
        if lead_x>680 and lead_x<710 and lead_y<550 and lead_y>150 or lead_x>330 and lead_x<360 and lead_y<410 and lead_y>250:
            lead_x=80
            lead_y=560
            lead_x_change = 0
            lead_y_change = 0
        if lead_x<0 or lead_x>790 or lead_y<0 or lead_y>590 or lead_x>190 and lead_x<360 and lead_y>380 and lead_y<410:
            lead_x=80
            lead_y=560
            lead_x_change = 0
            lead_y_change = 0
        if lead_x>150 and lead_x<180 and lead_y<410 and lead_y>250 or lead_x>150 and lead_x<360 and lead_y>250 and lead_y<280 or lead_x>90 and lead_x<120 and lead_y>100 and lead_y<500:
            lead_x=80
            lead_y=560
            lead_x_change = 0
            lead_y_change = 0
        if lead_x>40 and lead_x<760 and lead_y>40 and lead_y<70 or lead_x>90 and lead_x<710 and lead_y>90 and lead_y<120 or lead_x>90 and lead_x<710 and lead_y>470 and lead_y<500:
            lead_x=80
            lead_y=560
            lead_x_change = 0
            lead_y_change = 0
        if lead_x>90 and lead_x<750 and lead_y>520 and lead_y<550 or lead_x>680 and lead_x<710 and lead_y>140 and lead_y<160:
            lead_x=80
            lead_y=560
            lead_x_change = 0
            lead_y_change = 0
        if lead_x>280 and lead_x<330 and lead_y>280 and lead_y<330:
            k=2



    if k==2:
        aken.fill(valge)
        tekst_aknas = kirjastiil.render("Jätkamiseks vajutage A, sulgemiseks vajutage B",1,[0,0,0])
        aken.blit(tekst_aknas,(160,300))
        pygame.display.flip()
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN:
                if i.key==pygame.K_a:
                    k=1
                    lead_x=80
                    lead_y=560
                    lead_x_change = 0
                    lead_y_change = 0
                if i.key==pygame.K_b:
                    sys.exit()
                    pygame.quit()
    
                




        





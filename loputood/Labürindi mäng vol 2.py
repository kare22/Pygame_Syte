import pygame, sys

#Pygame initseerimine
pygame.init()

#V‰rvid     R   G    B
valge =   [255, 255, 255]
punane =  [255, 0  ,   0]
must =    [  0,   0,   0]
kollane = [255, 255,   0]
sinine =  [  0,   0, 225]

#Kella defineerimine
kell=pygame.time.Clock()

#Akna raam
laius=800
korgus=600
aken=pygame.display.set_mode([laius,korgus])

#Muutuja muutujad
lead_x=80
lead_y=560
lead_x_change = 0
lead_y_change = 0


#Konsoolile antakse v√§rv- Valge
aken.fill(valge)

#Liikuva objekti v‰ljastamine
pygame.draw.rect(aken,must,[lead_x,lead_y,10,10])


#Pıhi raam
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

pygame.display.flip()









while True:
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
           
    #Loogiline sisu, muutujatele
    aken.fill(valge)
    #Pıhi raam
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
    lead_y+=lead_y_change
    lead_x+=lead_x_change

    
    pygame.draw.rect(aken,must,[lead_x,lead_y,10,10])
    pygame.display.flip()

    kell.tick(20)
    if lead_x<0 or lead_x>790 or lead_y<0 or lead_y>590 or lead_x>40 and lead_x<70 and lead_y<550 and lead_y>40 or lead_x>740 and lead_x<770 and lead_y<550 and lead_y>40 or lead_x>680 and lead_x<710 and lead_y<550 and lead_y>150:
        lead_x=80
        lead_y=560
        lead_x_change = 0
        lead_y_change = 0
    if lead_x>90 and lead_x<120 and lead_y<500 and lead_y>100:
                lead_x=80
                lead_y=560
                lead_x_change = 0
                lead_y_change = 0





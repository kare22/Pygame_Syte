import pygame, sys


pygame.init()


#Värvid     R   G    B
valge =   [255, 255, 255]
punane =  [255, 0  ,   0]
must =    [  0,   0,   0]
kollane = [255, 255,   0]
sinine =  [  0,   0, 225]


kell=pygame.time.Clock()


pygame.display.set_caption("sdfgdfsdf")


laius=800
korgus=600
aken=pygame.display.set_mode([laius,korgus])


lead_x=80
lead_y=560


lead_x_change = 0
lead_y_change = 0


k=0

kirjastiil = pygame.font.Font(None,30)

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
           print(i)

        aken.fill(valge)

        lead_y+=lead_y_change
        lead_x+=lead_x_change


        pygame.draw.rect(aken,must,[lead_x,lead_y,10,10])
        pygame.display.flip()


        





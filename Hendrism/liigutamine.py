

import pygame, sys, time
pygame.init()

ekraan = pygame.display.set_mode([800, 600])
valge = [255, 255, 255] #Valge värv
pygame.display.set_caption("Elevant") #Avanenud ekraani pealkiri

pilt = pygame.image.load("Superbunny.jpg") #Laen pildi

pildisuurus=pilt.get_rect().size
x=400-(pildisuurus[0]/2) #Määran pildi algkordinaadid 
y=300-(pildisuurus[1]/2)


pygame.key.set_repeat(5,30)
samm=3   
while True:
    ekraan.fill(valge)
    ekraan.blit(pilt,(x,y))#Paigutan pildi vastavasse asukohta
    pygame.display.flip()
    for i in pygame.event.get():
       if i.type == pygame.QUIT:
           sys.exit()
       elif i.type == pygame.KEYDOWN:
           if i.key == pygame.K_UP and y>0: #Kui vajutatakse ülemist klahvi ja pilt ei ole liiga kõrgel,
               y=y-samm #Liigub üles
           elif i.key == pygame.K_DOWN and y<600-pildisuurus[1]: #Kui vajutatakse alumist klahvi ja pilt ei ole liiga all,
                y = y + samm #Liigub alla 
           elif i.key == pygame.K_LEFT and x>0: #Kui vajutatakse vasakut klahvi ja pilt ei ole liiga vasakul,
                x = x - samm #liigub vasakule
           elif i.key == pygame.K_RIGHT and x<800-pildisuurus[0]:#Kui vajutatakse paremat klahvi ja pilt ei ole liiga paremal,
                x = x + samm #liigub paremale    

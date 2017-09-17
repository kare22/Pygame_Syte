### -*- coding: cp1257 -*-
##'''pildi_liigutamine
##Hendriico Merila
##Pildi liikuma panemine nooleklahvidega'''

import pygame, sys, time
pygame.init()

ekraan = pygame.display.set_mode([800, 600])
valge = [255, 255, 255] #Valge värv
pygame.display.set_caption("Muutuv pilt") #Avanenud ekraani pealkiri

pilt = pygame.image.load("Boby.jpg") #Laen esimese pildi
pilt2= pygame.image.load("Superbunny.jpg")#Laen teise pildi
pildisuurus=pilt.get_rect().size #Leian pildi suurused, kuna mul on pildid sama suurusega, siis piisab ainult ühe leidmisest
x=400-(pildisuurus[0]/2) #Määran pildi algkordinaadid 
y=300-(pildisuurus[1]/2)
s=1 #Uus muutuja 
while True:
    ekraan.fill(valge)
    if s%2==1: #Kui s on paaritu arv,siis panen esimese pildi
        ekraan.blit(pilt,(x,y))
    elif s%2==0: #Kui s on paarisarv, siis panen teise pildi
        ekraan.blit(pilt2,(x,y))
    pygame.display.flip()
    for i in pygame.event.get():
       if i.type == pygame.QUIT:
           sys.exit()
       elif i.type == pygame.MOUSEBUTTONDOWN  : #Kui vajutatakse hiirt,
           x,y=i.pos #saan selle koha kordinaadid
           if y<=300+(pildisuurus[1]/2)and y>=300-(pildisuurus[1]/2)and x<=400+(pildisuurus[0]/2)and x>=400-(pildisuurus[0]/2):#Kui kordinaadid asuvad pildil,
               s=s+1#Muudan s-i paarsust ja sellega ka pilti
    x=400-(pildisuurus[0]/2)# Paigutan pildi jälle keskele tagasi, et ta ei liiguks koos hiirega   
    y=300-(pildisuurus[1]/2)   
  
           
              
     

               
          

          

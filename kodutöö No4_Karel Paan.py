##Neljas Kodutöö, loetelu paarisarvude keskmine
##Karel Paan
##7.12.15

#Sisestan arvude küsimise
arv1 = int(input("Sisestage loendi esimene arv: "))
arv2 = int(input("Sisestage loendi viimane arv: "))

#Loon abimuutuja, et leida vahemikus olevate paarisarvude summat
summa = 0 

#Loen paarisarvude hulga
paarisarvud = 0 

#Koostan tsükli
for i in list(range(arv1,arv2+1,1)):
    if i % 2 == 0: #Kasutan modulot, mis leiab jäägi
        summa += i
        paarisarvud += 1

#Leian keskmise
keskmine = summa / paarisarvud

#Prindin selle välja
print(keskmine)

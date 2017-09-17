##Kolmas Kodutöö
##Karel Paan, SS
##30.11.2015
read = int(input("Sisestage ridade arv: "))
istekohad = int(input("Kohtade arv reas: "))

rida = "" ##juurdeliidetatav

for i in range(1, istekohad+1, 1):
    rida += str(i) + " " ##" " annab numbrite ridadele vahed, saab ka ilma ridatetta, kui see osa lihtsalt ära võtta
rida += "\n" ##See paneb numbrid üksteise alla tulpa, muidu oleks väljund, kui vasakult paremale jada
##print((rida+"\n")*read), on teine võimalus selle kujutamiseks, nagu videos välja toodi
print(rida*read)

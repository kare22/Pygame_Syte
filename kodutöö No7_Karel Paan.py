##Kodutöö 7
##Karel Paan
##Rakenduste loomise ja programmeerimise alused
##18.01.16


fail = open("andmed.txt") #käsen konsoolil avada andmete fail
sisu = fail.read()
andmed = sisu.split(";")#andmed eristatakse semikooloni abil
sone = ""#sisestatud andme väärtus
for i in range(int(andmed[2])):
                for j in range(int(andmed[3])):
                                if i == int(andmed[0])-1 and j == int(andmed[1])-1:#määran x-i oma asukohale
                                                sone += "x"
                                else:
                                                sone += "." #loon saali, kõik pelae minu koha tähistatakse punktiga
                                if j == (int(andmed[3])-1):
                                                sone += "\n"
                

fail.close() #fail suletakse ja saadud tulemusena luuakse fail, kus saadud tulem on sees
teine_fail = open("tulemus.txt", "w")
teine_fail.write(sone)
teine_fail.close()

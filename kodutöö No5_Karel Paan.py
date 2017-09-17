#Viies Kodutöö
#Karel Paan SS
#15.12.15

# loon aluse sõnastikule
telefoniraamat = {}
nimed = []

#koostan tsükli, mis tööta, kuni on tõsi, kui vajutada lihtsalt enter, kajastab ta sõnaraamatu
while True:
    nimi = raw_input("Sisesta nimi (lopetamiseks vajuta .space.): ")
    if nimi == "":
        break#kui sisestatakse sõne, küsib programm järgmisena numbrit, peale numbrit uuesti nimi ja nii kuni tsükkel lõpetatakse
    telefon = raw_input("Sisesta telefoninumber: ") 
    nimed.append(nimi) # koostan listi elemendi
    andmed = (str(nimi) + " " + str(telefon))  # loon väärtuse, kus on nii nimi kui ka number 
    telefoniraamat[nimi] = andmed   # lisame sõnastikku  elemendi, mille võti on nimi ning sinu nimi ja number
#kui vastus on false, ehk tühik, lõpetab tsükkel oma töö

print("Telefoniraamatu sisu: ")
# annan käsu kogu sisu üksteise alla printida
for i in range(len(telefoniraamat)):
    telefoniraamatusisu = nimed[i]  
    #nüüd prindib programm kõik nimed vastavalt sisestuse järjekorrale välja
    print(telefoniraamat[telefoniraamatusisu]) # kuvan ekraanile konsoolis koostatud sisu

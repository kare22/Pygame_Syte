##Kodutöö No6
##Karel Paan
##11.01.16
##Funktisoonid ehk alamprogrammid

#Defineerin kalkolaatori väärtuse.
def kalkulaator(esimenearv,tehe,teinearv):
    if (tehe == "+"):#See os on sama teise ülesandega.
        vastus = str(esimenearv) + "+" + str(teinearv) + "=" + str(esimenearv + teinearv)
    elif (tehe == "-"):
        vastus = str(esimenearv) + "-" + str(teinearv) + "=" + str(esimenearv - teinearv)
    elif (tehe == "*"):
        vastus = str(esimenearv) + "+" * str(teinearv) + "=" + str(esimenearv * teinearv)
    elif (tehe == "/"):
        if (teinearv == 0):
            vastus = "VIGA!:nulliga ei saa jagada"
        else:
                vastus = str(esimenearv) + "/" + str(teinearv) + "=" + str(esimenearv / teinearv)
    return vastus
def pohi(): #Loon programmile tsükli, ehk kui kasutaja soovib kalkulaatorit uuesti kasutada ei pea kogu aeg F5-te kasutama.
    run = 1
    while run == 1:#Kuni runi väärtus on üks, lõpetab ta peale teise arvu sisestamist oma töö ja pakub võimalust selle taasalustamiseks.
        esimenearv = float(raw_input("Sisestage esimene arv: "))#Koostan arvude ja tehte sisestamise võimaluse, nagu ka teises ülesandes.
        tehe = raw_input("Sisestage tehe: ")
        teinearv = float(raw_input("Sisestage teine arv: "))

        vastus = kalkulaator(esimenearv,tehe,teinearv)
        print vastus
        print
        print
        end = raw_input("Sisestage l, et lahkuda, e, et edasi minna. ")
        if (end == "l"):
            run = 0

pohi()


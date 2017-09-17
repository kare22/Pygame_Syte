'''
Õunapuu õunade ülesanne

Eesmärgiks on talumehle öelda, kui palju tal õunu kokku on.
Oletame, et ühe puu peal kasvab kümme õuna.

Koosta programm, mis küsib talumehelt õunapuude arvu ja hiljem tagastab õunade kogusumma.
NB! Oma töös kasuta funktsiooni!

'''


#Näide

#Luuakse sisend, kuhu talumees sisestab oma õunapuude arvu.
ounap=input("Tere! Sisestage õunapuude arv: ")

#Luuakse funktsioon
def ounad(ounapuu):#Koostatakse funktsioon, mille nimeks on "ounad", mis arvutab antud arvväärtusel lahendi.
    tulemus=10*ounapuu#Funktsiooni põhiosa, kuna igal puul on kümme õuna on õunapuude arv vaja korrutada kümnega.
    return (tulemus)#Tagastatakse saadud tulem.



#Talumehele edastatakse ekraanile tema koguõuna summa.
print("Teie õuna kogusumma on "+ str(ounad(ounap)) +" õuna.")

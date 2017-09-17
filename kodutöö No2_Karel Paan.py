##Teine kodutöö
##Karel Paan SS
##23.11.15

esimenearv = input ("Sisestage esimene arv: ")
teinearv = input ("Sisestage teine arv: ")


tehe = input (str("Sisestage tehe: "))


##On jutumärkides, sest ei osanud teha nii,et konsooli saaks panna algse märgi.
plus="+"
minus="-"
times="*"
share="/"

if tehe == plus:
    print ((str(esimenearv) + "+" + str(teinearv) + "=" + str(esimenearv + teinearv)))
if tehe == minus:
    print ((str(esimenearv) + "-" + str(teinearv) + "=" + str(esimenearv - teinearv)))
if tehe == times:
    print ((str(esimenearv) + "*" + str(teinearv) + "=" + str(esimenearv * teinearv)))
if tehe == share:
    print ((str(esimenearv) + "/" + str(teinearv) + "=" + str(esimenearv / teinearv)))

##Komakohaga arve arvutab õigesti.
##Jagamine nulliga fikseerimata.

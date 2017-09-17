'''
Failioperatsioon

Dialoog on hargnenud kahte faili, sinu ülesandeks on tekidada uus fail, kuhu kogu dialoog kokku panna.
kiri1=
Tere!

Härra, kuidas saan teid aidata?

kiri2=
Tere! Sooviksin tassi kohvi.

'''



#Avatakse esimene fail
fail=open("kiri1.txt")
#Loetakse andmed
sisu=fail.read()
#Fail suletakse
fail.close() 

#Avatakse teine fail
teine_fail=open("kiri2.txt")
#Loetakse andmeid
sisu2=teine_fail.read()
#Fail sulgetakse
teine_fail.close() 

#Koostatakse uus teksti fail
kolmas_fail = open("kiri3.txt", "w")
#Teksti failile väljastatakse andmed
kolmas_fail.write(sisu)
kolmas_fail.write(sisu2)
#Kolmas fail suletakse
kolmas_fail.close()

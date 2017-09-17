from math import ceil
 
print ("Mitu küpsist on laiuti?:" )
laius=input()
print ("Mitu küpsist on pikuti?:" )
pikkus=input()
print ("Mitu küpsise kihti on?:" )
kiht=input()
print ("Mitu küpsist on pakis?:" )
pakk=input()


alg_kook = laius*pikkus*kiht/pakk

kook = ceil(alg_kook)

print(str(kook))

print ("výtejte v aplikaci pro výpočet objemu kvádru")

a = input ("zadejte délku strany A ")
b = input ("zadejte délku strany B ")
c = input ("zadejte délku strany C ")

a = int(a)
b = int(b)
c = int(c)

if a>0:
   if b>0:
    if c>0:
        print("výsledek je:")
    print(a*b*c)

else:
    print("nedá se dělit nulou")
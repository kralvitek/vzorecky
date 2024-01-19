print("Vítejte v aplikaci pro výpočet obvodu obdelníku")

a = input("zadejte délku strany a:")
b = input("zadejte délku strany b:")

a = int(a)
b = int (b)

if a>0 and b>0:
    print("výsledek je:")
    print(2*a+2*b)
else:
    print("copak to děláš blbečku")
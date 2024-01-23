print("Vítejte v aplikaci pro výpočet obsah kruhu")

r = input("zadejte délku strany r:")

r = int(r)

if r>0:
    print("výsledek je:")
    print(r*r*3.14)
else:
    print("copak to děláš blbečku takhle to nefunguje")
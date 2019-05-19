import time
jatkuu = True
rivi = ""
uusi = ""
nykyinen = ""
try:
    tiedosto = open("muistio.txt", "r")

except IOError:
    print("Oletusmuistiota ei löydy, luodaan tiedostoa.")
    tiedosto = open("muistio.txt", "w")



while jatkuu:
    nykyinen = tiedosto.name
    print("Käytetään muistiota:", tiedosto.name)
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Vaihda muistiota\n(5) Lopeta\n")
    valinta = int(input("Mitä haluat tehdä?: "))
    if valinta == 1:
        tiedosto = open(nykyinen, "r")
        sisalto = tiedosto.readlines()
        for i in sisalto:
            print(i)
        tiedosto.close()
    elif valinta == 2:
        tiedosto = open(nykyinen, "a")
        rivi = input("Kirjoita uusi merkintä: ")
        rivi += ":::"
        rivi += time.strftime("%X %x")
        rivi += "\n"
        tiedosto.write(rivi)
        tiedosto.close()
    elif valinta == 3:
        tiedosto.close()
        tiedosto = open(nykyinen, "w")
        print("Muistio tyhjennetty.")
    elif valinta == 4:
        try:
            uusi = input("Anna tiedoston nimi:")
            tiedosto = open(uusi,"r")

        except IOError:
            print("Tiedostoa ei löydy, luodaan tiedosto.")
            tiedosto = open(uusi,"w")

    elif valinta == 5:
        tiedosto.close()
        jatkuu = False
        print("Lopetetaan.")
    else:
        print("Tuntematon valinta.\n")
import random
kone, voitot, kierrokset, tasapelit = 0, 0, 0, 0
valinnat = ["", "Jalka", "Ydinase", "Torakka"]
while True:
    valinta = input("Jalka, Ydinase vai Torakka? (Lopeta lopettaa):")
    if valinta == "Lopeta":
        break
    else:
        kone = valinnat[random.randint(1, 3)]
        tulos = kone[:1] + valinta[:1]
        print("Sinä valitsit: ", valinta, "\ntietokone valitsi:", kone)
        kierrokset += 1
        if valinta == kone:
            print("Tasapeli!")
            tasapelit += 1
        elif tulos == "JT" or tulos == "TY" or tulos == "YJ":
            print("Hävisit!")
        else:
            print("Voitit!")
            voitot += 1
print("Pelasit",kierrokset,"kierrosta, joista voitit",voitot, "ja pelasit tasan",tasapelit, "peliä.")
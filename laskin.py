import math


def main():

    jatkuu = True
    luku1 = tarkastaja()
    luku2 = tarkastaja()
    while jatkuu:
        print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(luku1/luku2)\n(6)cos(luku1/luku2)\n(7)Vaihda luvut\n(8)Lopeta\nValitut luvut: ",luku1,luku2)
        valinta = int(input("Tee valinta (1-8): "))
        if valinta == 1:
            print("Tulos on: ", luku1 + luku2)
        elif valinta == 2:
            print("Tulos on: ", luku1 - luku2)
        elif valinta == 3:
            print("Tulos on: ", luku1 * luku2)
        elif valinta == 4:
            print("Tulos on: ", luku1 / luku2)
        elif valinta == 5:
            print("Tulos on: ", math.sin(luku1/luku2))
        elif valinta == 6:
            print("Tulos on: ", math.cos(luku1/luku2))
        elif valinta == 7:
            luku1 = tarkastaja()
            luku2 = tarkastaja()
        elif valinta == 8:
            jatkuu = False
        else:
            print("Valintaa ei tunnistettu.")


def tarkastaja():
    while True:
        try:
            luku = input("Anna luku:")
            luku = int(luku)

        except ValueError:
            print("Virheellinen syöte!")

        else:
            return luku




if __name__ == "__main__":
    main()

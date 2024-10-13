import random

def raad_het_nummer():
    nummer = random.randint(1, 100)
    pogingen = 0
    print("Welkom bij Raad het nummer!")
    print("Raad een nummer tussen 1 en 100.")

    while True:
        gok = input("Voer je gok in: ")

        try:
            gok = int(gok)
        except ValueError:
            print("Voer een geldig nummer in.")
            continue

        pogingen += 1

        if gok < nummer:
            print("Hoger!")
        elif gok > nummer:
            print("Lager!")
        else:
            print(f"Gefeliciteerd! Je hebt het nummer {nummer} geraden in {pogingen} pogingen.")
            break

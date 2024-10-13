import random


def galgje():
    woorden = ['auto', 'fiets', 'huis', 'boom', 'computer']
    woord = random.choice(woorden)
    geraden_letters = []
    fouten = 0
    max_fouten = 5

    print("Welkom bij Galgje!")

    while fouten < max_fouten:
        display = ""
        for letter in woord:
            if letter in geraden_letters:
                display += letter
            else:
                display += "_"

        print("Woord:", display)

        gok = input("Raad een letter: ")

        if gok in geraden_letters:
            print("Je hebt deze letter al geraden.")
        elif gok in woord:
            geraden_letters.append(gok)
            print("Goed gedaan!")
        else:
            fouten += 1
            print("Fout! Aantal fouten:", fouten)

        if all(letter in geraden_letters for letter in woord):
            print("Gefeliciteerd, je hebt het woord geraden:", woord)
            break
    else:
        print("Helaas, je hebt verloren. Het woord was:", woord)


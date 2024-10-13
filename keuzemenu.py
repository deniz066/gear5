import galgje  # Importeer het galgje bestand
import raad_het_nummer  # Importeer het raad_het_nummer bestand

def main_menu():
    while True:
        print("\nKies een spel:")
        print("1. Galgje")
        print("2. Raad het nummer")
        print("3. Stop")

        keuze = input("Maak je keuze: ")

        if keuze == '1':
            galgje.galgje()  # Roep de galgje functie aan vanuit het galgje.py bestand
        elif keuze == '2':
            raad_het_nummer.raad_het_nummer()  # Roep de raad_het_nummer functie aan vanuit het raad_het_nummer.py bestand
        elif keuze == '3':
            print("Bedankt! Tot ziens!")
            break
        else:
            print("Ongeldige keuze, probeer het opnieuw.")

if __name__ == "__main__":
    main_menu()

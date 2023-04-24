import GAME
import kostka
import pocetHracu
rules = open("pravidla.txt", "r")
print(f"Výtej u pthon hry Osadníci z Katanu,\n Pro zobrazení pravidel zavolej funkcy pravidla()\n pro začátek hry zavolej funkcy hra()")

def pravidla():
    text = rules.readlines()
    print(text)
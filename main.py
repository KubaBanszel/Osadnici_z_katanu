import GAME
import kostka

rules = open("pravidla.txt", "r")
print(f"Výtej u python hry Osadníci z Katanu,\n Pro zobrazení pravidel zavolej funkcy pravidla()\n pro začátek hry zavolej funkcy hra()")

def pravidla():
    return rules.readlines()

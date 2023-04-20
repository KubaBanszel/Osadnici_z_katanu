def pocitaniHracu():
    pocetHracu = int(input("Zadej pocet hracu od 2 do 4: "))

    if pocetHracu >= 5 or pocetHracu <= 1:
        print("Špatně zadaný počet hráčů, počet hráčů musí být od 2 do 4")
        pocitaniHracu()

pocitaniHracu()

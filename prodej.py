def sell():
    global poleHrace
    global budovy1
    global budovy2
    global budovy3
    global budovy4
    global budovy5
    global penize
    print("Teď si můžeš vybrat jakou budovu chceš prodat.")
    if poleHrace != len(poleHrace) == 0:
        print(f"Budov na čísle 1 máš: {budovy1}")
        print(f"Budov na čísle 2 máš: {budovy2}")
        print(f"Budov na čísle 3 máš: {budovy3}")
        print(f"Budov na čísle 4 máš: {budovy4}")
        print(f"Budov na čísle 5 máš: {budovy5}")
        kterou = input("Pro prodání budovy zadej číslo, podle čísla na kterém stojí: ")
        if kterou == 1:
            poleHrace.remove("1")
            penize += 4
            exit()
        elif kterou == 2:
            poleHrace.remove("2")
            penize += 4
            exit()
        elif kterou == 3:
            poleHrace.remove("3")
            penize += 4
            exit()
        elif kterou == 4:
            poleHrace.remove("4")
            penize += 4
            exit()
        elif kterou == 5:
            poleHrace.remove("5")
            penize += 4
            exit()
        
        
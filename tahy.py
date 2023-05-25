import kostka

penize = 10
poleHrace = []


hrac_x = 0
hrac_y = 0
cisloTahu = 1

print("Vítej ve hře Turista v Katanu!\n Při cestování ti zloděj zajal syna.\n Jako výkupné po tobě chce 75 peněz, které musíš získat nakupováním a prodáváním budov")
print("Přečti si pravidla a vydej se")
print(f"\n hru spustíš zadáním příkazu tah().")
    
def tah():
    global penize
    global cisloTahu
    print(f"Jsi na tahu číslo {cisloTahu}")
#Toto zařizuje prodávání budov
    if cisloTahu != 1:
        odpoved = input("Chceš v tomto kole prodat jednu svoji budovu? Ano = a, Ne = n")
        if odpoved == "a":   
            global poleHrace
            global penize
            budovy1 = poleHrace.count("1")
            budovy2 = poleHrace.count("2")
            budovy3 = poleHrace.count("3")
            budovy4 = poleHrace.count("4")
            budovy5 = poleHrace.count("5")
            print("Teď si můžeš vybrat jakou budovu chceš prodat.")
            if len(poleHrace) != 0:
                print(f"Budov na čísle 1 máš: {budovy1}")
                print(f"Budov na čísle 2 máš: {budovy2}")
                print(f"Budov na čísle 3 máš: {budovy3}")
                print(f"Budov na čísle 4 máš: {budovy4}")
                print(f"Budov na čísle 5 máš: {budovy5}")
                kterou = int(input("Pro prodání budovy zadej číslo, podle čísla na kterém stojí: "))
                if kterou == 1:
                    poleHrace.remove("1")
                    penize += 4
                    
                elif kterou == 2:
                    poleHrace.remove("2")
                    penize += 4
                    
                elif kterou == 3:
                    poleHrace.remove("3")
                    penize += 4
                    
                elif kterou == 4:
                    poleHrace.remove("4")
                    penize += 4
                    
                elif kterou == 5:
                    poleHrace.remove("5")
                    penize += 4
                    
                
                
            else:
                print("V tomto kole ještě není možné prodávat.")
#konec části s prodáváním    
#Toto přidává peníze hráči za počet budov postavených na políčkách podle čísla (*1 je tam z důvodu jednoduché úpravy pravidel)
    aktivniBudova = kostka.kostkaFunkce()
        
    if aktivniBudova == 1:
            budovy1 = poleHrace.count("1")
            penize += budovy1 * 1
        
    elif aktivniBudova == 2:
            budovy2 = poleHrace.count("2")
            penize += budovy2 * 1
        
    elif aktivniBudova == 3:
            budovy3 = poleHrace.count("3")
            penize += budovy3 * 1

    elif aktivniBudova == 4:
            budovy4 = poleHrace.count("4")
            penize += budovy4 * 1

    elif aktivniBudova == 5:
            budovy5 = poleHrace.count("5")
            penize += budovy5 * 1

        
    print(f"Na kostce padlo číslo {aktivniBudova}. Dostaneš tolik peněz, kolik máš na tomto číslu budov.\n Nyní máš {penize} peněz.")
#Při dosažení 75 peněz hra končí
    if penize >= 75 and cisloTahu <= 20:
        print(f"Gratuluji ,hru jsi vyhrál!\n Máš o {penize - 75} více peněz než bylo potřeba.\n Vyhrál jsi na tahu číslo {cisloTahu}.")
        exit()
    elif cisloTahu > 20 and penize < 75:
        print(f"Hra skončila.\n Ty jsi v ní ale prohrál!")
        exit()
    elif penize != 75 and cisloTahu <= 20:
        cisloTahu += 1
    
        
    #toto je na chození a zobrazení hráče na mapě
        MAP_WIDTH = 5
        MAP_HEIGHT = 5
        
        global hrac_x
        global hrac_y

        
        if cisloTahu <=20:
            
            
            for y in range(MAP_HEIGHT):
                for x in range(MAP_WIDTH):
                    if x == hrac_x and y == hrac_y:
                        print("H", end=" ")  
                    else:
                        print(".", end=" ")  
                print()  


            smer = input("Zadej smer (w/a/s/d): ")


            if smer == "w" and hrac_y > 0:
                hrac_y -= 1 
            elif smer == "a" and hrac_x > 0:
                hrac_x -= 1  
            elif smer == "s" and hrac_y < MAP_HEIGHT - 1:
                hrac_y += 1  
            elif smer == "d" and hrac_x < MAP_WIDTH - 1:
                hrac_x += 1 
        else:
            print("Hra skončila.")


    #Tady začíná samotný tah hráče, kdy může na políčku na kterém stojí postavit budovu, která mu bude generovat peníze do budoucna
        if hrac_x == 0 and hrac_y == 0:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("1")
                    penize -= 5
                else:
                    tah()
            else:
                tah()
        
        elif hrac_x == 1 and hrac_y == 0:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("3")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 2 and hrac_y == 0:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("5")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 3 and hrac_y == 0:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("4")
                    penize -= 5
                else:
                    tah()
            else:
                tah()
        
        elif hrac_x == 4 and hrac_y == 0:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("1")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 0 and hrac_y == 1:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("4")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 1 and hrac_y == 1:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("2")
                    penize -= 5
                else:
                    tah()
            else:
                tah()
        
        elif hrac_x == 2 and hrac_y == 1:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("2")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 3 and hrac_y == 1:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("3")
                    penize -= 5
                else:
                    tah()
            else:
                tah()
        
        elif hrac_x == 4 and hrac_y == 1:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("4")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 0 and hrac_y == 2:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("1")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 1 and hrac_y == 2:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("5")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 2 and hrac_y == 2:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("1")
                    penize -= 5
                else:
                    tah()
            else:
                tah()
        
        elif hrac_x == 3 and hrac_y == 2:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("2")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 4 and hrac_y == 2:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("5")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 0 and hrac_y == 3:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("2")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 1 and hrac_y == 3:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("4")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 2 and hrac_y == 3:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("3")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 3 and hrac_y == 3:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("4")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 4 and hrac_y == 3:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("1")
                    penize -= 5
                else:
                    tah()
            else:
                tah()
            
        elif hrac_x == 0 and hrac_y == 4:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("5")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 1 and hrac_y == 4:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("3")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 2 and hrac_y == 4:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("5")
                    penize -= 5
                else:
                    tah()
            else:
                tah()
        
        elif hrac_x == 3 and hrac_y == 4:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("3")
                    penize -= 5
                else:
                    tah()
            else:
                tah()

        elif hrac_x == 4 and hrac_y == 4:
            if penize >= 5:
                odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
                if odpoved == "a":
                    poleHrace.append("2")
                    penize -= 5
                else:
                    tah()
            else:
                tah()
    tah()

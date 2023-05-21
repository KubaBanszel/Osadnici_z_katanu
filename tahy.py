import kostka

penize = 0
poleHrace = []


hrac_x = 0
hrac_y = 0
cisoTahu = 1
def tah():
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

    else:
        print("Došlo k chybě programu, prosím vypni hru a zapni novou.")
    
    print(f"Na kastce padlo číslo {aktivniBudova}. Dostaneš tolik peněz, kolik máš na tomto číslu budov.\n Nyní máš {penize} peněz.")
#toto je na chození a zobrazení hráče na mapě
    MAP_WIDTH = 5
    MAP_HEIGHT = 5
    global cisoTahu
    global hrac_x
    global hrac_y

    
    if cisoTahu <=20:
        print(f"Jsi na tahu číslo {cisoTahu}")
        cisoTahu += 1
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
                poleHrace.append(1)
                penize -= 5
            else:
                tah()
        else:
            tah()
    
    elif hrac_x == 0 and hrac_y == 1:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(3)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 0 and hrac_y == 2:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(5)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 0 and hrac_y == 3:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(4)
                penize -= 5
            else:
                tah()
        else:
            tah()
    
    elif hrac_x == 0 and hrac_y == 4:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(1)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 1 and hrac_y == 0:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(4)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 1 and hrac_y == 1:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(2)
                penize -= 5
            else:
                tah()
        else:
            tah()
    
    elif hrac_x == 1 and hrac_y == 2:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(2)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 1 and hrac_y == 3:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(3)
                penize -= 5
            else:
                tah()
        else:
            tah()
    
    elif hrac_x == 1 and hrac_y == 4:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(4)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 2 and hrac_y == 0:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(1)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 2 and hrac_y == 1:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(5)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 2 and hrac_y == 2:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(1)
                penize -= 5
            else:
                tah()
        else:
            tah()
    
    elif hrac_x == 2 and hrac_y == 3:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(2)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 2 and hrac_y == 4:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(5)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 3 and hrac_y == 0:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(2)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 3 and hrac_y == 1:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(4)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 0 and hrac_y == 2:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(3)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 3 and hrac_y == 3:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(4)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 3 and hrac_y == 4:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(1)
                penize -= 5
            else:
                tah()
        else:
            tah()
        
    elif hrac_x == 4 and hrac_y == 0:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(5)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 4 and hrac_y == 1:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(3)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 4 and hrac_y == 2:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(5)
                penize -= 5
            else:
                tah()
        else:
            tah()
    
    elif hrac_x == 4 and hrac_y == 3:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(3)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x == 4 and hrac_y == 4:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(2)
                penize -= 5
            else:
                tah()
        else:
            tah()
            
    
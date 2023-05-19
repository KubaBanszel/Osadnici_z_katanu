import kostka

penize = 0
poleHrace = []


hrac_x = 0
hrac_y = 0
tah = 1
def tah():
#Toto přidává peníze hráči za počet budov postavených na políčkách podle čísla
    aktivníBudova = kostka.kostkaFunkce()
    if aktivníBudova == 1:
        budovy1 = poleHrace.count("1")
        penize += budovy1 * 1
    
    elif aktivníBudova == 2:
        budovy2 = poleHrace.count("2")
        penize += budovy2 * 1
    
    elif aktivníBudova == 3:
        budovy3 = poleHrace.count("3")
        penize += budovy3 * 1

    elif aktivníBudova == 4:
        budovy4 = poleHrace.count("4")
        penize += budovy4 * 1

    elif aktivníBudova == 5:
        budovy5 = poleHrace.count("5")
        penize += budovy5 * 1

    else:
        print("Došlo k chybě programu, prosím vypni hru a zapni novou.")
#toto je na chození hráče po mapě
    MAP_WIDTH = 5
    MAP_HEIGHT = 5
    global tah
    global hrac_x
    global hrac_y

    
    if tah <=20:
        print(f"Jsi na tahu číslo {tah}")
        tah += 1
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
        print("Již jsi dohrál")


#Tady začíná samotný tah hráče
    if hrac_x and hrac_y == 0:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(1)
                penize -= 5
            else:
                tah()
        else:
            tah()

    elif hrac_x and hrac_y == 1:
        if penize >= 5:
            odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
            if odpoved == "a":
                poleHrace.append(2)
                penize -= 5
            else:
                tah()
        else:
            tah()


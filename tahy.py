import kostka
import pohyb_hrace
import GAME

poleHrace = []

if hrac_x and hrac_y == 1:
    if penize >= 5:
        odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
        if odpoved == "a":
            poleHrace.append(1)
            penize -= 5
        else:
            pohyb()
            

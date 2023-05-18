import kostka
import pohyb_hrace
import GAME

poleHrace = []
pohyb_hrace.pohyb()
if hrac_x and hrac_y == 0:
    if penize >= 5:
        odpoved = input("Chceš si zde koupit budovu? Ano = a; Ne = n:")
        if odpoved == "a":
            poleHrace.append(1)
            penize -= 5
        else:
            pohyb()
    else:
        pohyb()

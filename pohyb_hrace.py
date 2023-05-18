
MAP_WIDTH = 5
MAP_HEIGHT = 5


hrac_x = 0
hrac_y = 0


while True:
   
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

    import os
    os.system("cls" if os.name == "nt" else "clear")

from rich.console import Console
import numpy as np

console = Console(width=20)

style = "bold black on blue"
console.print("Rich", style=style)
console.print("Hello", "World!", style=style)

#esempio stampa mappa
#genero mappa
map = np.zeros((5,5))
map[0][0] = 1
#ciclo sulle righe
for row in range(5):
    for col in range(5):
        cell = "_"
        if map[row][col] == 0:
            cell = '_'
        else:
            cell = 'X'
        print(cell, end=" ")
    #a fine riga vado a capo
    print("\n")
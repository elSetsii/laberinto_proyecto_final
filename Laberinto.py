import os
import time
#laberintos
laberintos = [ 
[ 
    [  # Nivel 1
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "P", " ", "#", " ", " ", " ", " ", "E", "#"],
        ["#", " ", "#", "#", " ", "#", "#", " ", " ", "#"],
        ["#", " ", "#", " ", " ", " ", "#", " ", "#", "#"],
        ["#", " ", "#", "#", "#", " ", "#", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", "#", " ", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
    ],
    [  # Nivel 2
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", "P", " ", " ", " ", " ", " ", "#", "E", "#"],
        ["#", " ", "#", "#", " ", " ", "#", " ", " ", "#"],
        ["#", " ", " ", " ", " ", "#", "#", "#", " ", "#"],
        ["#", "#", " ", "#", "#", " ", " ", " ", " ", "#"],
        ["#", " ", " ", " ", " ", " ", "#", "#", " ", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
    ]
]
tiempos = [40,35]
def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selecciona una opción:")
    for i in range(len(laberintos)):
        print(f"{i+1}. Nivel {i+1} (Tiempo límite: {tiempos[i]} segundos)")
    print("3. Salir")
    opcion = int(input("Elige un número (1-3): "))
    return opcion
    
def mostrar_laberinto(nivel, posicion, tiempo_restante):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Tiempo restante: {tiempo_restante:.1f} segundos (Presiona 'p' para pausar)")
    for i in range(len(laberintos[nivel])):
        fila = ""
        for j in range(len(laberintos[nivel][i])):
            if [i, j] == posicion:
                fila += "P "  
            else:
                fila += laberintos[nivel][i][j] + " "
        print(fila)

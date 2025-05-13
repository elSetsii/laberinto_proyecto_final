import os
import time

# Laberintos
laberintos = [ 
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
    ],
    [  # Nivel 3
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#"],
        ["#", "P", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ","E", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
    ]
]

tiempos = [40, 35, 45]

def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Selecciona una opción:")
    for i in range(len(laberintos)):
        print(f"{i+1}. Nivel {i+1} (Tiempo límite: {tiempos[i]} segundos)")
    print("4. Salir")
    
    while True:
        try:
            opcion = int(input("Elige un número (1-4): "))
            if 1 <= opcion <= 4:
                return opcion
            else:
                print("Por favor, elige un número válido (1-4).")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")

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

def mover(direccion, nivel, posicion):
    x, y = posicion
    if direccion == "w" and x > 0 and laberintos[nivel][x-1][y] != "#":
        x -= 1
    elif direccion == "s" and x < len(laberintos[nivel])-1 and laberintos[nivel][x+1][y] != "#":
        x += 1
    elif direccion == "a" and y > 0 and laberintos[nivel][x][y-1] != "#":
        y -= 1
    elif direccion == "d" and y < len(laberintos[nivel][0])-1 and laberintos[nivel][x][y+1] != "#":
        y += 1
    return [x, y]

def menu_pausa():
    print("\n**Juego en pausa**")
    print("1. Continuar")
    print("2. Reiniciar nivel")
    print("3. Volver al menú principal")
    while True:
        opcion = input("Selecciona una opción (1-3): ")
        if opcion in ("1", "2", "3"):
            return opcion
        else:
            print("Opción inválida. Elige 1, 2 o 3.")

# Bucle principal
while True:
    opcion = mostrar_menu()
    
    if opcion == 4:
        print("¡Gracias por jugar!")
        break

    nivel_actual = opcion - 1
    posicion = [1, 1]
    tiempo_limite = tiempos[nivel_actual]
    inicio = time.time()

    while laberintos[nivel_actual][posicion[0]][posicion[1]] != "E":
        tiempo_restante = tiempo_limite - (time.time() - inicio)

        if tiempo_restante <= 0:
            print("¡Tiempo agotado! Has perdido.")
            break

        mostrar_laberinto(nivel_actual, posicion, tiempo_restante)
        direccion = input("Movimiento (W/A/S/D/P para pausar): ").lower()

        if direccion == "p":
            opcion_pausa = menu_pausa()
            if opcion_pausa == "1":
                inicio = time.time() - (tiempo_limite - tiempo_restante)
                continue
            elif opcion_pausa == "2":
                posicion = [1, 1]
                inicio = time.time()
                continue
            elif opcion_pausa == "3":
                break  # vuelve al menú principal
        else:
            posicion = mover(direccion, nivel_actual, posicion)

    if laberintos[nivel_actual][posicion[0]][posicion[1]] == "E":
        print("¡Felicidades, encontraste la salida a tiempo!")

    input("Presiona Enter para volver al menú...")
    

import random
print("------------------------------------------------------")
print("   Bienvenido al Juego enfrentamiento de dados 🎲! ")
print("------------------------------------------------------")

J1 = input("Ingrese el nombre del PRIMER JUGADOR: ")
J2 = input("Ingrese el nombre del SEGUNDO JUGADOR: ")
input(f"{J1}, presiona Enter para lanzar el dado.")
lanzamientoJ1 = random.randint(1, 6)
print(f"{J1} sacaste {lanzamientoJ1}")
input(f"{J2}, presiona Enter para lanzar el dado.")
lanzamientoJ2 = random.randint(1, 6)
print(f"{J2} sacaste {lanzamientoJ2}")
if lanzamientoJ1 > lanzamientoJ2:
    print(f"El ganador es {J1}")
elif lanzamientoJ2 > lanzamientoJ1:
    print(f"El ganador es {J1}")
else:
    print(f"{J1} y {J2} empataron")
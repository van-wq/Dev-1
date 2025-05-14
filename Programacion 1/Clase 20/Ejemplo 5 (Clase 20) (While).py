i=0
tope=int(input("Ingrese cuanta veces desea Ejectuar el Control: "))
while i < tope:
    # Solicitar al usuario ingresar su edad
    edad = int(input("Ingrese edad: "))

    # Verificar si puede ver TV
    if edad >= 18:
        print("-- Puede ver TV")
    elif edad <= 17:
        print("--- No puedes ver TV")
    i=i+1

# Mensaje final indicando que se terminó el proceso
print()
print("Terminamos IF")
print()
# Solicitar al usuario ingresar su edad
edad = int(input("Ingrese edad: "))

# Verificar si puede ver TV
if edad >= 18:
    print("-- Puede ver TV")
elif edad <= 17:
    print("--- No puedes ver TV")

# Mensaje final indicando que se terminó el proceso
print()
print("Terminamos IF")
print()
# Inicializamos variables
peso = 0
altura = 0
imc = 0

# Solicitamos al usuario que ingrese datos
peso = float(input("Ingrese el peso (kg): "))
altura = float(input("Ingrese la altura (m): "))

# Calculamos el IMC
imc = peso / (altura * altura)

# Clasificamos el IMC
if imc < 19:
    print("Delgado")
elif 19 <= imc <= 25:
    print("Normal")
elif 26 <= imc <= 30:
    print("Sobrepeso")
else:
    print("Obesidad")
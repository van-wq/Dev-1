# Solicitar al usuario que ingrese los valores de los sueldos
juan_basico = float(input("Ingrese el sueldo básico de Juan: "))
pedro_basico = float(input("Ingrese el sueldo básico de Pedro: "))
maria_basico = float(input("Ingrese el sueldo básico de María: "))

# Solicitar al usuario que ingrese el presupuesto total disponible
presupuesto = float(input("Ingrese el presupuesto total disponible: "))

# Porcentajes de descuentos
obra_social = 0.03
jubilacion = 0.11

# Calcular sueldo neto de cada empleado
juan_neto = juan_basico - (juan_basico * obra_social) - (juan_basico * jubilacion)
pedro_neto = pedro_basico - (pedro_basico * obra_social) - (pedro_basico * jubilacion)
maria_neto = maria_basico - (maria_basico * obra_social) - (maria_basico * jubilacion)

# Sumar el total final de sueldos
total_sueldos = juan_neto + pedro_neto + maria_neto
resto=presupuesto - total_sueldos

# Verificar si alcanza el presupuesto
if total_sueldos <= presupuesto:
    print("Pagar")
    print(f"Total final a pagar: $ {total_sueldos:} y le quedan: ${resto}")
else:
    print("No alcanza")
    print(f"Total final a pagar: ${total_sueldos:} y Su Presupuesto es de: ${presupuesto}")
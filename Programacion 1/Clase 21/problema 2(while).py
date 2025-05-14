#Inicializar variables
i=0
total_sueldos=0
#Asignamos el Porcentaje de descuento
obra_social=0.03
jubilacion=0.11
#Solicitamos al Usuario que nos diga cuanto empleados tenemos
empleados=int(input("Ingrese la cantidad de Empleados: "))
presupuesto=float(input("Ingrese El prespuesto que tiene : "))
while i < empleados:
    #Solicitar al usuario que ingrese el sueldo
    sueldo=float(input("Ingrese el sueldo basico de un Empleado: "))
    #Calcular el sueldo basico de un empleado
    sueldo_neto=sueldo - (sueldo * obra_social) - (sueldo * jubilacion)
    #Acumular Sueldo 
    total_sueldos= total_sueldos + sueldo_neto
    i=i+1
#Calcular el resto del presupuesto
resto= presupuesto - total_sueldos
#Verificar si podemos pagar el sueldo
if total_sueldos <= presupuesto:
    print("Pagar")
    print(f"total final a pagar: ${total_sueldos} y quedan: ${resto}")
else:
    print("No Alcanza")
    print(f"total final a pagar: ${total_sueldos} y su presupuesto es de: ${presupuesto}")
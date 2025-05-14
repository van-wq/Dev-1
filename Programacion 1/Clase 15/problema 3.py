#Creado por Jorge Exequiel Lazarte Comision 2 
#Inicializar variables 
pHarina, pYerba, cantHarina, cantYerba, factura, factotal, iva= 0, 0, 0, 0, 0, 0, 0
#Pedimoos al usuario que ingrese el precio de la harina  y la yerba , lo guardo en tipo de variable float (porque puede ser decimal su precio)
pHarina=float(input("Ingrese el precio de la harina: "))
pYerba=float(input("Ingrese el precio de la yerba: "))
#Pedimos al usuario que ingrese la cantidad de harina y yerba que desea comprar , lo guardo en tipo de variable entero (son numeros enteros)
cantHarina=int(input("Ingrese la cantidad de harina que desea comprar: "))
cantYerba=int(input("Ingese La Cantidad de yerba que desea comprar: "))
#Calculamos el total de la factura
factura=(pHarina*cantHarina)+(pYerba*cantYerba)
#Calculamos el iva
iva=factura*0.21
#Calculamos el total de la factura
factotal=factura+iva
#Imprimimos el resultado de la factura
print("El total de la factura es: ",factotal)
print("El iva de la factura es: ",iva)
print("El total de la factura sin iva es: ", factura)
#Final del programa 
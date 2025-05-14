#Creado por Jorge Exequiel Lazarte Comision 2 
#Inicializamos las variables
cantCafe,cantAzucar, pCafe, pAzucar, GastGeneral= 0,0,0,0,0
#Pedimos al usuario que ingrese la cantidad de cafe,azucar y sus precios lo guardo en variable (cantCafe y cantAzucar) de tipo entero (cantidad son entero)
cantCafe=int(input("Ingrese la cantidad de cafe: "))
cantAzucar=int(input("Ingrese la cantidad de azucar: "))
#Pedimos al usuario que ingrese el precio de Azucar y Cafe lo guardo en variable (pAzucar y pCafe) de tipo float (puede ser decimal su precio)
pAzucar=float(input("Ingrese el precio del azucar: "))
pCafe=float(input("Ingrese el precio del cafe: "))
#Calculamos el gasto total
GastGeneral=(cantCafe*pCafe)+(cantAzucar*pAzucar)
#Imprimimos el resultado
print("El gasto total es: ",GastGeneral)
#Fin del programa
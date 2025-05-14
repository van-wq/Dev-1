#Creado por Jorge Exequiel Lazarte Comision 2 
#Inicializamos Las variables           
#N1, N2, N3, N4, N5 son los cinco numeros enteros
N1, N2, N3, N4, N5, NT, P, M = 0, 0, 0, 0, 0, 0, 0 , 0
#Pedimos al usuario que ingrese los cinco numeros enteros y por cuandoto desea multiplicar el promedio
print("Ingrese cinco numeros enteros")
N1=int(input("Ingrese el primer numero: "))
N2=int(input("Ingrese el segundo numero: "))
N3=int(input("Ingrese el tercer numero: "))
N4=int(input("Ingrese el cuarto numero: "))
N5=int(input("Ingrese el quinto numero: "))
print("Por cuandoto desea multiplicar el promedio de los cinco numeros enteros")
M=int(input("Ingrese el numero: "))    
#Sumamos los cinco numeros enteros y los almacenamos en la variable NT
NT=N1+N2+N3+N4+N5
#Calculamos el promedio de los cinco numeros enteros y lo almacenamos en la variable P
P=NT*M
#Imprimimos el resultado de la suma y el promedio
print("La suma de los cinco numeros es: ",NT)
print("El promedio de los cinco numeros es: ",P)	
#Fin del programa

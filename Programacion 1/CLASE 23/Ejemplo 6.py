#Jorge Exequiel Lazarte C2
#Importamos Libreraria para interactura con el sistema operativo
import os
#Asignamos valor a la variable estado
estado= "S"
#Mientras Estado="S" Nuestro Programa Continua
while (estado=="S"):
    try:
        #Solicitamos dato al usuario
        n1=int(input("Ingrese el Primero Numero: "))
        n2=int(input("Ingrese el Segundo Numero: "))
        R= n1 * n2
        #Imprimo Resultado
        print(R)
        #Preguntamos si desea continuar o Salir del Programa Lo hacemos mediante la funcion break
        estado=input("Desea continuar? S/N?")
        if estado== "N":
            print("Bye Bye")
            break
        #Limpiamos la pantalla para una nueva operacion
        os.system("cls")
    #Controlar el margen de error    
    except:
        print("Debe Ingresar un nro: ")
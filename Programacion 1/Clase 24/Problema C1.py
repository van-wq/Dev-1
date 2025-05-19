#Importo Libreria para limpiar pantalla
import os
#Asigno Valores a la Variables 
No_Contable=0
contable=0
Categoria_A=0
estado="S"
#Mientras Estado="S"
while (estado=="S"):
    try:
        #Solicitamos datos al Usuario 
        sector=str(input("Ingrese El Sector (CON MAYUS): "))
        categoria=str(input("Ingrese Su Categoria(CON MAYUS): "))
        #Comparamos los sectores para ver si Ingresan
        if sector == "CONTABLE" and categoria== "A":
            print("Ingresa")
            contable=contable+1
            Categoria_A=Categoria_A+1
        else:
            print("No Ingresa")
        estado=input("Desea Continuar? S/N?: ")
        if estado=="N":
            print("Good Bye")
            break
        #Limpiamos pantalla con la Funcion cls
        os.system("cls")
    except:
        print("Por favor Ingrese un Sector: ")

#Imprimir Texto En Pantalla
print("-------------------------------")
print("Ingresaron por el sector Contable: ",contable)
print("Ingresaron por el Sector A: ",Categoria_A)
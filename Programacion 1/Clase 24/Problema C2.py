#Importamos libreria para interactura con el sistema operativo
import os
#Asigno valores a las variables
BONOA=0
BONOB=0
BONO0=0
estado="S"
while (estado=="S"):
    try:
        #Solicitamos datos al Usuario
        edad=int(input("Ingrese su Edad: "))
        localidad=str(input("Ingrese su localidad (CON MAYUS): "))
        #Comparamos los resultados con las condiciones
        if edad== 21 and localidad== "CONCEPCION":
            print("BONO 50 OTORGADO!")
            BONOA=BONOA+1

        elif edad > 21:
            print("Mayor de Edad bono no Otorgado!")
            BONO0=BONO0+1
        if edad < 21:
            print("BONO 10 OTORGADO! ")
            BONOB=BONOB+1
        estado=input("Desea Continuar? (S)/(N)?:")
        if estado=="N":
            print("Good Bye")
            break
        #limpiamos pantalla en cada proceso 
        os.system("cls")
    except:
        print("Por favor Ingresar una Edad: ")
#texto
informe=f""" 
{BONOA} FUERON  DE 50.000
{BONOB} FUERON  DE 10.000
{BONO0} FUERON RECHAZADO POR NO CUMPLIR REQUISITOS!"""
#Imprimo en pantalla
print("---------------------------------")
print(informe)
#Inicializo las variables 
i=0
Contable=0
No_contable=0
#Solicito al usuario que me diga cuanta veces quiero que recorra el codigo
int=int(input("Ingrese La Cantidad de Empleados: "))
while i < int:
    #Solicito datos de sector y categoria POR FAVOR RESPECTAR EL INGRESO DE DATOS CUANDO ESPECIFIQUE QUE ES CON MAYUSCULA
    sector=str(input("Ingrese Si Es Sector (CON MAYUS): "))
    categoria=str(input("Ingrese Su Categoria (CON MAYUS): "))
    #Comparo si los datos son lo solicito , muestro resultado e incremento mi contador de variables 
    if sector == "CONTABLE" and categoria== "A":
        print("Ingresa")
        Contable=Contable+1
    else:
        print("No Ingresa")
        No_contable=No_contable+1
    #Incremento contador 
    i=i+1
#Creo 1 texto para mostra 1 mensaje de salida de manera estructurada con la funcion de cadenas de texto (f """")
Informe=f""" 
Ingresaron La Cantidad de {i} Empleados
{Contable} CATEGORIA A
{No_contable}  CATEGORIA B"""
#Imprimo en pantalla los resultado
print("---------------------------------------------------------------------")
print(Informe)

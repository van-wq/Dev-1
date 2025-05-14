#Inicializar las variables 
i=0
BONOA=0
BONOB=0
BONO0=0
#Solicito al usuario que me diga cuanta veces quiero que corra y lo guardo en la variables intentos
intentos=int(input("Ingresar La Cantidad Para Otorgar Bono: "))
while i < intentos:
    #Solicitamos datos que nos indica el problema "Edad" y "Cuidad" POR FAVOR RESPECTAR EL INGRESO DE DATOS CUANDO ESPECIFIQUE QUE ES CON MAYUSCULA
    edad=int(input("Ingrese Su Edad: "))
    localidad=str(input("Ingrese Su Localidad (CON MAYUSC): "))
    #Comparamos los resultado con las condiciones que no piden 
    if edad == 21 and localidad== "CONCEPCION":
        print("BONO 50 OTORGADO !")
        BONOA=BONOA+1
    elif edad > 21:
        print("Mayor de Edad Bono no Otorgado! ")
        BONO0=BONO0+1
    if edad < 21:
        print("BONO 10 OTORGADO! ")
        BONOB=BONOB+1
    #Incrementamos nuestro contador 
    i=i+1
#Creo 1 texto  en la variable informe 
informe=f""" 
SE OTORGARON {intentos} BONOS
{BONOA} FUERON  DE 50.000
{BONOB} FUERON  DE 10.000
{BONO0} FUERON RECHAZADO POR NO CUMPLIR REQUISITOS!"""
#Imprimo en pantalla mi informe creado en el paso Anterior
print("---------------------------------------------------------------------------------")
print(informe)
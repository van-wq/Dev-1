n1=input("Ingrese el 1º Nro")
n2=input("Ingrese el 2º Nro")
print(n1,n2)
#----------------------
n1=int(n1)
n2=int(n2)
suma=n1+n2
resta=n1-n2
Multiplicacion=n1*n2
Division=n1/n2
Mensaje= f""" el resultado de 4 operaciones con {n1} y {n2}
es el Siguiente:
La Suma es:{suma}
La Resta es:{resta}
El Producto es:{Multiplicacion}
La Division es:{Division}"""
print(Mensaje)
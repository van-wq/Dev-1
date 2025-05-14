nombre="Jorge Exequiel"
apellido="Lazarte"
#se aplicar Format o con minúsculas la f siempre entre comillas y llaves para concatenar
nombre_completo=f"{nombre} {apellido}"
print(nombre_completo)
print("------------------------------------------------")
n1=input("ingrese el primer nro: ")
n2=input("ingrese el segundo nro: ")
# esto concatena pero no suma nros
print(n1 + n2)
# ahora debemos aplicar tipo de dato
n1=int(n1)
n2=int(n2)
suma=n1+n2
resta=n1-n2
multi=n1*n2
div=n1/n2
mensaje=f"""
el resultado
de cuatro operaciones con {n1} y {n2} es el siguiente:
la suma es : {suma}
la resta es: {resta}
el producto es : {multi}
la división es: {div}"""
print(mensaje)
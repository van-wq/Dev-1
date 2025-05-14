#Clase 21 Jorge Exequiel Lazarte
#Asignamos valores al contador y pedimos al usuario que ingrese Un Tope
i=0
Tope=int(input("Ingrese La Cantidad de Persona que van a Comprar: "))
while i < Tope:
#Pedimos al usuario que Ingrese Valores
    fondos=float(input("Ingrese su presupuesto: "))
    cant_roja=int(input("Ingrese la cantidad de lapiceras Roja: "))
    prec_roja=float(input("Ingrese el precio c/u de lapicera Roja: "))
    cant_verde=int(input("Ingrese la cantidad de lapiceras verde: "))
    prec_verde=float(input("Ingrese el precio c/u de lapiceras verde: "))
    cant_azul=int(input("Ingrese la cantidad de lapiceras Azul: "))
    prec_azul=float(input("Ingrese el precio c/u de lapiceras Azul: "))
#Calculamos el gasto total de cada Lapicera
    total_roja=cant_roja*prec_roja
    total_verde=cant_verde*prec_verde
    total_azul=cant_azul*prec_azul
#Calculamos La factura sin iva y factura total con Iva
    factura=total_azul+total_roja+total_verde
    iva= (factura*21)/100
    factura_total=factura+iva
#Mensaje de Ticket
    ticket=f""" Su Factura a pagar es de : {factura_total}
    Lapiceras Roja x {cant_roja} por $ {prec_roja} C/U
    Lapiceras Verd x {cant_verde} por $ {prec_verde} C/U
    Lapiceras Azul x {cant_azul} por ${prec_azul} C/U
    IVA ${iva}"""
    if factura_total <= fondos:
        print("Confirmar Compra", factura_total)
        print(ticket)
    else: 
        print("Cancelar Compra")
    i=i+1
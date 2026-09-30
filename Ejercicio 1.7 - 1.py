# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

Total_compra=float(input("Ingrese el valor total de la compra: "))

#aplicamos el descuento que da la tienda
porcentaje_descuento=Total_compra*0.15
Total_compra-=porcentaje_descuento

print(f"El total a pagar de la compra es: {Total_compra:.2f}")
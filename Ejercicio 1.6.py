sueldo_base=float(input("Ingrese el sueldo base del individuo: "))

#Un vendedor recibe un sueldo base, mas un 10% extra por comisión de sus ventas, el vendedor uesea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

ventasxmes=36
i=0

while i<ventasxmes:
    suma_por_comision=sueldo_base*0.10
    sueldo_base+=suma_por_comision
    i+=1

#paga de lo invertido 15% al año
porcentaje_sueldo=sueldo_base*0.15

dinero_ganado=sueldo_base+porcentaje_sueldo

print(f"El dinero ganado al invertir todo el sueldo, dentro de un año ganaria: {dinero_ganado:.2f}")
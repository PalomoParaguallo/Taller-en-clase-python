# Dada una cantidad en pesos, obtener la equivalencia en dólares, 
# asumiendo que la unidad cambiaría a un dato desconocido.

cantidad_colombianos=float(input("Ingrese el valor en pesos colombianos que desea convertir: "))

precio_dollar=float(input("Ingrese el valor actual del dollar en pesos colombianos: "))

equivalencia=cantidad_colombianos/precio_dollar

print(f"La cantidad de en dolares de lo ingresado es de: {equivalencia:.2f} dolares")
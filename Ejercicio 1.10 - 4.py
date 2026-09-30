# Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de 
# ejercicio, si la fórmula es: numPulsaciones = (220 - edad)/10

edad = float(input("Ingrese la edad de la persona de la cual desea calcular su numero de pulsaciones: "))

numPulsaciones = (220 - edad)/10

print(f"El numero de pulsaciones de esta persona deberia ser aproximadamente de: {numPulsaciones:.0f} pulsaciones por segundo")
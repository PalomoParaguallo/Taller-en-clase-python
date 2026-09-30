# La presión, el volumen y la temperatura de una masa de aire se relacionan por la fórmula: 
# masa = (presión * volumen)/(0.37 * (temperatura + 460))

presion = float(input("Ingresa la presion: "))
volumen = float(input("Ingresa el volumen: "))
temperatura = float(input("Ingresa la temperatura: "))

masa = (presion * volumen)/(0.37*(temperatura + 460))

print("La masa es:", masa)

# Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
# #Dicha calificación se compone de los siguientes porcentajes: 40% del promedio de sus 
# tres calificaciones parciales, 50% de la calificación del examen final y 10% de la 
# calificación de un trabajo final.

calificacion1=float(input("Ingrese la primera nota parcial: "))
calificacion2=float(input("Ingrese la segunda nota parcial: "))
calificacion3=float(input("Ingrese la tercera nota parcial: "))

promedio_parciales=(calificacion1+calificacion2+calificacion3)/3

# ahora la segunda nota, 50% calificacion examen final
examen_final=float(input("Ingrese la nota del examen final: "))

# la tercera nota, 10%
trabajo_final=float(input("Ingrese la calificacion del trabajo final: "))

#Calculamos los valores
Calificacion_final=(promedio_parciales*0.40)+(examen_final*0.50)+(trabajo_final*0.10)

print(f"\nLa calificaion final es de: {Calificacion_final:.2f}")
#propositos para hoy...
# comprender como se manejan los arreglos en python
# realizar operaciones basicoas y algunas avanzadas para resolver problemas de la vida cotidiana.
# aplicar logica de programación para manipular datos almacenados en arreglos.

#Conceptos Fundamentales del tema de los arreglos.

# 1 ¿Que es un arreglo?
# es una forma de estructurar datos que almacena una secuencia de elementos de forma consecutiva.
# Cada elemento se puede encontrar por medio de su indice. (el indice de cada arreglo comienza desde cero.)

#2 Uso comun de los vectores / arreglo / lista / array.
# guarda datos relacionados como nombres, numeros o resultados.
# procesar grandes cantidades de informacion, esto de forma ordenada.

#3 operaciones basicas:
# crear y llenar
# recorrer y manipular datos
# realizar busquedas, filtros y transformaciones.


#Ejemplos detallados
#  crear y mostrar un vector.

vector = []

#vamos a llenar el vector por valores definidos por el usuario.
for i in range(5):
    valor = int(input(f"ingrese un numero para la posicion {i}: "))
    vector.append(valor) #.append es una funcion interna de python que recibe como parametro lo que se va a agregar a un arreglo y lo coloca en la ultima posicion disponible.
print(f"Arreglo ingresado: {vector}")

# Ejercicio 1: Registro de Temperaturas
# Problema: Crea un programa que:

# Solicite al usuario registrar las temperaturas de los últimos 7 días.
# Muestre:
# La temperatura promedio.
# El día con la temperatura más alta.
# El día con la temperatura más baja.

#crear un arreglo para almacenar las temperaturas
temperaturas = []

# llenamos el arreglo
for i in range(7):
    temp = float(input(f"Ingrese la temperatura del dia {i + 1 }: "))
    temperaturas.append(temp)

#calculamos el promedio
promedio = sum(temperaturas) / len(temperaturas)

# encontramos maximos y minimos.
max_temp = max(temperaturas)
min_temp = min(temperaturas)

#imprimir los resultados
print(f"Temperaturas registradas: {temperaturas}")
print(f"Promedio de temeperatura: {promedio:.2f} grados")
print(f"Temperatura mas alta: {max_temp} grados fue el dia {temperaturas.index(max_temp) + 1}")
print(f"Temperatura mas baja: {min_temp} grados fue el dia {temperaturas.index(min_temp) + 1}")

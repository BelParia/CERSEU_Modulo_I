# Ejercicio 3
"""
3. Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado insertados en
la terminal
"""

lista = []
lista.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
suma_valores = lista[0]+lista[1]+lista[2]+lista[3]+lista[4]+lista[5]+lista[6]+lista[7]+lista[8]+lista[9]
media_valores = suma_valores/len(lista)
print(f"La suma de los valores de la lista es {suma_valores}")
print(f"La media de los valores de la lista es {media_valores}")

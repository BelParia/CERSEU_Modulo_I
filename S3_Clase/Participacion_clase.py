"""
Requisitos:
- Crear dos listas vacías
- Agregar los datos de nombre, apellido paterno, edad y profesión para ambas listas
- Obtener y mostrar la suma de las edades de ambas listas
- Sumar las listas y mostrar el resultado en la terminar
- Mostrar de forma inversa la suma de ambas listas
- Actualizar la nueva lista eliminando la edad de la primera y el apellido del segundo
(Utilizar cualquiera de los métodos de eliminación)
"""

# Definir variables
lista1 = []
lista2 = []
lista1.extend(["Brayan", "de la Cruz", 24, "Biólogo"])
lista2.extend(["Piero", "Carillo", 23, "Biotegnólogo"])

# Suma de edades
print(f"La suma de edades de ambas listas es: {lista1[2] + lista2[2]}")

# Suma de listas
suma_listas = lista1 + lista2
print(f"La suma de las listas: {suma_listas}")

# Suma inversa de las listas
suma_listas.reverse()
print(f"La suma inversa de las listas: {suma_listas}")

# Actualización de listas
del lista1[2]  # elimina la edad
del lista2[1]  # elimina el apellido
print(lista2)
lista2[2] = "Arquitecto"  # actualizamos la profesión

print(f"Primera lista actualizada: {lista1}")
print(f"Segunda lista actualizada: {lista2}")
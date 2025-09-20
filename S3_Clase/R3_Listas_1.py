# Ejercicio 1
"""
1. Escribir un programa donde ingresarás el tamaño de la lista mediante consola,
este tamaño servirá para ingresar una cantidad X de nombres de alumnos.
Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de la
lista que fueron ingresados.
"""

print("*** Lista de alumnos ***")
tamanio_lista = int(input("Indique el tamaño de la lista de alumnos: "))
lista_alumnos = []
nombres_de_lista = ""
print(f"\nLa cantidad de nombres a escribir en la lista es {tamanio_lista}\n"
      f"No escriba más por favor, ya que de lo contrario la lista no se generará\n")
if tamanio_lista:
    nombres_alumnos = input("Escriba el nombre de los alumnos, separados por un espacio: ")
    lista_alumnos.extend([nombres_alumnos])
    nombres_de_lista = lista_alumnos[0].split(" ")
    if len(nombres_de_lista) > tamanio_lista:
        print(f"\nTe dije que no se generaría la lista, ya que son {len(nombres_de_lista)} nombres\n"
              f"pero indicaste al inicio que escribirías un total de {tamanio_lista}.")
        lista_alumnos = []
    else:
        print(f"\nEl tamaño de la lista es {len(nombres_de_lista)} y los nombres son {", ".join(nombres_de_lista)}")
else:
    print("\nDigita un número entero, por favor")

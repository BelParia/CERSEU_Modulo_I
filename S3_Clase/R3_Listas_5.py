# Ejercicio 5
"""
5. Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
datos mediante consola también (5 compañías relacionadas con al mundo de TI)
y harás una copia donde adrede agregarás nombres que estarán repetidos
(mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también te mostrará la lista inicial
"""

## Variables iniciales
print("*** Busqueda de información de compañias de TI ***")
tamanio_lista = int(input("Indique el tamaño de la lista: "))
nombres_companias = input(f"Indique {tamanio_lista} nombres de compañias, separadas por un espacio: ")
nombres_companias = nombres_companias.split(" ")
print("Cargando...\n")
print("Si quiere una busqueda profunda de las compañias,")
print("por favor, indique cuáles quieres que sean buscados,\n"
      "de manera más completa.\n")

## Variables afín a las copias
lista_con_copias = input("Nombre de compañias: ")  # literalmente serán copias
lista_con_copias = lista_con_copias.split(" ")
lista_copiada = nombres_companias.copy()  # la lista copia de la primera lista
lista_copiada.extend(lista_con_copias) # lista con copias adredes

# Flujos condicionales
if tamanio_lista <= len(nombres_companias):
# Filtrar nombres únicos (no repetidos en lista_con_copias)
    nombres_no_repetidos = []
    for nombre in nombres_companias:
        if nombre not in lista_con_copias:
            nombres_no_repetidos.append(nombre)
    print(f"Los siguientes comañias no fueron consideraras para la busqueda completa: {" ".join(nombres_no_repetidos)}")

    print(f"\nLa lista de las compañias que fueron buscadas inicialmente fueron:\n"
          f"{", ".join(nombres_companias)}")
else:
    print("Por favor, escribe la cantidad de nombres en relación al tamaño de la lista")


## Observaciones
"""
Profesor, no llegué a entender lo de "(5 compañías relacionadas con al mundo de TI)", ya que
tengo entendido que el tamaño de la lista, la que se pido al inicio, es la que decidirá cuantos
elementos deberá tener la lista inicial. Ahora, es posible entender tambien que esas 5 compañias
deben ser agregadas a la lista inicial debido a la copia adrede, pero se supone que es el usuario
quien debe realizar el proceso, si lo hacemos nosotros estariamos interrumpiendo el "flujo". Frente
a esto consideré simplemente hacer un llamado a "Busqueda profunda de información de las compañias".
De esta manera el usuario tiene prevalencia por elegir cual será la copia, y si escribe lo mismo que
el inicio, pues no se mostará nada con respecto a los no repetidos, y la lista inicial seguirá siendo
la misma con un mensaje afin a lo mencionado anteriormente. Además, no encontré manera de realizar 
esta actividad sin usar a las funciones iterativas, como While, for, filter, map, entre otros; por
lo que me vi forzado a usar un for, espero comprenda la situación, y si realmente hay una manera de 
hacerlo sin un iterativo, me gustaría saberlo y tal vez podría ennviarme un mensaje sobre el mismo 
por el correo de gmail. De ante mano, muchas gracias.
"""
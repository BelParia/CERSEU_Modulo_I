# Ejercicio 1
"""
1. El valor de ‘¡HI TuNombre Apellido!’ imprimirlo en consola, el texto
debe ser un string y deberás guardarlo en una variable llamada mi_saludo.
Tu nombre completo debe estar en otra variable.
"""

# Ejercicio 1
print("*** Convertir de soles a dolares ***\n")
monto_1 = 110
monto_2 = 220
monto_3 = 330
tipo_cambio = 0.29  ## es el tipo de cambio en el 19/09/2025
print(f"Los S/ {monto_1}, con el tipo de cambio de {tipo_cambio}, es igual a $ {(monto_1*tipo_cambio):.2f}")
print(f"Los S/ {monto_2}, con el tipo de cambio de {tipo_cambio}, es igual a $ {(monto_2*tipo_cambio):.2f}")
print(f"Los S/ {monto_3}, con el tipo de cambio de {tipo_cambio}, es igual a $ {(monto_3*tipo_cambio):.2f}")

# Ejercicio 2
print("*** Calculadora de Índice de Masa Corporal ***\n")
nombre_usuario = "Brayan de la Cruz"
peso_usuario = 71
altura_usuario = 1.69
indice_masa_corporal = peso_usuario/pow(altura_usuario, 2)
categoria = ""
if indice_masa_corporal < 18.5:
    categoria = "Bajo"
elif 18.5 <= indice_masa_corporal <=25:
    categoria = "Normal"
elif 25 < indice_masa_corporal <= 30:
    categoria = "Sobrepeso"
    print("Cambia tu dieta, ejercitate a menudo. Tu puedes.")
else:
    categoria = "Obeso"
    print("Cambia tu dieta, ejercitate a menudo. Tu puedes.")
print(f"{nombre_usuario}, usted posee un IMC igual a {indice_masa_corporal:.1f},\n"
      f"asi que se encuentra en el grupo {categoria}")

# Ejercicio 3
flotante1 = 3.4
flotante2 = 5.6
entero1 = int(flotante1)
entero2 = int(flotante2)
if entero1%entero2 == 0:
    print(f"El primer número ({entero1} es múltiplo de {entero2})")
else:
    print(f"El primer número ({entero1} no es múltiplo de {entero2})")

# Ejercicio 4
numero_decimal6 = 1.234567
print(f"Número flotante con 1 decimal: {numero_decimal6:.1f}")
print(f"Número flotante con 2 decimal: {numero_decimal6:.2f}")
print(f"Número flotante con 1 decimal: {numero_decimal6:.4f}")

# Listas Ejercicio 1
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


# Listas Ejercicio 2
lista_departamentos = ["Depa1", "Depa2", "Depa3", "Depa4", "Depa5", "Depa6"]
print(lista_departamentos)
print("Todos esos son los departamentos disponibles")
eleccion_departamento = input("\nElija 2 departamentos, separalos por un espacio: ")
primer_depa_lista = eleccion_departamento.split(" ")
lista_departamentos[0] = primer_depa_lista[1]
print(lista_departamentos)

# Listas Ejercicio 3
lista = []
lista.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
suma_valores = lista[0]+lista[1]+lista[2]+lista[3]+lista[4]+lista[5]+lista[6]+lista[7]+lista[8]+lista[9]
media_valores = suma_valores/len(lista)

# Listas Ejercicio 4
lista_nombres = ["Brayan", "Roly", "Mirian", "Carlos", "Ian"]
nombre_elegido = input("Ingrese el nombre de un estudiante: ")
if nombre_elegido in lista_nombres:
    lista_nombres.remove(nombre_elegido)
    print(f"El nombre de {nombre_elegido} será eliminado")
    print(f"La lista actualizada es {lista_nombres}")
else:
    lista_nombres.append(nombre_elegido)
    print(f"El nombre que indicaste ({nombre_elegido}) no está en la\n"
          f"lista general, asi que será añadida a la lista:\n"
          f"{lista_nombres}")


# Listas Ejercicio 5

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

## Flujos condicionales
if tamanio_lista <= len(nombres_companias):
## Filtrar nombres únicos (no repetidos en lista_con_copias)
    nombres_no_repetidos = []
    for nombre in nombres_companias:
        if nombre not in lista_con_copias:
            nombres_no_repetidos.append(nombre)
    print(f"Los siguientes comañias no fueron consideraras para la busqueda completa: {" ".join(nombres_no_repetidos)}")

    print(f"\nLa lista de las compañias que fueron buscadas inicialmente fueron:\n"
          f"{", ".join(nombres_companias)}")
else:
    print("Por favor, escribe la cantidad de nombres en relación al tamaño de la lista")

## Variables afín a las copias
lista_con_copias = input("Nombre de compañias: ")  # literalmente serán copias
lista_con_copias = lista_con_copias.split(" ")
lista_copiada = nombres_companias.copy()  # la lista copia de la primera lista
lista_copiada.extend(lista_con_copias) # lista con copias adredes

## Flujos condicionales
if tamanio_lista <= len(nombres_companias):
## Filtrar nombres únicos (no repetidos en lista_con_copias)
    nombres_no_repetidos = []
    for nombre in nombres_companias:
        if nombre not in lista_con_copias:
            nombres_no_repetidos.append(nombre)
    print(f"Los siguientes comañias no fueron consideraras para la busqueda completa: {" ".join(nombres_no_repetidos)}")

    print(f"\nLa lista de las compañias que fueron buscadas inicialmente fueron:\n"
          f"{", ".join(nombres_companias)}")
else:
    print("Por favor, escribe la cantidad de nombres en relación al tamaño de la lista")


# Listas Ejercicio 6
guests = ["Ana", "Katherine", "Pedro", "Luis", "Raúl", "Fiorella", "Miguel"]

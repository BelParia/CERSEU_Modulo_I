# Ejercicio 20

"""
Intervención

Requisitos:
- Crear una función la cuál va a evaluar una lista y un índice
- Habrá una exepción donde dentro de la función que sa a considerar
una lista con 4 valores
- Cuando se va a modificar una de las posiciones no existentes
crear un nuevo índice y darle un valor de 0
- Mostrar la lista final
"""

def evaluar_lista(lista, indice):
    if len(lista) > 4:
        raise IndexError(f"Por favor no digite listas con más de 4 elementos.\n"
                         f"Su lista posee {len(lista)} elementos")
    return lista[indice]

try:
    print("* Para evaluar la lista y cambiar algún elemento, no digite más de 4 elementos *\n")
    supuesta_lista = input("Indique los elementos de sus lista, porfavor sepárelos por un espacio:\n")
    lista_inicial = supuesta_lista.split()
    poner_indice = int(input("Indique el indice a modificar: "))
    evaluar_lista(lista_inicial, poner_indice)
    modificar = input("Indique que palabra o número debe reemplazar a tal índice: ")
    if poner_indice > (len(lista_inicial)-1):
        print(f"El elemento {modificar} no puede ser modificado por que el índice {poner_indice}\n"
              f"esta fuera de la longitud limitada: solo 4 elementos por lista")
        lista_inicial.append("0")
        print(f"\nDebido a que no hizo caso del límite, se le añadira un valor cero a\n"
              f"su lista. La nueva lista es {lista_inicial}")
    lista_inicial[poner_indice] = modificar
    print(f"Esta es la nueva lista: {lista_inicial}")
except IndexError as error:
    print(f"Lista pasa límite: {error}")
finally:
    print("\nEl proceso de validación de lista ha terminado. Vuelva pronto")

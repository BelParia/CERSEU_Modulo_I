# Clase Listas

"""
Las listas son un tipo de variable que permite 'guardar' varios tipos de variables,
parece extraño, pero relamente pueden contener cualquier elemento dentro, basta que
las codifiques como lista, y listo.
Cada elemento dentro de una lista se encuentra indexado, como si fuera un string.
Asi que si tienes una lista (["Pepito", "Lucho", "Toño"]) el primer elemento de esa
lista es Pepito, y se cuentra indexado con el valor de "0"; el siguiente, Lucho con
el valor de "1" y toño, "3". Pero existe la posibilidad de un indexado inverso, es
igualmente numérico pero con valores negativos, por lo que comienza desde la derecha
hacia la izquierda: comenzando con un -1 y no con el típico "0".
["Pepito", "Lucho", "Toño"]
    0         1        2
   -3        -2       -1

OJO, OJO, OJO. Practicamente todas las siguientes fuciones no te permiten guardarla en
una nueva lista, asi que considera ejecutarlas en una fila nada más, no agregues en otras
actividades, solo hazla separadas, para evitar errores. Eso es lo que sé hasta el momento
"""
## Códigos usados en lista
"""
-variable[index]: te permite elegir específicamente a un elemento de una lista, recuerda que es un indexado
-sumar listas: simplemente un 'lista1 + lista2', y literalmente las une en ese orden
- string.split(): si tienes un string que posea varios elementos dentro y separados por algún caracter,
puedes separarlos en base a ese caracter y generar una lista por defecto. Mira el R3_Listas_1.py

-len(variable): es una código usado en variables que contienen strings, simplemente cuenta el
número caracteres o elementos, según se el tipo de variable.
-variable.count(): cantidad de veces que se repite un elemento dentro de una lista

-variable.append(elemento): te permite añadir un solo elemento dentro de tu lista
-variable.extend(elementos): te permite añadir muchos elementos (pero dentro de []) dentro de una lista,
pero no lo puedes igualar a otra lista, muy raro lo sé, pero es así
-variable.insert(index,elemento): añadir un elemento en una posición expecífica. Esta es muy buena

-variable.pop(index): quitar un elemento de un posición dada, pero si no pones un index simplemente
te arroja el último elemento de la lista
-del variable[index]: este es el más usado para eliminar elementos en base al index de una lista
-variable.remove(elemento): elimina un elemento de la lista, pero tienes que indicar específicamente
-variable.clear(): te permite limpiar todo elemento dentro de una lista

-variable.reverse(): es un comando único que no necesita y no debe estar guardado en una varible
simplemente ejecuta y literalmente cambia el orden, no es un por un solo momento, sino todo el
código que esta delante, es un tanto complejo de ver, pero ya te acostumbraras.
-variable[::-1]: revierte la lista y lo puedes guardar en una nueva variable, no es como el '.reverse()'

-variable.sort(): ordena los elementos de una lista, si es un número pues va de menor a mayor; si
son strings, pues va en orden alfabético
-variable.copy(): solo funciona dentro de una nueva lista, no sé que de difente tiene con simplemente
igual una variable nueva y la otra que quieres que sea igual -> lista_nueva = lista_antigua
"""

##

# Funciones
"""
Te permiten literalmente crear nuevas funciones desde cero en Python, puedes hacer cualquier tipos de funciones
que necesites, incluso disponer funciones dentro de funciones. De esta menra interas varias características dentro
de otras. Ayuda mucho al momento de no crear código desde cero, sino que una vez realizado con algún objetivo
específico, por lo que si quieres modificarlo puedes hacerlo de acuerdo a tus interes.
Pero considera siempre que debes resolver el objetivo de la función con un 'return'.

Cuando una función ejecuta 'return', se detiene inmediatamente y entrega el valor especificado. Ese valor puede
ser un número, una cadena, una lista, un objeto… lo que sea.
"""

## Comando único
"""
El único comando es 
def nombre_función(nvariables):
    códigos a ejecutar
nombre_función(nvariables) aquí tienes que poner lo que se indica de las variables
"""

## Ejemplos

### Ejemplo 1

var1 = 100
var2 = 80

def sumar(a, b):
    return a + b  ### o resultado = a + b \n return resultado

resultado = sumar(var1, var2)
print(resultado)

### Ejemplo 2

"""Eliminar elementos duplicados de una lista, se mantiene el orden original"""
mi_lista = [1, 2, 3, 1, 2, 4, 5, 5]
lista_sin_duplicados = []
for elemento in mi_lista:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)
print(lista_sin_duplicados)
# Salida: [1, 2, 3, 4, 5]

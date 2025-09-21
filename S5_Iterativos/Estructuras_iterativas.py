# Estructuras iterativas

"""
Las estructuras iterativas en programación son mecanismos que permiten ejecutar un bloque de código
varias veces de forma repetitiva, ya sea un número conocido de veces o mientras se cumpla una condición.
En Python, las más comunes son for y while: con for recorres elementos de una secuencia (listas, cadenas,
rangos, etc.) de manera controlada, y con while repites instrucciones mientras una condición lógica sea
verdadera, lo que lo hace útil cuando no sabes de antemano cuántas repeticiones habrá. Gracias a estas
estructuras, los programas pueden automatizar tareas repetitivas, procesar colecciones de datos y reaccionar
a cambios en tiempo de ejecución, evitando tener que escribir las mismas instrucciones varias veces manualmente.
"""

## Estructura while
"""
El bucle while es una estructura iterativa que ejecuta un bloque de código mientras una condición sea 
verdadera. Es ideal cuando no sabemos cuántas veces se repetirá la acción, sino que dependerá de una 
condición dinámica. Su sintaxis es:

contador = 1
while contador <= 5:
    print("Iteración:", contador)
    contador += 1
    
Aquí, Python imprime del 1 al 5 porque la condición contador <= 5 se cumple. Una vez que deja de 
cumplirse, el bucle se detiene.
mportante: si la condición nunca deja de ser verdadera, el while se convierte en un bucle infinito,
por lo que siempre conviene asegurarse de que haya una forma de salir (ejemplo: modificando la 
variable de control o usando break).
"""

### Ejercicios while
numero_prueba = 5
i = 0
while i < numero_prueba:
    print(i)
    i += 1



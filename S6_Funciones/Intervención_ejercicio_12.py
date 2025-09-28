# Ejercicio 12

"""
Intervención

Requisitos:
- Crear una función que multiplicará 4 valores (int y floats)
- La función tendrá un parámetro o que contendrá un valor
- Mostrar 2 casos donde ese ingresó los valores donde uno no afectará el valor del parámetro
que ya contiene un valor y otro donde si lo estará afectando
"""

def multiplicar(a, b, c, d = 2.7):
    return a * b * c * d

resultado = multiplicar(3, 4, 5.6)  # 'd' mantiene su valor en 2.7
print(f"{resultado:.2f}")
resultado2 = multiplicar(7, 8, 9.1, d = 10.2)  # 'd' fue modificado a 10.5
print(f"{resultado2:.2f}")

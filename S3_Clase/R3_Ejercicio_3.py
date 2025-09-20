# Ejercicio 3
"""
Escribe un programa que reciba dos flotantes, luego estos
pasarán a ser convertidos en enteros. Indique si el primero es
múltiplo del segundo. Usar mod para la verificación si el residuo
es 0.
"""

flotante1 = 3.4
flotante2 = 6.6
entero1 = int(flotante1)
entero2 = int(flotante2)
if entero1%entero2 == 0:
    print(f"El primer número ({entero1}) es múltiplo de {entero2}")
else:
    print(f"El primer número ({entero1}) no es múltiplo de {entero2}")
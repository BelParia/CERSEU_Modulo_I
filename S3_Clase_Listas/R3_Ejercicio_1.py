# Ejercicio 1
"""
1. Escribe un programa que convierta cierta cantidad de soles a
dólares, usando un tipo de cambio que se proporciona en el
programa.
Estos valores estarán dentro de sus variables respectivamente.
La salida mostrará tres cambios que hagas respectivamente de
tres montos a convertir.
"""

print("*** Convertir de soles a dolares ***\n")
monto_1 = 110
monto_2 = 220
monto_3 = 330
tipo_cambio = 0.29  ## es el tipo de cambio en el 19/09/2025
print(f"Los S/ {monto_1}, con el tipo de cambio de {tipo_cambio}, es igual a $ {(monto_1*tipo_cambio):.2f}")
print(f"Los S/ {monto_2}, con el tipo de cambio de {tipo_cambio}, es igual a $ {(monto_2*tipo_cambio):.2f}")
print(f"Los S/ {monto_3}, con el tipo de cambio de {tipo_cambio}, es igual a $ {(monto_3*tipo_cambio):.2f}")

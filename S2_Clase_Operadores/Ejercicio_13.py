# Ejercicio 13
"""
13. Crea un programa que convierta una temperatura en grados Celsius a
Fahrenheit. La fórmula que tiene que tener en cuenta es la siguiente:
F = (C * 9)/5 + 32

Deberá imprimir algo como lo siguiente:
La temperatura en °C: 30
Temperatura en Fahrenheit: 86.00

Realizarlo con dos distintos datos para la temperatura en Celsius (usar dos
variables iniciales para obtener dos temperaturas finales en Fahrenheit)
"""
temperatura = 30
temperatura_2 = 60
convertidor_f = ((temperatura * 9)/5) + 32
convertidor_f_2 = ((temperatura_2 * 9)/5) + 32
print(f"La temperatura en °C: {temperatura}\n"
      f"Temperatura en Farenheit: {convertidor_f:.2f}\n"
      f"\nLa temperatura en °C: {temperatura_2}\n"
      f"Temperatura en Farenheit: {convertidor_f_2:.2f}")
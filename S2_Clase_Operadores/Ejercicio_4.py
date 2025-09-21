# Ejercicio 4
"""
4. Hallar el volumen de una esfera, cada dato requerido para hallar el
volumen debe estar en una variable. Mostrar el volumen por pantalla
indicándoselo al usuario. Considera a π = 3.14159
La fórmula para calcular el volumen de una esfera es: V = (4/3)
. π . r ^3 Y finalmente deberá verse lo siguiente:
Radio de la esfera: 5.5
Volumen de la esfera: 696.91
"""
radio = 5.5
valor_pi = 3.14159
volumen_esfera = (4/3) * (valor_pi * pow(radio,3))
print(f"Radio de la esfera: {radio}")
print(f"Volumen de la esfera: {volumen_esfera:.2f}")
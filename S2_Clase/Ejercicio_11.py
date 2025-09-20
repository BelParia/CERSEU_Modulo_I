# Ejercicio 11
"""
11. Identificar qué tipo de dato se obtiene al elevar tu edad con
exponente 5 y luego dividirlo por 10. Mostrar el resultado de su módulo con
3 en pantalla
"""
mi_edad = 24
operacion11 = int((pow(mi_edad,5))/10)
print(f"{operacion11%3}. Y es de {type(operacion11)}")
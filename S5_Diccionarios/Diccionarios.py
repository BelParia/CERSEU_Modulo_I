# Diccionarios en Phyton
"""
Los nombres de los key(llaves) van a ir escritos en minúsculas (por buenas prácticas)
Los llaves son propiamentes strings, pero los valors pueden ser cualquiera
"""
## Ejemplo
estudiantes = {"nombre": "Gustavo", "edad": 27, "promedio": 17.5, "Casado": False}

## Códigos
"""
- variable["key"] = valor : te permite agregar una nueva key con su respectivo valor. Si existe el key
entonces simplemente reemplazará el valor que se esté indicando.

- del variable["key"] : en base a una key te permite eleminar la misma con su respectivo valor. Pero lo
interesante es que si no existe ese key el programa te indicará un error (KeyError).

- sorted: te permite obtener los nombres de los keys de un diccionario, y lo entrega con formato lista.

-
"""
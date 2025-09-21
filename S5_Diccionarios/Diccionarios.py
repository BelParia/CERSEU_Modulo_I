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

### Obtener nombres de los keys
- sorted (variable): te permite obtener los nombres de los keys de un diccionario, y lo entrega con formato lista.
- variable.values() : te permite obtener los valores de tu lista, pero mejor "list(variable.values())",
para que no estes convirtiendo nada más y solo obtengas valores.
- variable.keys() : tambien te permite obtener el nombre de los keys, pero debes guardarlo en una
varibale nueva. Pero te aparece en un tipo de dato conjunto "([])" que aún no lo vimos, pero para que
sepas, asi que mejor toma el siguiente formato:
- diccionario_keys = list(variable.keys()) : con esto conviertes ese datos conjunto a solo una lista,
siendo igual a un sorted, asi que mejor sigue con sorted Dx.

### Conversión de diccionarios a listas
- variable_nueva = list(variable_diccionario) : te permitirá obtener una lista de los keys
- variable_nueva = list(variable_diccionario.value()) : te permitirá obtener una lista de los valores
de los keys
- variable_nueva = list(variable_diccionario.items()) : te permite obtener una tupla (que es una lista
compleja), que dento posee key y su valores respectivo separados de otros, mira los ejemplos más abajo,

"""

# Pruebas

estudiantes = {"nombre": "Gustavo", "edad": 27, "promedio": 17.5, "casado": False}

## Agregando nuevos keys y sus respectivos valores
estudiantes["distrito"] = "San Miguel"
estudiantes["habilitado"] = True
estudiantes["nombre"]= "Fiorella"

## Eliminando keys y su respectivos valores
del estudiantes["edad"]
### del estudiantes["keynoexistente"] --> 'pues te indica un eror Dx'
print(estudiantes)

## Obtener solo nombres del diccionario
base_datos = {"nombre": "Mysql", "tipo": "BD relacional", "gestor_bd": "workbench"}
keys = sorted(base_datos)
print(keys, type(keys))

base_datos_keys = list(base_datos.keys())
print(f"\nkeys: {base_datos_keys}")

## Conversión de diccionarios a listas
base_datos_list = list(base_datos)
print(f"\nDiccionario convertido en lista: {base_datos_list}")  ### solo te da los keys

base_datos_values = list(base_datos.values())    ### obtienes los valores de los keys
print(f"Values: {base_datos_values}")

### Conversión a tuplas con items()
base_datos_items = list(base_datos.items())
print(f"Items: {base_datos_items}\n")

## Recorrido de listas en BUCLE: for
notas = [12, 18, 16, 20, 11, 14, 13]
print(notas[0])
for nota in notas:
    print(nota, end = " ")

print("")

notas = [12, 18, 16, 20, 11, 14, 13]
i = 0
for nota in notas:
    notas[i] = nota - 2
    print(f"\nNotas iniciales: {nota}")
    print(notas[i])
    i = i + 1  ### esto ayuda que otras variables o datoss/valores formen un bucle
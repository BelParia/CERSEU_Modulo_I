# Ejercicio 07

"""
Intervención

Requisitos:
- Ingresar su nombre y apellido por consola
(variables distintas)
- Obtener el tamaño de tu nombre completo y muéstralo en consola
- Imprimir el resultado final, tod0 en mayúsculas: .upper()
- Indicar mediante condicionales si el tamaño del nombre es mayor o no al apellido ingresado
- Solamente ingresar el apellido paterno
"""

nombre = input("Indique su nombre: ").strip()
apellido = input("Indique su apellido paterno: ").strip()
ape= apellido.replace(" ","")  # para evitar los espacios entre apellidos
nombre_completo = nombre + " " + apellido
print(f"Buenos días, {nombre_completo.upper()}")
if len(nombre) > len(ape):
    print(f"El tamaño del nombre ({len(nombre)}) es mayor al de tu apellido ({len(ape)})")
else:
    print(f"El tamaño de tu apellido es ({len(ape)}) es mayor que tu nombre ({len(nombre)})")

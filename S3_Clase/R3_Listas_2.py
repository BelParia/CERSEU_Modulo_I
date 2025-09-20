# Ejercicio 2
"""
2. Crear un programa en Python donde tendrás una lista con 6 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista.
"""

lista_departamentos = ["Depa1", "Depa2", "Depa3", "Depa4", "Depa5", "Depa6"]
print(lista_departamentos)
print("Todos esos son los departamentos disponibles")
eleccion_departamento = input("\nElija 2 departamentos, separalos por un espacio: ")
primer_depa_lista = eleccion_departamento.split(" ")
lista_departamentos[0] = primer_depa_lista[1]
print(lista_departamentos)
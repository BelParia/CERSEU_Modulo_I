"""
- Crear diccionario de contactos, el cual tendrá como key: Nombre, value: teléfono (9 dígitos)
- Verificar si existe el número de contacto de una persona, para esto estos valores serán
verificados con variables, entre 2 que existan y dos que no existan
- Indicar mediante un mensaje si está o no agregados a la agenda de contactos
- En caso que no exista agregarlo al diccionario de contactos
- Mostrar finalmente el diccionario actualizado.
"""
from random import randint
diccionario_contactos = {"Brayan": 918480044, "Mirian": 918480011, "Pepe": 918480022, "María": 918480033}
lista_keys = sorted(diccionario_contactos)
lista_values = list(diccionario_contactos.values())
print(lista_keys)
print(lista_values)
contactos_verificar = ["Brayan", "Mirian", "Carlos", "Valeria"]

for contacto in contactos_verificar:
    if contacto in lista_keys:
        print(f"El contacto de {contacto}, con número {diccionario_contactos[contacto]}, SI existe"
              f" en el diccionario de contactos")
    else:
        numero_contacto = randint(900000000, 999999999)
        print(f"El contacto de {contacto}, con número {numero_contacto}, NO existe"
              f" en el diccionario de contactos")
        diccionario_contactos[contacto]= numero_contacto

print(f"El diccionario de contactos actualizado:\n"
      f"{diccionario_contactos}")
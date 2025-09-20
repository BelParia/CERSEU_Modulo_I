# Ejercicio 4
"""
4. Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y luego esta será agregada a la lista.
Finalmente mostrar la lista actualizada en consola.
"""

lista_nombres = ["Brayan", "Roly", "Mirian", "Carlos", "Ian"]
nombre_elegido = input("Ingrese el nombre de un estudiante: ")
if nombre_elegido in lista_nombres:
    lista_nombres.remove(nombre_elegido)
    print(f"El nombre de {nombre_elegido} será eliminado")
    print(f"La lista actualizada es {lista_nombres}")
else:
    lista_nombres.append(nombre_elegido)
    print(f"El nombre que indicaste ({nombre_elegido}) no está en la\n"
          f"lista general, asi que será añadida a la lista:\n"
          f"{lista_nombres}")
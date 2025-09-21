# Entradas y salidas
"""
A entradas y salidas yo le llamo "Llamado por consola", que en sí es la actividad de input.
En Python, la función input() permite hacer lo que llamas un “llamado por consola”:
básicamente detener el programa y esperar que el usuario escriba algo desde el teclado, lo que
convierte al script en interactivo. Por defecto, lo que devuelve siempre es una cadena de texto
(string), aunque luego puedes transformarla a otros tipos de datos (como int() o float()). Por ejemplo,
si escribes nombre = input("¿Cómo te llamas? "), el programa mostrará el mensaje y quedará en pausa
hasta que el usuario escriba su respuesta, la cual se guardará en la variable nombre. Esto hace posible
que los programas en Python reciban datos externos en tiempo de ejecución, en lugar de estar limitados
solo a lo que ya está escrito en el código.
"""

## Dato curioso
"""
Algo que talvez no es propiamente del Entradas y salidas es que propiamente se pueden acortar
cierto valores al ser nombrados, sé que lo estoy explicando mal, pero creeme que puede de alguna
manera cortar ciertas líneas de códigos.
"""

datos = ["Pollito", "24", "Darian"]
apodo, edad, nombre = datos
print(f"El nombre es {nombre}")
print(f"La edad que tiene: {24} años")
print(f"Su apodo es {apodo}")

## Ejercicios
edad = int(input("\nIndique su edad (en años): 24"))
if 0 < edad < 18:
    print("1. Usted es menor de edad")
elif 19 <= edad < 65:
    print("2. Usted es una persona adulta")
elif 65 <= edad < 100:
    print("3. Usted es una persona adulta de la tercera edad")
elif edad >= 100:
    print("Felicidades, es de las pocas personas que poseen 3 dígitos como edad")
### Xd, pero quien sabe tal vez algún día alquien posee como 567 años, o algo así.
else:
    print("Ingrese una edad correcta")


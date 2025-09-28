# Manejo de cadenas

"""
En teoría esto es la parte básica para el manejo de cadenas, de hecho debería haberse revisado al inicio de
estas clases, pero bueno. Principalmente trata de códigos para cadenas, te permitirá modificar algunos
aspectos necesario en las cadenas .
"""
## Códigos de manejo de cadenas
"""
x.split() : te permite separar los strings dentro de tu variable cadena, como los nombres que siembre estan
espaciados por un " " o espacio, asi que el split te permite separarlos como strings individuales y te crea
una lista con ellas.
    x.split(sep="separador"): tambien puedes separar los strings en base a un separador, como las ",".
        *variable = si por ejemplo no sabes cuantos strings tiene tu cadena, puedes guardarlos de esa manera,
        pero claro, primero le haces un x.split() luego las strings que conozcas los agrupas, pero lo que no
        pues los guardaras en una nueva variable:
        xintentos = "X1 X2 X3 X4 ... XN"
        var1, var2, *resto = xintentos.split()
        print(var1) = "X1" ; print(var2) = "X2" siendo estos 2 conocidos
        print(resto) = ["X3", "X4", "...", "XN"] siendo estos los que no conocemos pero ya los agrupamos

x.find("string") : te busca un string específico en tu cadena, pero solo te encuentra el índice que corresponde
a la primera letra coincidente de tu busqueda, si hay repetidos no sabras cuantos realmente hay.

r.strip(): elimina los espacios del inico y final de la cadena
    x.lstrip(): borra los espacios de la izquierda del todo (left)
    x.rstrip(): borra los espacio de la derecha del todo (left)

x.upper(): te covierte cada caracter a uno de tipo mayuscualas
x.lower(): te covierte cada caracter a uno de tipo minúsuclas
x.title(): te convierte la cadena como si fuera un título: inicio de cada string con mayuscula y lo demás minúscula
   x.capitalize() : te convierte solo la primera letra de la cadena en mayuscula

"""

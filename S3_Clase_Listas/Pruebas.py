# Lista original de invitados
guests = ["Ana", "Katherine", "Pedro", "Luis", "Raúl", "Fiorella", "Miguel"]

# Lista para nombres con número impar de letras
impares = []
pares = []

# Clasificación según longitud del nombre
for nombre in guests:
    if len(nombre) % 2 == 1:  ## imopar
        impares.append(nombre)
    else:
        pares.append(nombre)

# Lista reorganizada
reorganizados = impares + pares

# Mostrar resultado
print("Lista reorganizada:")
print(reorganizados)






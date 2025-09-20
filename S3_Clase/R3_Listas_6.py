# Ejercicio 6
"""
6. Tiene una lista de invitados que llegaron a una boda de acuerdo a su orden
de llegada:
guests = [“Ana”, “Katherine”, “Pedro”, “Luis”, “Raúl”, “Fiorella”, “Miguel”]
Se requiere reorganizar esta lista.
Primero los que tienen número impar y en el orden que fueron llegando
Segundo las personas que tienen número par de letras
Input: [“Ana”, “Pedro”, “Raúl”, “Fiorella”, “Katherine”, “Miguel”, “Luis”]
Output: [“Ana”, “Pedro”, ”Katherine”, “Raúl”, “Fiorella”, “Miguel”, “Luis”]
"""

# Lista original de invitados
guests = ["Ana", "Katherine", "Pedro", "Luis", "Raúl", "Fiorella", "Miguel"]
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

print("Lista reorganizada:")
print(reorganizados)

## Observaciones:
"""
Al igual que el ejercicio 5, consideré el uso de un 'for' ya que ahorraría
muchos pasos para realizar lo que se indica en este ejercicio.
"""


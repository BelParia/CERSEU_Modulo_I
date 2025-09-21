# Ejercicio 11
"""
Intervención

Requisitos:
- Dentro de una empresa se vaa solicitar pedir el nombre y apelldio del empleado (input)
- Distrito de residencia ingresado por teclado
- Sueldo y cálculo del bono final de año, que será el triple del sueldo mensual menos el 10% del sueldo
- Todos estos datos se van a ingresar a un diccionario
- Asignar a 3 variables los valores del diccionario
- Mostrar por la terminal (output) el mensaje de: "'Nombre' 'Apellido',
recibirá 'bono' soles de fin de año"
"""

print("*** Bono de final de año ***")
nombre_usuario = input("Digite su nombre y apellido: ")
distrito_residencia = input("¿En qué distrito reside actualmente?: ")
sueldo = float(input("¿Cuanto le paga la empresa actualmente (en S/)?: "))
bono_final = (3*sueldo) - (0.10)*sueldo
diccionario_usuario = {"nombre": nombre_usuario, "distrito": distrito_residencia, "sueldo": sueldo, "bono": bono_final}
print("Calculando...Espere un momento por favor")
print("...")
print("...")
print("...")
print(f"Estimado, {nombre_usuario}, en base al sueldo que percibe, S/ {sueldo:.2f}\n"
      f"ustede debería recibir un Bono de Final de Año de S/ {bono_final:.2f}")
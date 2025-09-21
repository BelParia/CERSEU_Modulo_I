# Ejercicio 1
nombre = "Brayan Roly de la Cruz Condori"
mi_saludo = f"¡HI {nombre}!"
print(mi_saludo)

# Ejercicio 2
numero_entero = 5
operacion2 = float((numero_entero * 10) - 10)
print(f"{operacion2}, y es de {type(operacion2)}")

# Ejercicio 3
numero_cadena = "3"
numero_entero_2 = 4
print(f"{int(numero_cadena) + numero_entero_2}")

# Ejercicio 4
radio = 5.5
valor_pi = 3.14159
volumen_esfera = (4/3) * (valor_pi * pow(radio,3))
print(f"Radio de la esfera: {radio}")
print(f"Volumen de la esfera: {volumen_esfera}")

# Ejercicio 5
sueldo = 315
if sueldo % 2 == 0:
    print("La variable es par")
else:
    print("La variable es impar")

# Ejercicio 6
dato1 = 1.2
dato2 = 3.4
dato3 = 5.6
dato4 = 7.8
dato5 = 9.1
resultado_media = (dato1 + dato2 + dato3 + dato4 + dato5)/5
print(f"Media:{resultado_media}. Y es de {type(resultado_media)}")

# Ejercicio 7
numero1 = 31
numero2 = -32
numero3 = 33
print(f"{numero1%3} + {numero2%5} + {numero3%7}")

# Ejercicio 8
lista = []
lista2 = [9,1]
if lista:
    print("La lista contiene al menos un elemento")
else:
    print("La lista esta vacía")

# Ejercicio 9
exponente = 6
resultado9 = pow(3,exponente)
resta = resultado9 - (2*resultado9)
print(resta)

# Ejercicio 10
numero_flotante = 1.234567
print(f"1 decimal: {numero_flotante:.1f}")
print(f"2 decimales: {numero_flotante:.2f}")
print(f"4 decimales: {numero_flotante:.4f}")

# Ejercicio 11
mi_edad = 24
operacion11 = (pow(mi_edad,5))/10
print(f"{operacion11%3}. Y es de {type(operacion11)}")

# Ejercicio 12
print("*** Programa de Pollitos UNMSM ***")
nombre_cliente = "Brayan de la Cruz"
producto = "Pollo a la brasa"
precio_pollito = 50.50
cantidad = 2
print(f"Buen día, {nombre_cliente}, el detalle de su compra es el siguiente:\n"
      f"-   Producto: Pollo a la brasa\n"
      f"-   Precio unitario: {precio_pollito}\n"
      f"-   Cantidad: {cantidad}\n"
      f"-   Total a pagar: {precio_pollito*cantidad}")

# Ejercicio 13
temperatura = 30
temperatura_2 = 60
convertidor_f = ((temperatura * 9)/5) + 32
convertidor_f_2 = ((temperatura_2 * 9)/5) + 32
print(f"La temperatura en °C: {temperatura}\n"
      f"Temperatura en Farenheit: {convertidor_f:.2f}\n"
      f"\nLa temperatura en °C: {temperatura_2}\n"
      f"Temperatura en Farenheit: {convertidor_f_2:.2f}")


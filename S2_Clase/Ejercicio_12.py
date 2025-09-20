# Ejercicio 12
"""
12. Escribe un programa que almacene información de un producto: Tu
nombre, nombre del producto, precio unitario (float), cantidad (int) e
imprimirá finalmente algo como lo siguiente:

Buen día Nombre, el detalle de su compra es el siguiente: -
Producto: Pollo a la brasa - - -
Precio unitario: 50.50
Cantidad: 2
Total a pagar: 101
"""
print("*** Programa de Pollitos UNMSM ***")
nombre_cliente = "Brayan de la Cruz"
producto = "Pollo a la brasa"
precio_pollito = 50.50
cantidad = 2
print(f"Buen día, {nombre_cliente}, el detalle de su compra es el siguiente:\n"
      f"-   Producto: Pollo a la brasa\n"
      f"-   Precio unitario: {precio_pollito:.2f}\n"
      f"-   Cantidad: {cantidad}\n"
      f"-   Total a pagar: {precio_pollito*cantidad:.0f}")
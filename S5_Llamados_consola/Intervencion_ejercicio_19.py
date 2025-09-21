# Ejercicio 19

"""
Intervención

Uso de if ternarios
Requisitos:
- Ingresar por teclado el sueldo del empleado
- Si el sueldo es mayor que 4000, imprimir "Su sueldo no tiene bonificación"
- Caso contrario indicar: "Su sueldo tiene bonificación este año y será de :
sueldo_final", sueldo_final = sueldo + 20% * sueldo
"""

sueldo_empleado = float(input("Indique el sueldo del empleado (en S/): "))
sueldo_final = sueldo_empleado + 0.20*sueldo_empleado
sueldo = "Su sueldo no tiene bonificación" if sueldo_empleado > 4000 else ("Su sueldo tiene bonificación "
                                                                          f"este año y será de S/ {sueldo_final:.2f}")
print(sueldo)